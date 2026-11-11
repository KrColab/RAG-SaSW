#!/usr/bin/env python3
"""
Clean, Modern Streamlit Web UI for ApexBuild Construction Company Ontology-RAG.
Designed for clarity, readability, and seamless Dark/Light mode compatibility.
Runs locally on http://localhost:8501 and connects to Ollama (qwen2.5:7b).
"""

import time
import streamlit as st

from rag_engine import DEFAULT_SYSTEM_PROMPT, HybridOntologyRAG

st.set_page_config(
    page_title="ApexBuild AI | Construction Ontology RAG",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Clean, theme-adaptive CSS (works seamlessly in both Dark Mode and Light Mode)
st.markdown(
    """
    <style>
    /* Center and give breathing room to main content */
    .block-container {
        max-width: 1050px !important;
        padding-top: 5.2rem !important;
        padding-bottom: 4rem !important;
    }

    /* Clean minimalist top header */
    .app-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.9rem 1.25rem;
        border-radius: 14px;
        background: rgba(59, 130, 246, 0.08);
        border: 1px solid rgba(59, 130, 246, 0.22);
        margin-bottom: 1.4rem;
    }
    .app-header-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.01em;
    }
    .app-header-sub {
        font-size: 0.84rem;
        opacity: 0.78;
        margin-top: 2px;
    }
    .badge-row {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }
    .status-badge {
        font-size: 0.76rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(59, 130, 246, 0.14);
        border: 1px solid rgba(59, 130, 246, 0.3);
        white-space: nowrap;
    }

    /* Tag pills for OWL classes */
    .onto-pill {
        display: inline-block;
        padding: 2px 9px;
        border-radius: 6px;
        font-size: 0.76rem;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        font-weight: 500;
        background: rgba(59, 130, 246, 0.14);
        border: 1px solid rgba(59, 130, 246, 0.32);
        margin-right: 6px;
        margin-bottom: 5px;
    }
    .onto-pill-green {
        display: inline-block;
        padding: 2px 9px;
        border-radius: 6px;
        font-size: 0.76rem;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        font-weight: 500;
        background: rgba(16, 185, 129, 0.14);
        border: 1px solid rgba(16, 185, 129, 0.32);
        margin-right: 6px;
        margin-bottom: 5px;
    }

    /* Clean cards inside source tabs */
    .context-card {
        padding: 0.9rem 1.1rem;
        border-radius: 10px;
        background: rgba(148, 163, 184, 0.07);
        border: 1px solid rgba(148, 163, 184, 0.22);
        margin-bottom: 0.75rem;
    }
    .context-card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.45rem;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .score-pill {
        font-size: 0.74rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 999px;
        background: rgba(99, 102, 241, 0.16);
        border: 1px solid rgba(99, 102, 241, 0.32);
    }
    .context-body {
        font-size: 0.86rem;
        line-height: 1.55;
        opacity: 0.92;
        white-space: pre-wrap;
    }

    /* Chat message spacing */
    [data-testid="stChatMessage"] {
        padding-top: 0.6rem;
        padding-bottom: 0.6rem;
    }

    /* Center suggestion pills cleanly */
    [data-testid="stPills"] > div {
        justify-content: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource(show_spinner="Loading OWL Ontology & 10 PDF Documents...")
def get_rag_engine(chunk_size: int = 850, chunk_overlap: int = 150) -> HybridOntologyRAG:
    return HybridOntologyRAG(chunk_size=chunk_size, chunk_overlap=chunk_overlap)


def render_sources_panel(retrieval_res: dict):
    """Render a clean, tabbed citation panel under an assistant answer."""
    onto_exp = retrieval_res.get("ontology_expansion", {})
    owl_results = retrieval_res.get("owl_results", [])
    pdf_results = retrieval_res.get("pdf_results", [])
    direct_entities = onto_exp.get("direct_entities", [])
    notes = onto_exp.get("reasoning_notes", [])

    expander_title = (
        f"📚 View Sources & Ontology Context  ·  "
        f"{len(pdf_results)} PDF Excerpts  ·  {len(owl_results)} OWL Rules"
    )
    with st.expander(expander_title, expanded=False):
        if direct_entities:
            pills = "".join(f"<span class='onto-pill'>{e}</span>" for e in direct_entities)
            st.markdown(f"**Detected Ontology Entities:** &nbsp; {pills}", unsafe_allow_html=True)

        t_pdf, t_owl, t_reason = st.tabs([
            f"📄 PDF Sources ({len(pdf_results)})",
            f"🧬 OWL Ontology Rules ({len(owl_results)})",
            f"🧠 Reasoning Path ({len(notes)})",
        ])

        with t_pdf:
            for i, item in enumerate(pdf_results, 1):
                tags_html = "".join(
                    f"<span class='onto-pill'>{c}</span>" for c in item.get("ontology_classes", [])[:6]
                )
                st.markdown(
                    f"""
                    <div class="context-card">
                        <div class="context-card-header">
                            <span>📄 [{i}] {item['source']} &nbsp;·&nbsp; Page {item['page']}</span>
                            <span class="score-pill">Relevance: {item['score']:.2f}</span>
                        </div>
                        <div style="margin-bottom: 6px;">{tags_html}</div>
                        <div class="context-body">{item['text']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with t_owl:
            for i, item in enumerate(owl_results, 1):
                st.markdown(
                    f"""
                    <div class="context-card">
                        <div class="context-card-header">
                            <span>🧬 [{i}] OWL {item['entity_name']}</span>
                            <span class="score-pill">Score: {item['score']:.2f}</span>
                        </div>
                        <div class="context-body" style="font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.81rem;">{item['text']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        with t_reason:
            if notes:
                for n in notes:
                    st.markdown(f"- {n}")
            else:
                st.caption("No direct ontology class names were triggered in this query.")


def main():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None

    # ==================== SIDEBAR ====================
    with st.sidebar:
        st.markdown("### 🏗️ ApexBuild RAG")

        # Main view navigation in sidebar keeps the main screen clean and uncluttered
        view_mode = st.radio(
            "Navigation",
            options=["💬 AI Chat Assistant", "📄 PDF Documents (10)", "🧬 OWL Ontology (50)"],
            label_visibility="collapsed",
        )

        if st.button("✨ New Chat Conversation", use_container_width=True, type="primary"):
            st.session_state.messages = []
            st.session_state.pending_prompt = None
            st.session_state.pop("starter_pills_key", None)
            st.rerun()

        st.markdown("---")
        st.markdown("#### 🤖 Model & Generation")

        available_models = HybridOntologyRAG.get_available_ollama_models()
        default_idx = 0
        for i, m in enumerate(available_models):
            if "qwen2.5" in m.lower():
                default_idx = i
                break

        selected_model = st.selectbox(
            "Ollama Model",
            options=available_models,
            index=default_idx,
            help="Local LLM running via Ollama (http://localhost:11434)",
        )

        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.2,
            value=0.2,
            step=0.05,
            help="0.1–0.3 = strict factual answers from PDFs & OWL ontology; higher = more creative.",
        )

        num_ctx = st.select_slider(
            "Context Size (tokens)",
            options=[2048, 4096, 8192, 16384, 32768],
            value=8192,
            help="Ollama num_ctx parameter (context window size).",
        )

        st.markdown("#### 🔎 RAG Retrieval")
        use_ontology_expansion = st.toggle(
            "OWL Ontology Reasoning",
            value=True,
            help="Automatically expands queries with OWL superclasses, subclasses, and restrictions.",
        )

        col_k1, col_k2 = st.columns(2)
        with col_k1:
            top_k_pdf = st.number_input("PDF Chunks", min_value=1, max_value=10, value=5)
        with col_k2:
            top_k_owl = st.number_input("OWL Axioms", min_value=1, max_value=10, value=6)

        with st.expander("⚙️ Advanced Parameters"):
            num_predict = st.slider("Max Output Tokens", 256, 4096, 1024, step=128)
            top_p = st.slider("Top-P Sampling", 0.1, 1.0, 0.9, step=0.05)
            chunk_size = st.number_input("Chunk Size (chars)", 300, 2000, 850, step=50)
            chunk_overlap = st.number_input("Chunk Overlap (chars)", 0, 500, 150, step=25)
            system_prompt = st.text_area("System Prompt", value=DEFAULT_SYSTEM_PROMPT, height=150)
            if st.button("🔄 Rebuild Vector Index", use_container_width=True):
                st.cache_resource.clear()
                st.rerun()

        engine = get_rag_engine(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    # ==================== TOP BAR ====================
    st.markdown(
        f"""
        <div class="app-header">
            <div>
                <div class="app-header-title">🏗️ ApexBuild Construction Ontology RAG</div>
                <div class="app-header-sub">Hybrid Knowledge Graph (OWL) + Document Retrieval (10 PDFs) in English</div>
            </div>
            <div class="badge-row">
                <span class="status-badge">🤖 {selected_model}</span>
                <span class="status-badge">🌡️ Temp {temperature}</span>
                <span class="status-badge">📐 Ctx {num_ctx // 1024}k</span>
                <span class="status-badge">📚 10 PDFs · 50 OWL Classes</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ==================== VIEW 1: AI CHAT ASSISTANT ====================
    if view_mode == "💬 AI Chat Assistant":
        # Show a clean, centered welcome card + sleek horizontal pills when chat is empty
        welcome_placeholder = st.empty()
        if not st.session_state.messages:
            with welcome_placeholder.container():
                st.markdown(
                    """
                    <div style="text-align: center; padding: 2.2rem 1rem 1.2rem 1rem;">
                        <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🏗️</div>
                        <h3 style="margin: 0 0 0.4rem 0; font-weight: 700;">How can I help you with the Construction Ontology today?</h3>
                        <p style="opacity: 0.72; font-size: 0.92rem; max-width: 620px; margin: 0 auto;">
                            Ask any question in English about our OWL ontology classes, restrictions, projects, materials, suppliers, employees, or heavy machinery.
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                starter_map = {
                    "⚡ Electrician vs. Plumber": "What is the difference between Electrician and Plumber in the OWL ontology, and which employees hold these roles?",
                    "🏢 Eurovea Tower (2023)": "Tell me everything about EuroveaTower: its ontology classes, completion year, concrete specifications, cranes, budget, and site manager.",
                    "🏠 FamilyHouse & WoodenHouse": "What are the formal OWL restrictions for FamilyHouseExample (2026) and WoodenHouse, and why can't a WoodenHouse use Concrete?",
                    "🏛️ Famous Projects & Periods": "Compare EmpireStateBuilding and EuroveaTower in terms of their ProjectPeriod classification, year, and structural materials.",
                    "🚚 Suppliers & Materials": "Which approved suppliers provide Concrete, Steel, Brick, and Wood, and what are the SLA rules for delivering fresh Concrete?",
                    "🛠️ 4 Construction Phases": "Explain the four ConstructionPhase stages in the ontology and specify which roles, machines, and materials are used in each phase.",
                }

                selected_pill = st.pills(
                    "Suggested topics",
                    options=list(starter_map.keys()),
                    selection_mode="single",
                    label_visibility="collapsed",
                    key="starter_pills_key",
                )
                if selected_pill:
                    st.session_state.pending_prompt = starter_map[selected_pill]

        # Render existing chat messages
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg.get("meta"):
                    st.caption(msg["meta"])
                if msg.get("retrieval"):
                    render_sources_panel(msg["retrieval"])

        # Chat input at bottom
        typed_query = st.chat_input("Ask in English about projects, OWL classes, materials, employees, suppliers, or machines...")
        active_query = typed_query or st.session_state.pending_prompt
        if st.session_state.pending_prompt:
            st.session_state.pending_prompt = None

        if active_query:
            welcome_placeholder.empty()
            st.session_state.messages.append({"role": "user", "content": active_query})
            with st.chat_message("user"):
                st.markdown(active_query)

            with st.chat_message("assistant"):
                t0 = time.time()
                retrieval_res = engine.retrieve(
                    query=active_query,
                    top_k_pdf=int(top_k_pdf),
                    top_k_owl=int(top_k_owl),
                    use_ontology_expansion=use_ontology_expansion,
                )
                retrieval_ms = int((time.time() - t0) * 1000)

                prior_history = st.session_state.messages[:-1]
                llm_messages = engine.build_messages(
                    query=active_query,
                    retrieval_result=retrieval_res,
                    chat_history=prior_history,
                    system_prompt=system_prompt,
                )

                response_box = st.empty()
                full_response = ""
                t_gen = time.time()
                for token in engine.stream_ollama_chat(
                    messages=llm_messages,
                    model=selected_model,
                    temperature=temperature,
                    num_ctx=num_ctx,
                    top_p=top_p,
                    num_predict=num_predict,
                ):
                    full_response += token
                    response_box.markdown(full_response + "▌")

                gen_sec = time.time() - t_gen
                response_box.markdown(full_response)

                meta_line = (
                    f"⚡ Retrieved {len(retrieval_res['pdf_results'])} PDF chunks & "
                    f"{len(retrieval_res['owl_results'])} OWL axioms in {retrieval_ms} ms  ·  "
                    f"Generated in {gen_sec:.1f}s with `{selected_model}` (temp={temperature}, ctx={num_ctx})"
                )
                st.caption(meta_line)
                render_sources_panel(retrieval_res)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response,
                    "meta": meta_line,
                    "retrieval": retrieval_res,
                })

    # ==================== VIEW 2: PDF DOCUMENTS LIBRARY ====================
    elif view_mode == "📄 PDF Documents (10)":
        st.markdown("#### 📄 Knowledge Base: 10 English PDF Documents (`./PDF/`)")
        st.caption(
            f"All 10 documents ({sum(f['pages'] for f in engine.pdf_files_summary)} pages total) are automatically "
            f"chunked into {len(engine.pdf_chunks)} segments and tagged with OWL ontology classes."
        )

        selected_pdf = st.selectbox(
            "Choose a PDF document to read its content & ontology tags:",
            options=[f["filename"] for f in engine.pdf_files_summary],
        )

        file_info = next(f for f in engine.pdf_files_summary if f["filename"] == selected_pdf)
        c1, c2, c3 = st.columns(3)
        c1.metric("Pages", file_info["pages"])
        c2.metric("Indexed Chunks", file_info["chunks"])
        c3.metric("Characters", f"{file_info['chars']:,}")

        all_file_tags = "".join(f"<span class='onto-pill'>{c}</span>" for c in file_info["matched_classes"])
        st.markdown(f"**Linked OWL Ontology Classes:** &nbsp; {all_file_tags}", unsafe_allow_html=True)
        st.markdown("---")

        matching_chunks = [c for c in engine.pdf_chunks if c["source"] == selected_pdf]
        for c in matching_chunks:
            chunk_tags = "".join(f"<span class='onto-pill'>{cls}</span>" for cls in c["ontology_classes"])
            st.markdown(
                f"""
                <div class="context-card">
                    <div class="context-card-header">
                        <span>📑 {c['id']} &nbsp;·&nbsp; Page {c['page']} (Segment {c['chunk_index_on_page']})</span>
                    </div>
                    <div style="margin-bottom: 6px;">{chunk_tags}</div>
                    <div class="context-body">{c['text']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ==================== VIEW 3: OWL ONTOLOGY EXPLORER ====================
    elif view_mode == "🧬 OWL Ontology (50)":
        st.markdown("#### 🧬 OWL Ontology Explorer (`stavebna_firma_ontology - kópia.owl`)")
        col_search, col_type = st.columns([2, 1])
        with col_search:
            search_q = st.text_input("🔍 Filter classes or properties:", placeholder="Type e.g. Project, Worker, Concrete, Eurovea, usesMaterial...")
        with col_type:
            show_mode = st.selectbox("Show", ["Classes (50)", "Properties (12)"])

        if show_mode.startswith("Classes"):
            for cname, cinfo in sorted(engine.ontology.classes.items()):
                all_sups = engine.ontology.get_transitive_superclasses(cname)
                verb_text = cinfo.to_verbalized_text(all_superclasses=all_sups)
                if search_q and search_q.lower() not in verb_text.lower():
                    continue
                sups_str = ", ".join(cinfo.superclasses) if cinfo.superclasses else "owl:Thing"
                with st.expander(f"🧬 **{cname}**  —  subclass of `{sups_str}`"):
                    st.code(verb_text, language="yaml")
        else:
            for pname, pinfo in sorted(engine.ontology.properties.items()):
                verb_text = pinfo.to_verbalized_text()
                if search_q and search_q.lower() not in verb_text.lower():
                    continue
                with st.expander(f"🔗 **{pname}** (`{pinfo.prop_type}`)"):
                    st.code(verb_text, language="yaml")


if __name__ == "__main__":
    main()
