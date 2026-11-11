#!/usr/bin/env python3
"""
OWL Ontology Parser & Verbalizer for `stavebna_firma_ontology - kópia.owl`.

Parses classes, subclass hierarchies, object/datatype properties, domains/ranges,
inverse properties, existential/universal/value restrictions, numeric facet
restrictions, union/intersection equivalent classes, and disjointness axioms
directly from RDF/XML without requiring external dependencies.
"""

import os
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple

NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def local_name(uri: str) -> str:
    if not uri:
        return ""
    if "#" in uri:
        return uri.split("#")[-1]
    return uri.rstrip("/").split("/")[-1]


def camel_to_words(name: str) -> str:
    """Convert CamelCase identifier (e.g. 'ResidentialProject') to 'residential project'."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1 \2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s1).lower()


@dataclass
class OntologyClassInfo:
    name: str
    uri: str
    superclasses: List[str] = field(default_factory=list)
    subclasses: List[str] = field(default_factory=list)
    restrictions: List[str] = field(default_factory=list)
    equivalents: List[str] = field(default_factory=list)
    disjoints: List[str] = field(default_factory=list)
    related_terms: Set[str] = field(default_factory=set)

    def to_verbalized_text(self, all_superclasses: List[str] = None) -> str:
        lines = [f"OWL Ontology Class: {self.name} ({camel_to_words(self.name)})"]
        if self.superclasses:
            lines.append(f"- Direct Superclasses (rdfs:subClassOf): {', '.join(sorted(set(self.superclasses)))}")
        if all_superclasses and set(all_superclasses) != set(self.superclasses):
            lines.append(f"- Inherited Superclasses (Transitive): {', '.join(sorted(set(all_superclasses)))}")
        if self.subclasses:
            lines.append(f"- Direct Subclasses: {', '.join(sorted(set(self.subclasses)))}")
        if self.equivalents:
            for eq in sorted(set(self.equivalents)):
                lines.append(f"- Equivalent Class Definition (owl:equivalentClass): {eq}")
        if self.restrictions:
            for r in sorted(set(self.restrictions)):
                lines.append(f"- Formal OWL Restriction: {r}")
        if self.disjoints:
            lines.append(f"- Disjoint With (owl:disjointWith): {', '.join(sorted(set(self.disjoints)))}")
        return "\n".join(lines)


@dataclass
class OntologyPropertyInfo:
    name: str
    prop_type: str  # "ObjectProperty" or "DatatypeProperty"
    domains: List[str] = field(default_factory=list)
    ranges: List[str] = field(default_factory=list)
    sub_properties_of: List[str] = field(default_factory=list)
    inverse_of: List[str] = field(default_factory=list)

    def to_verbalized_text(self) -> str:
        lines = [f"OWL {self.prop_type}: {self.name} ({camel_to_words(self.name)})"]
        if self.domains:
            lines.append(f"- Domain (rdfs:domain): {', '.join(sorted(set(self.domains)))}")
        if self.ranges:
            lines.append(f"- Range (rdfs:range): {', '.join(sorted(set(self.ranges)))}")
        if self.sub_properties_of:
            lines.append(f"- SubProperty Of (rdfs:subPropertyOf): {', '.join(sorted(set(self.sub_properties_of)))}")
        if self.inverse_of:
            lines.append(f"- Inverse Property Of (owl:inverseOf): {', '.join(sorted(set(self.inverse_of)))}")
        return "\n".join(lines)


class ConstructionOntology:
    def __init__(self, owl_path: str):
        self.owl_path = owl_path
        self.classes: Dict[str, OntologyClassInfo] = {}
        self.properties: Dict[str, OntologyPropertyInfo] = {}
        self._parse()

    def _parse_datatype_restriction(self, dt_elem: ET.Element) -> str:
        on_dt = dt_elem.find("owl:onDatatype", NS)
        dt_name = local_name(on_dt.attrib.get(f"{{{NS['rdf']}}}resource", "integer")) if on_dt is not None else "integer"
        with_restr = dt_elem.find("owl:withRestrictions", NS)
        bounds = []
        if with_restr is not None:
            for desc in with_restr.findall("rdf:Description", NS):
                for child in desc:
                    tag_local = local_name(child.tag)
                    val = (child.text or "").strip()
                    if tag_local == "minInclusive":
                        bounds.append(f">= {val}")
                    elif tag_local == "maxExclusive":
                        bounds.append(f"< {val}")
                    elif tag_local == "maxInclusive":
                        bounds.append(f"<= {val}")
                    elif tag_local == "minExclusive":
                        bounds.append(f"> {val}")
        if bounds:
            return f"{dt_name}[{' and '.join(bounds)}]"
        return dt_name

    def _parse_restriction(self, restr_elem: ET.Element) -> Tuple[str, Set[str]]:
        """Return a human-readable restriction string and set of referenced entity names."""
        referenced = set()
        on_prop_elem = restr_elem.find("owl:onProperty", NS)
        prop_name = local_name(on_prop_elem.attrib.get(f"{{{NS['rdf']}}}resource", "")) if on_prop_elem is not None else "unknownProperty"
        if prop_name:
            referenced.add(prop_name)

        some_elem = restr_elem.find("owl:someValuesFrom", NS)
        all_elem = restr_elem.find("owl:allValuesFrom", NS)
        val_elem = restr_elem.find("owl:hasValue", NS)

        if some_elem is not None:
            res_attr = some_elem.attrib.get(f"{{{NS['rdf']}}}resource")
            if res_attr:
                target = local_name(res_attr)
                referenced.add(target)
                return f"{prop_name} some {target} (existential: must have at least one {target})", referenced
            dt_elem = some_elem.find("rdfs:Datatype", NS)
            if dt_elem is not None:
                dt_str = self._parse_datatype_restriction(dt_elem)
                return f"{prop_name} some {dt_str}", referenced

        if all_elem is not None:
            res_attr = all_elem.attrib.get(f"{{{NS['rdf']}}}resource")
            if res_attr:
                target = local_name(res_attr)
                referenced.add(target)
                return f"{prop_name} only {target} (universal owl:allValuesFrom: all values must be {target})", referenced

        if val_elem is not None:
            val_text = (val_elem.text or "").strip()
            return f"{prop_name} value {val_text} (exact value owl:hasValue = {val_text})", referenced

        return f"{prop_name} restriction", referenced

    def _parse(self):
        if not os.path.exists(self.owl_path):
            raise FileNotFoundError(f"OWL ontology file not found: {self.owl_path}")

        tree = ET.parse(self.owl_path)
        root = tree.getroot()

        # 1. Parse ObjectProperties and DatatypeProperties
        for prop_tag, prop_type in [("owl:ObjectProperty", "ObjectProperty"), ("owl:DatatypeProperty", "DatatypeProperty")]:
            for elem in root.findall(prop_tag, NS):
                uri = elem.attrib.get(f"{{{NS['rdf']}}}about", "")
                pname = local_name(uri)
                if not pname:
                    continue
                info = self.properties.setdefault(pname, OntologyPropertyInfo(name=pname, prop_type=prop_type))
                for dom in elem.findall("rdfs:domain", NS):
                    dname = local_name(dom.attrib.get(f"{{{NS['rdf']}}}resource", ""))
                    if dname:
                        info.domains.append(dname)
                for rng in elem.findall("rdfs:range", NS):
                    rname = local_name(rng.attrib.get(f"{{{NS['rdf']}}}resource", ""))
                    if rname:
                        info.ranges.append(rname)
                for subp in elem.findall("rdfs:subPropertyOf", NS):
                    spname = local_name(subp.attrib.get(f"{{{NS['rdf']}}}resource", ""))
                    if spname:
                        info.sub_properties_of.append(spname)
                for inv in elem.findall("owl:inverseOf", NS):
                    invname = local_name(inv.attrib.get(f"{{{NS['rdf']}}}resource", ""))
                    if invname:
                        info.inverse_of.append(invname)

        # Ensure symmetric inverseOf visibility
        for pname, pinfo in list(self.properties.items()):
            for inv in pinfo.inverse_of:
                if inv in self.properties and pname not in self.properties[inv].inverse_of:
                    self.properties[inv].inverse_of.append(pname)

        # 2. Parse Classes (note: a class URI may appear in multiple <owl:Class> blocks in the OWL file)
        for elem in root.findall("owl:Class", NS):
            uri = elem.attrib.get(f"{{{NS['rdf']}}}about", "")
            cname = local_name(uri)
            if not cname:
                continue
            cinfo = self.classes.setdefault(cname, OntologyClassInfo(name=cname, uri=uri))

            # rdfs:subClassOf (can be a direct resource or a nested owl:Restriction)
            for sub_elem in elem.findall("rdfs:subClassOf", NS):
                res_attr = sub_elem.attrib.get(f"{{{NS['rdf']}}}resource")
                if res_attr:
                    parent_name = local_name(res_attr)
                    if parent_name:
                        cinfo.superclasses.append(parent_name)
                        cinfo.related_terms.add(parent_name)
                        parent_info = self.classes.setdefault(parent_name, OntologyClassInfo(name=parent_name, uri=res_attr))
                        parent_info.subclasses.append(cname)
                        parent_info.related_terms.add(cname)
                else:
                    restr = sub_elem.find("owl:Restriction", NS)
                    if restr is not None:
                        r_text, refs = self._parse_restriction(restr)
                        cinfo.restrictions.append(r_text)
                        cinfo.related_terms.update(refs)

            # owl:disjointWith
            for disj_elem in elem.findall("owl:disjointWith", NS):
                d_uri = disj_elem.attrib.get(f"{{{NS['rdf']}}}resource", "")
                d_name = local_name(d_uri)
                if d_name:
                    cinfo.disjoints.append(d_name)
                    cinfo.related_terms.add(d_name)
                    d_info = self.classes.setdefault(d_name, OntologyClassInfo(name=d_name, uri=d_uri))
                    if cname not in d_info.disjoints:
                        d_info.disjoints.append(cname)
                    d_info.related_terms.add(cname)

            # owl:equivalentClass
            for eq_elem in elem.findall("owl:equivalentClass", NS):
                inner_cls = eq_elem.find("owl:Class", NS)
                if inner_cls is not None:
                    union_elem = inner_cls.find("owl:unionOf", NS)
                    if union_elem is not None:
                        members = []
                        for desc in union_elem.findall("rdf:Description", NS):
                            m_name = local_name(desc.attrib.get(f"{{{NS['rdf']}}}about", ""))
                            if m_name:
                                members.append(m_name)
                                cinfo.related_terms.add(m_name)
                                m_info = self.classes.setdefault(m_name, OntologyClassInfo(name=m_name, uri=""))
                                m_info.related_terms.add(cname)
                        if members:
                            cinfo.equivalents.append(f"Union of ({' OR '.join(members)})")

                    inter_elem = inner_cls.find("owl:intersectionOf", NS)
                    if inter_elem is not None:
                        parts = []
                        for restr in inter_elem.findall("owl:Restriction", NS):
                            r_text, refs = self._parse_restriction(restr)
                            parts.append(r_text)
                            cinfo.related_terms.update(refs)
                        if parts:
                            cinfo.equivalents.append(f"Intersection of ({' AND '.join(parts)})")

    def get_transitive_superclasses(self, class_name: str) -> List[str]:
        visited = []
        queue = list(self.classes.get(class_name, OntologyClassInfo(name=class_name, uri="")).superclasses)
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.append(curr)
                if curr in self.classes:
                    for sup in self.classes[curr].superclasses:
                        if sup not in visited:
                            queue.append(sup)
        return visited

    def get_transitive_subclasses(self, class_name: str) -> List[str]:
        visited = []
        queue = list(self.classes.get(class_name, OntologyClassInfo(name=class_name, uri="")).subclasses)
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.append(curr)
                if curr in self.classes:
                    for sub in self.classes[curr].subclasses:
                        if sub not in visited:
                            queue.append(sub)
        return visited

    def get_all_verbalized_chunks(self) -> List[Dict]:
        """Return structured chunks for every OWL class and property for indexing."""
        chunks = []
        for cname, cinfo in sorted(self.classes.items()):
            all_sups = self.get_transitive_superclasses(cname)
            all_subs = self.get_transitive_subclasses(cname)
            text = cinfo.to_verbalized_text(all_superclasses=all_sups)
            if all_subs and set(all_subs) != set(cinfo.subclasses):
                text += f"\n- All Transitive Subclasses: {', '.join(sorted(set(all_subs)))}"
            # Also include inherited restrictions from superclasses so each class chunk is self-contained
            inherited_restr = []
            for sup in all_sups:
                if sup in self.classes:
                    for r in self.classes[sup].restrictions:
                        inherited_restr.append(f"(Inherited from {sup}) {r}")
            if inherited_restr:
                text += "\n- Inherited Restrictions:\n  " + "\n  ".join(inherited_restr)

            chunks.append({
                "id": f"OWL_CLASS_{cname}",
                "source": "stavebna_firma_ontology - kópia.owl",
                "source_type": "ontology_class",
                "entity_name": cname,
                "page": 1,
                "text": text,
                "ontology_classes": sorted({cname} | set(all_sups) | set(cinfo.subclasses) | set(cinfo.related_terms)),
            })

        for pname, pinfo in sorted(self.properties.items()):
            text = pinfo.to_verbalized_text()
            chunks.append({
                "id": f"OWL_PROP_{pname}",
                "source": "stavebna_firma_ontology - kópia.owl",
                "source_type": "ontology_property",
                "entity_name": pname,
                "page": 1,
                "text": text,
                "ontology_classes": sorted(set(pinfo.domains) | set(pinfo.ranges) | {pname}),
            })
        return chunks

    def match_entities_in_text(self, text: str) -> List[str]:
        """Detect ontology class and property names mentioned in arbitrary English text."""
        text_lower = text.lower()
        matched = set()

        # Check class names & spaced versions
        for cname in self.classes:
            spaced = camel_to_words(cname)
            if cname.lower() in text_lower or spaced in text_lower:
                matched.add(cname)

        # Check property names & spaced versions
        for pname in self.properties:
            spaced = camel_to_words(pname)
            if pname.lower() in text_lower or spaced in text_lower:
                matched.add(pname)

        # Common English synonyms / plurals mapping to ontology classes
        synonym_map = {
            "company": "ConstructionCompany",
            "firm": "ConstructionCompany",
            "apexbuild": "ConstructionCompany",
            "client": "Customer",
            "clients": "Customer",
            "customers": "Customer",
            "staff": "Employee",
            "employees": "Employee",
            "worker": "ConstructionWorker",
            "workers": "ConstructionWorker",
            "manual worker": "ManualWorker",
            "electricians": "Electrician",
            "plumbers": "Plumber",
            "site manager": "SiteManager",
            "site managers": "SiteManager",
            "architects": "Architect",
            "designers": "Designer",
            "management": "ManagementRole",
            "suppliers": "Supplier",
            "vendor": "Supplier",
            "vendors": "Supplier",
            "procurement": "Supplier",
            "materials": "Material",
            "timber": "Wood",
            "wooden": "WoodenHouse",
            "clt": "Wood",
            "rebar": "Steel",
            "bricks": "Brick",
            "masonry": "Brick",
            "machinery": "ConstructionMachine",
            "machines": "ConstructionMachine",
            "equipment": "ConstructionMachine",
            "fleet": "ConstructionMachine",
            "excavators": "Excavator",
            "digger": "Excavator",
            "cranes": "Crane",
            "loaders": "Loader",
            "trucks": "Truck",
            "mixer": "Truck",
            "eurovea": "EuroveaTower",
            "skyscraper": "EuroveaTower",
            "empire state": "EmpireStateBuilding",
            "famous": "FamousProject",
            "villa": "FamilyHouseExample",
            "záhorie": "FamilyHouseExample",
            "zahorie": "FamilyHouseExample",
            "family house": "FamilyHouse",
            "family houses": "FamilyHouse",
            "apartments": "ApartmentBuilding",
            "residential": "ResidentialProject",
            "commercial": "CommercialProject",
            "office": "OfficeBuilding",
            "industrial": "IndustrialProject",
            "renovation": "Reconstruction",
            "reconstructions": "Reconstruction",
            "retrofit": "Reconstruction",
            "phases": "ConstructionPhase",
            "stages": "ConstructionPhase",
            "workflow": "ConstructionPhase",
            "historical": "HistoricalProject",
            "mid-century": "MidCenturyProject",
            "modern": "ModernProject",
            "future": "FutureProject",
            "2027": "FutureProject",
            "2026": "FamilyHouseExample",
            "2023": "EuroveaTower",
            "1931": "EmpireStateBuilding",
        }
        for kw, target in synonym_map.items():
            if kw in text_lower:
                matched.add(target)

        return sorted(matched)


if __name__ == "__main__":
    owl_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stavebna_firma_ontology - kópia.owl")
    onto = ConstructionOntology(owl_file)
    print(f"Loaded {len(onto.classes)} OWL classes and {len(onto.properties)} OWL properties.")
    chunks = onto.get_all_verbalized_chunks()
    print(f"Generated {len(chunks)} verbalized ontology chunks.")
    print("\nSample verbalized chunk (EuroveaTower):")
    print(onto.classes["EuroveaTower"].to_verbalized_text(onto.get_transitive_superclasses("EuroveaTower")))

