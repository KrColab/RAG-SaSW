#!/usr/bin/env python3
"""
Hybrid Ontology-Enhanced RAG Engine for the Construction Company Knowledge System.

Combines:
1. Formal OWL Ontology axioms & hierarchy (`stavebna_firma_ontology - kópia.owl`)
2. 10 Technical & Operational PDF Documents (`./PDF/*.pdf`)
3. Hybrid Retrieval: Word/Subword Cosine Vector Search + OWL Graph Expansion
4. Local LLM Generation via Ollama (`qwen2.5:7b` default) with streaming support
"""

import glob
import json
import os
import re
from typing import Dict, Generator, List, Optional, Tuple

import numpy as np
import pymupdf
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from ontology_parser import ConstructionOntology, camel_to_words

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OWL_PATH = os.path.join(BASE_DIR, "stavebna_firma_ontology - kópia.owl")
DEFAULT_PDF_DIR = os.path.join(BASE_DIR, "PDF")
INDEX_CACHE_PATH = os.path.join(BASE_DIR, "vector_store_cache.json")
OLLAMA_BASE_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

DEFAULT_SYSTEM_PROMPT = """You are an expert AI Knowledge Assistant for ApexBuild Construction Corp.
You answer questions in English using ONLY the provided context, which has two parts:
1. [OWL ONTOLOGY AXIOMS]: Formal classes, subclass hierarchies, properties, and restrictions from `stavebna_firma_ontology - kópia.owl`.
2. [PDF DOCUMENT EXCERPTS]: Extracted text chunks from the company's 10 official PDF documents in the `./PDF/` folder.

Guidelines:
- Always ground your answer in both the OWL Ontology rules and the specific facts, numbers, budgets, personnel, and tables from the PDF excerpts.
- Explicitly cite OWL classes/properties in backticks (e.g., `EuroveaTower`, `ResidentialProject`, `usesMaterial`) and cite the PDF filename and page number in brackets (e.g., [04_eurovea_tower_and_apartments.pdf, p. 1]).
- If a question asks about logical rules, restrictions, disjointness, or class hierarchy, explain the exact OWL axiom clearly.
- If the answer is not contained in the provided ontology or PDF context, state clearly that the information is not available in the knowledge base."""


class HybridOntologyRAG:
    def __init__(
        self,
        owl_path: str = DEFAULT_OWL_PATH,
        pdf_dir: str = DEFAULT_PDF_DIR,
        chunk_size: int = 850,
        chunk_overlap: int = 150,
    ):
        self.owl_path = owl_path
        self.pdf_dir = pdf_dir
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.ontology = ConstructionOntology(self.owl_path)
        self.owl_chunks: List[Dict] = []
        self.pdf_chunks: List[Dict] = []
        self.pdf_files_summary: List[Dict] = []

        # Vectorizers for PDF and OWL chunks
        self.pdf_word_vec: Optional[TfidfVectorizer] = None
        self.pdf_char_vec: Optional[TfidfVectorizer] = None
        self.pdf_word_matrix = None
        self.pdf_char_matrix = None

        self.owl_word_vec: Optional[TfidfVectorizer] = None
        self.owl_word_matrix = None

        self.build_index()

    def _chunk_text(self, text: str) -> List[str]:
        """Split page text into clean overlapping semantic chunks."""
        # Normalize excessive blank lines while keeping paragraph structure
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        full_text = "\n\n".join(paragraphs)
        if len(full_text) <= self.chunk_size:
            return [full_text] if full_text else []

        chunks = []
        start = 0
        n = len(full_text)
        while start < n:
            end = min(start + self.chunk_size, n)
            if end < n:
                # Try to break at a newline or sentence period
                nl_pos = full_text.rfind("\n", start + int(self.chunk_size * 0.5), end)
                dot_pos = full_text.rfind(". ", start + int(self.chunk_size * 0.5), end)
                best_break = max(nl_pos, dot_pos + 1 if dot_pos != -1 else -1)
                if best_break > start:
                    end = best_break
            chunk_str = full_text[start:end].strip()
            if chunk_str:
                chunks.append(chunk_str)
            if end >= n:
                break
            start = max(start + 1, end - self.chunk_overlap)
        return chunks

    def build_index(self) -> Dict:
        """Parse OWL ontology and all PDF files in ./PDF/, enrich with ontology tags, and build vector matrices."""
        # 1. Build OWL Ontology chunks
        self.owl_chunks = self.ontology.get_all_verbalized_chunks()

        # 2. Load and chunk all PDFs in ./PDF/
        self.pdf_chunks = []
        self.pdf_files_summary = []
        pdf_paths = sorted(glob.glob(os.path.join(self.pdf_dir, "*.pdf")))

        chunk_counter = 0
        for path in pdf_paths:
            fname = os.path.basename(path)
            doc = pymupdf.open(path)
            total_chars = 0
            doc_classes = set()
            file_chunk_count = 0

            for page_idx, page in enumerate(doc):
                raw_text = page.get_text("text")
                # Strip repetitive running header/footer lines if present cleanly
                lines = [
                    line for line in raw_text.splitlines()
                    if not line.startswith("ApexBuild Construction Corp. | DOC-")
                    and not (line.startswith("Ontology Focus:") or re.match(r"^Page \d+ of \d+$", line.strip()))
                ]
                cleaned_page_text = "\n".join(lines).strip()
                total_chars += len(cleaned_page_text)

                page_chunks = self._chunk_text(cleaned_page_text)
                for c_idx, c_text in enumerate(page_chunks):
                    chunk_counter += 1
                    file_chunk_count += 1
                    matched_entities = self.ontology.match_entities_in_text(c_text)
                    expanded_entities = set(matched_entities)
                    for ent in matched_entities:
                        if ent in self.ontology.classes:
                            expanded_entities.update(self.ontology.get_transitive_superclasses(ent))
                    doc_classes.update(matched_entities)

                    # Create an enriched searchable representation combining text + spaced ontology tags
                    tag_boost_str = " ".join(
                        f"{ent} {camel_to_words(ent)}" for ent in sorted(expanded_entities)
                    )
                    self.pdf_chunks.append({
                        "id": f"PDF_{chunk_counter:03d}",
                        "source": fname,
                        "source_type": "pdf",
                        "page": page_idx + 1,
                        "chunk_index_on_page": c_idx + 1,
                        "text": c_text,
                        "search_text": f"{fname} {c_text}\nOntology Tags: {tag_boost_str}",
                        "ontology_classes": sorted(matched_entities),
                        "expanded_ontology_classes": sorted(expanded_entities),
                    })
            doc.close()
            self.pdf_files_summary.append({
                "filename": fname,
                "pages": len(pymupdf.open(path)),
                "chunks": file_chunk_count,
                "chars": total_chars,
                "matched_classes": sorted(doc_classes),
            })

        # 3. Fit Vectorizers on PDF chunks and OWL chunks
        if self.pdf_chunks:
            pdf_corpus = [c["search_text"] for c in self.pdf_chunks]
            self.pdf_word_vec = TfidfVectorizer(
                ngram_range=(1, 2),
                stop_words="english",
                sublinear_tf=True,
            )
            self.pdf_word_matrix = self.pdf_word_vec.fit_transform(pdf_corpus)

            self.pdf_char_vec = TfidfVectorizer(
                analyzer="char_wb",
                ngram_range=(3, 5),
                sublinear_tf=True,
            )
            self.pdf_char_matrix = self.pdf_char_vec.fit_transform(pdf_corpus)

        if self.owl_chunks:
            owl_corpus = [
                f"{c['entity_name']} {camel_to_words(c['entity_name'])} {c['text']}"
                for c in self.owl_chunks
            ]
            self.owl_word_vec = TfidfVectorizer(
                ngram_range=(1, 2),
                stop_words="english",
                sublinear_tf=True,
            )
            self.owl_word_matrix = self.owl_word_vec.fit_transform(owl_corpus)

        # Save lightweight metadata cache
        try:
            with open(INDEX_CACHE_PATH, "w", encoding="utf-8") as f:
                json.dump({
                    "owl_classes_count": len(self.ontology.classes),
                    "owl_properties_count": len(self.ontology.properties),
                    "pdf_files_count": len(self.pdf_files_summary),
                    "pdf_chunks_count": len(self.pdf_chunks),
                    "files": self.pdf_files_summary,
                }, f, indent=2)
        except Exception:
            pass

        return {
            "owl_classes": len(self.ontology.classes),
            "owl_properties": len(self.ontology.properties),
            "pdf_files": len(self.pdf_files_summary),
            "pdf_chunks": len(self.pdf_chunks),
        }

    def expand_query_with_ontology(self, query: str) -> Dict:
        """
        Identify ontology entities in the user query and expand with superclasses,
        subclasses, disjoint classes, and property restrictions.
        """
        direct_matches = self.ontology.match_entities_in_text(query)
        expanded_terms = set(direct_matches)
        reasoning_notes = []

        for ent in direct_matches:
            if ent in self.ontology.classes:
                cinfo = self.ontology.classes[ent]
                sups = self.ontology.get_transitive_superclasses(ent)
                subs = self.ontology.get_transitive_subclasses(ent)
                expanded_terms.update(sups)
                expanded_terms.update(cinfo.subclasses)
                expanded_terms.update(cinfo.related_terms)
                if sups:
                    reasoning_notes.append(f"`{ent}` ⊑ {', '.join(f'`{s}`' for s in sups)}")
                if subs:
                    reasoning_notes.append(f"Subclasses of `{ent}`: {', '.join(f'`{s}`' for s in subs[:8])}")
                for eq in cinfo.equivalents:
                    reasoning_notes.append(f"Equivalent axiom for `{ent}`: {eq}")
                for r in cinfo.restrictions:
                    reasoning_notes.append(f"Restriction on `{ent}`: {r}")
            elif ent in self.ontology.properties:
                pinfo = self.ontology.properties[ent]
                expanded_terms.update(pinfo.domains)
                expanded_terms.update(pinfo.ranges)
                expanded_terms.update(pinfo.inverse_of)
                reasoning_notes.append(
                    f"Property `{ent}` (domain: {', '.join(pinfo.domains) or 'Thing'} -> range: {', '.join(pinfo.ranges) or 'Thing'})"
                )

        expanded_query_str = query + " " + " ".join(
            f"{t} {camel_to_words(t)}" for t in sorted(expanded_terms)
        )
        return {
            "direct_entities": direct_matches,
            "expanded_entities": sorted(expanded_terms),
            "reasoning_notes": reasoning_notes,
            "expanded_query": expanded_query_str,
        }

    def retrieve(
        self,
        query: str,
        top_k_pdf: int = 5,
        top_k_owl: int = 6,
        use_ontology_expansion: bool = True,
    ) -> Dict:
        """
        Retrieve top-K relevant PDF chunks and top-K OWL ontology axioms using
        hybrid vector similarity + ontology graph overlap boosting.
        """
        onto_info = self.expand_query_with_ontology(query)
        search_query = onto_info["expanded_query"] if use_ontology_expansion else query
        direct_set = set(onto_info["direct_entities"])
        expanded_set = set(onto_info["expanded_entities"])

        # 1. Retrieve OWL Ontology Chunks
        retrieved_owl = []
        if self.owl_chunks and self.owl_word_vec is not None:
            q_owl_vec = self.owl_word_vec.transform([search_query])
            owl_sims = cosine_similarity(q_owl_vec, self.owl_word_matrix).flatten()

            for idx, chunk in enumerate(self.owl_chunks):
                score = float(owl_sims[idx])
                ename = chunk["entity_name"]
                if ename in direct_set:
                    score += 0.65  # Exact entity match boost
                elif ename in expanded_set:
                    score += 0.25  # Graph neighbor match boost
                retrieved_owl.append({**chunk, "score": round(score, 4)})

            retrieved_owl.sort(key=lambda x: x["score"], reverse=True)
            retrieved_owl = retrieved_owl[:top_k_owl]

        # 2. Retrieve PDF Chunks
        retrieved_pdf = []
        if self.pdf_chunks and self.pdf_word_vec is not None and self.pdf_char_vec is not None:
            q_word = self.pdf_word_vec.transform([search_query])
            q_char = self.pdf_char_vec.transform([ query ])

            word_sims = cosine_similarity(q_word, self.pdf_word_matrix).flatten()
            char_sims = cosine_similarity(q_char, self.pdf_char_matrix).flatten()

            for idx, chunk in enumerate(self.pdf_chunks):
                base_sim = 0.70 * float(word_sims[idx]) + 0.30 * float(char_sims[idx])
                chunk_direct_overlap = len(direct_set.intersection(chunk["ontology_classes"]))
                chunk_expanded_overlap = len(expanded_set.intersection(chunk["expanded_ontology_classes"]))
                onto_boost = (0.12 * chunk_direct_overlap + 0.03 * chunk_expanded_overlap) if use_ontology_expansion else 0.0
                total_score = base_sim + onto_boost
                retrieved_pdf.append({
                    **chunk,
                    "score": round(total_score, 4),
                    "vector_score": round(base_sim, 4),
                    "ontology_boost": round(onto_boost, 4),
                })

            retrieved_pdf.sort(key=lambda x: x["score"], reverse=True)
            retrieved_pdf = retrieved_pdf[:top_k_pdf]

        return {
            "query": query,
            "ontology_expansion": onto_info,
            "owl_results": retrieved_owl,
            "pdf_results": retrieved_pdf,
        }

    def build_messages(
        self,
        query: str,
        retrieval_result: Dict,
        chat_history: Optional[List[Dict]] = None,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    ) -> List[Dict]:
        """Construct the chat message payload for Ollama `/api/chat`."""
        owl_blocks = []
        for i, item in enumerate(retrieval_result["owl_results"], 1):
            owl_blocks.append(f"[OWL-{i}] (Score: {item['score']})\n{item['text']}")

        pdf_blocks = []
        for i, item in enumerate(retrieval_result["pdf_results"], 1):
            classes_str = ", ".join(item["ontology_classes"][:8])
            pdf_blocks.append(
                f"[PDF-{i}] Source: {item['source']} (Page {item['page']}) | "
                f"Matched OWL Classes: [{classes_str}] | Score: {item['score']}\n"
                f"{item['text']}"
            )

        context_str = (
            "=== 1. FORMAL OWL ONTOLOGY AXIOMS (`stavebna_firma_ontology - kópia.owl`) ===\n"
            + ("\n\n".join(owl_blocks) if owl_blocks else "No ontology axioms retrieved.")
            + "\n\n=== 2. EXTRACTED PDF DOCUMENT CHUNKS (`./PDF/`) ===\n"
            + ("\n\n".join(pdf_blocks) if pdf_blocks else "No PDF chunks retrieved.")
        )

        messages = [{"role": "system", "content": system_prompt}]
        if chat_history:
            # Keep last 6 turns of conversation history for multi-turn continuity
            for msg in chat_history[-6:]:
                if msg.get("role") in ("user", "assistant") and msg.get("content"):
                    messages.append({"role": msg["role"], "content": msg["content"]})

        user_prompt = (
            f"Use the following retrieved knowledge base context (OWL Ontology + PDF Documents) to answer the user's question accurately in English.\n\n"
            f"{context_str}\n\n"
            f"USER QUESTION: {query}\n\n"
            f"Provide a clear, well-structured answer in English and cite both the relevant OWL Ontology classes/properties and the source PDF filenames with page numbers."
        )
        messages.append({"role": "user", "content": user_prompt})
        return messages

    @staticmethod
    def get_available_ollama_models() -> List[str]:
        """Fetch installed models from local Ollama instance."""
        try:
            resp = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=3)
            if resp.status_code == 200:
                data = resp.json()
                models = [m["name"] for m in data.get("models", [])]
                return models if models else ["qwen2.5:7b"]
        except Exception:
            pass
        return ["qwen2.5:7b"]

    @staticmethod
    def stream_ollama_chat(
        messages: List[Dict],
        model: str = "qwen2.5:7b",
        temperature: float = 0.2,
        num_ctx: int = 8192,
        top_p: float = 0.9,
        num_predict: int = 1024,
    ) -> Generator[str, None, None]:
        """Stream response tokens from local Ollama `/api/chat` endpoint."""
        payload = {
            "model": model,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": float(temperature),
                "num_ctx": int(num_ctx),
                "top_p": float(top_p),
                "num_predict": int(num_predict),
            },
        }
        try:
            with requests.post(
                f"{OLLAMA_BASE_URL}/api/chat",
                json=payload,
                stream=True,
                timeout=180,
            ) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if not line:
                        continue
                    data = json.loads(line.decode("utf-8"))
                    chunk = data.get("message", {}).get("content", "")
                    if chunk:
                        yield chunk
                    if data.get("done"):
                        break
        except requests.exceptions.ConnectionError:
            yield (
                "⚠️ **Error connecting to Ollama at `http://localhost:11434`.** "
                "Please make sure Ollama is running (`ollama serve`) and model "
                f"`{model}` is pulled (`ollama pull {model}`)."
            )
        except Exception as e:
            yield f"⚠️ **Ollama Generation Error:** {str(e)}"


if __name__ == "__main__":
    engine = HybridOntologyRAG()
    print(f"Indexed {len(engine.owl_chunks)} OWL chunks and {len(engine.pdf_chunks)} PDF chunks.")
    sample_q = "What is the difference between Electrician and Plumber in the ontology, and who are the employees in those roles?"
    res = engine.retrieve(sample_q, top_k_pdf=3, top_k_owl=4)
    print("Direct matched OWL entities:", res["ontology_expansion"]["direct_entities"])
    print("Top OWL hit:", res["owl_results"][0]["entity_name"], res["owl_results"][0]["score"])
    print("Top PDF hit:", res["pdf_results"][0]["source"], "p.", res["pdf_results"][0]["page"], "score:", res["pdf_results"][0]["score"])

