#!/usr/bin/env python3
"""
Generator of 10 comprehensive, domain-specific English PDF documents for the
Construction Company Ontology RAG system (ApexBuild Construction Corp.).

Each PDF document is 2-3 pages long, richly formatted with tables, sections,
technical specifications, project codes, financial figures, and explicit
alignment with the classes, object properties, datatype properties, and
OWL restrictions defined in `stavebna_firma_ontology - kópia.owl`.
"""

import os
import pymupdf

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "PDF")

CSS_STYLE = """
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.45;
    color: #1f2937;
}
h1 {
    font-size: 17pt;
    color: #0f172a;
    border-bottom: 2px solid #1d4ed8;
    padding-bottom: 6px;
    margin-top: 0px;
    margin-bottom: 10px;
}
h2 {
    font-size: 13pt;
    color: #1e3a8a;
    margin-top: 14px;
    margin-bottom: 6px;
}
h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 10px;
    margin-bottom: 4px;
}
p {
    margin-top: 4px;
    margin-bottom: 8px;
    text-align: justify;
}
ul, ol {
    margin-top: 4px;
    margin-bottom: 8px;
    padding-left: 18px;
}
li {
    margin-bottom: 4px;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 12px;
    font-size: 9.5pt;
}
th {
    background-color: #dbeafe;
    color: #1e3a8a;
    font-weight: bold;
    text-align: left;
    padding: 6px;
    border: 1px solid #93c5fd;
}
td {
    padding: 5px 6px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}
.meta-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    padding: 8px 10px;
    margin-bottom: 12px;
    font-size: 9.5pt;
}
.ontology-box {
    background-color: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 8px 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    font-size: 9.5pt;
}
code {
    font-family: Courier, monospace;
    font-size: 9.5pt;
    background-color: #f1f5f9;
    padding: 1px 3px;
}
"""

DOCUMENTS = [
    {
        "filename": "01_company_profile_and_organization.pdf",
        "doc_id": "DOC-01-CORP",
        "title": "ApexBuild Construction Corp. - Corporate Profile, Governance & Client Portfolio",
        "ontology_focus": "ConstructionCompany, Customer, Employee, ManagementRole, Project, hasCustomer, hasEmployee, hasProject, hasSiteManager, hasDesigner, name, year",
        "html": """
        <h1>1. Corporate Profile & Ontology Alignment: ApexBuild Construction Corp.</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-01-CORP | <b>Version:</b> 4.2 (2026) | <b>Classification:</b> Official Corporate Standard<br/>
            <b>Primary OWL Classes:</b> <code>ConstructionCompany</code>, <code>Customer</code>, <code>Employee</code>, <code>ManagementRole</code>, <code>Project</code><br/>
            <b>Primary OWL Properties:</b> <code>hasCustomer</code>, <code>hasEmployee</code>, <code>hasProject</code>, <code>hasSiteManager</code>, <code>hasDesigner</code>, <code>name</code>, <code>year</code>
        </div>

        <h2>1.1 Executive Overview of the Construction Company</h2>
        <p>
            <b>ApexBuild Construction Corp.</b> (represented in our formal domain ontology as an instance of class <code>ConstructionCompany</code>) is a Central European full-service civil engineering and general contracting enterprise founded in 1998 and headquartered in Bratislava, Slovakia, with regional operational hubs in Vienna and Prague. Under the formal axioms of the Construction Company Ontology, every valid <code>ConstructionCompany</code> must satisfy three existential restrictions simultaneously:
        </p>
        <ul>
            <li><code>hasCustomer some Customer</code>: The company maintains active contractual relationships with verified private, corporate, and municipal clients (class <code>Customer</code>).</li>
            <li><code>hasEmployee some Employee</code>: The company employs certified engineering, architectural, supervisory, and manual trade personnel (class <code>Employee</code>).</li>
            <li><code>hasProject some Project</code>: The company executes at least one active or completed construction project (class <code>Project</code>).</li>
        </ul>
        <p>
            Furthermore, in accordance with strict ontological disjointness rules, the class <code>ConstructionCompany</code> is mutually disjoint with <code>Person</code>, <code>Project</code>, <code>Material</code>, and <code>ConstructionMachine</code>. A legal corporate entity cannot simultaneously be classified as an individual person, a physical building project, a raw construction material, or a piece of heavy machinery.
        </p>

        <h2>1.2 Organizational Governance and Management Roles</h2>
        <p>
            Within ApexBuild Construction Corp., human resources are modeled under the top-level class <code>Person</code>, which carries the existential restriction <code>worksOn some Project</code>. Every employee of the firm belongs to the subclass <code>Employee</code> (which requires <code>hasProject some Project</code>). Specialized leadership and supervisory authority is formally grouped under the defined equivalent class <code>ManagementRole</code>:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axiom (Equivalent Class):</b><br/>
            <code>ManagementRole ≡ SiteManager ⊔ Architect</code> (The union of <code>SiteManager</code> and <code>Architect</code>).<br/>
            Only personnel classified as either a <code>SiteManager</code> or an <code>Architect</code> hold formal project sign-off authority, budget approval rights above EUR 250,000, and statutory responsibility on site.
        </div>
        <p>
            Notice how object property hierarchy reflects organizational reporting lines: both <code>hasSiteManager</code> (range: <code>SiteManager</code>) and <code>hasDesigner</code> (range: <code>Designer</code>) are defined in the OWL ontology as sub-properties of <code>hasEmployee</code> (<code>rdfs:subPropertyOf hasEmployee</code>). Consequently, whenever a <code>ConstructionCompany</code> or <code>BuildingProject</code> is linked via <code>hasSiteManager</code> to an individual such as Ing. Martin Kováč, an OWL reasoner automatically infers that the individual is also linked via <code>hasEmployee</code>.
        </p>

        <h2>1.3 Key Corporate Divisions and Financial Metrics (2023–2026)</h2>
        <table>
            <tr>
                <th>Division Name</th>
                <th>Target Ontology Project Class</th>
                <th>Division Lead (Role)</th>
                <th>Annual Turnover (EUR)</th>
                <th>Active Projects</th>
            </tr>
            <tr>
                <td><b>Residential Development Division</b></td>
                <td><code>ResidentialProject</code>, <code>FamilyHouse</code>, <code>ApartmentBuilding</code>, <code>WoodenHouse</code></td>
                <td>Ing. Elena Varga (<code>Designer</code>) &amp; Ing. Martin Kováč (<code>SiteManager</code>)</td>
                <td>€48,500,000</td>
                <td>14 projects</td>
            </tr>
            <tr>
                <td><b>Commercial &amp; High-Rise Division</b></td>
                <td><code>CommercialProject</code>, <code>OfficeBuilding</code>, <code>FamousProject</code></td>
                <td>Ing. arch. Richard Novák, PhD. (<code>Architect</code>)</td>
                <td>€72,300,000</td>
                <td>6 projects</td>
            </tr>
            <tr>
                <td><b>Industrial &amp; Logistics Division</b></td>
                <td><code>IndustrialProject</code>, <code>BuildingProject</code></td>
                <td>Ing. Peter Horváth (<code>SiteManager</code>)</td>
                <td>€54,100,000</td>
                <td>5 projects</td>
            </tr>
            <tr>
                <td><b>Heritage &amp; Reconstruction Division</b></td>
                <td><code>Reconstruction</code>, <code>HistoricalProject</code>, <code>MidCenturyProject</code></td>
                <td>Ing. Lukáš Beneš (<code>SiteManager</code>)</td>
                <td>€19,800,000</td>
                <td>8 projects</td>
            </tr>
        </table>

        <h2>1.4 Strategic Client Portfolio (Class: Customer)</h2>
        <p>
            In the ontology, a <code>Customer</code> is a subclass of <code>Person</code> (representing either a natural person or a legal client representative) that satisfies the restriction <code>hasProject some Project</code> and <code>worksOn some Project</code> (participating in project reviews and handover). Additionally, every <code>BuildingProject</code> must satisfy <code>hasCustomer some Customer</code>, and every <code>Architect</code> satisfies <code>hasCustomer some Customer</code> because architects directly interface with commercial clients during feasibility and permitting phases.
        </p>
        <table>
            <tr>
                <th>Customer ID</th>
                <th>Customer Name (<code>name</code>)</th>
                <th>Client Segment</th>
                <th>Contracted Projects (<code>hasProject</code>)</th>
                <th>Assigned Architect / Site Manager</th>
            </tr>
            <tr>
                <td>CUST-101</td>
                <td><b>J&amp;T Real Estate Development Rep. (Mgr. Daniel Kráľ)</b></td>
                <td>High-Rise Residential</td>
                <td><code>EuroveaTower</code> (Year: 2023, Budget: €115M)</td>
                <td>Ing. Martin Kováč (<code>SiteManager</code>)</td>
            </tr>
            <tr>
                <td>CUST-102</td>
                <td><b>Danube Business Parks Rep. (Ing. Klára Šimková)</b></td>
                <td>Commercial Office</td>
                <td>Danube Atrium <code>OfficeBuilding</code> (Year: 2024, Budget: €42M)</td>
                <td>Ing. arch. Richard Novák (<code>Architect</code>)</td>
            </tr>
            <tr>
                <td>CUST-103</td>
                <td><b>Dr. Tomáš Gregor &amp; Family</b></td>
                <td>Private Residential</td>
                <td><code>FamilyHouseExample</code> in Záhorská Bystrica (Year: 2026)</td>
                <td>Ing. Elena Varga (<code>Designer</code>)</td>
            </tr>
            <tr>
                <td>CUST-104</td>
                <td><b>Alpine EcoHomes Rep. (Bc. Marek Zeman)</b></td>
                <td>Sustainable Timber Housing</td>
                <td>Tatry CLT <code>WoodenHouse</code> Cluster (Year: 2025, Budget: €3.8M)</td>
                <td>Ing. Elena Varga (<code>Designer</code>)</td>
            </tr>
            <tr>
                <td>CUST-105</td>
                <td><b>Central European AutoLogistics Rep. (Ing. Robert Klein)</b></td>
                <td>Industrial Manufacturing</td>
                <td>Trnava Smart Hall (<code>IndustrialProject</code>, Year: 2025)</td>
                <td>Ing. Peter Horváth (<code>SiteManager</code>)</td>
            </tr>
        </table>

        <h2>1.5 Classification of Projects by Chronological Period (ProjectPeriod)</h2>
        <p>
            ApexBuild Construction Corp. categorizes all historical, current, and planned engineering works using the ontology class <code>ProjectPeriod</code> and the datatype property <code>year</code> (<code>xsd:integer</code>). Using OWL <code>equivalentClass</code> definitions with numeric facet restrictions, any entity with a <code>year</code> value is automatically classified into one of four temporal categories:
        </p>
        <ul>
            <li><b><code>HistoricalProject</code>:</b> Equivalent to any project with <code>year &lt; 1950</code> (<code>maxExclusive 1950</code>). Example: <code>EmpireStateBuilding</code> (<code>year = 1931</code>) studied as an architectural benchmark and heritage structural reference.</li>
            <li><b><code>MidCenturyProject</code>:</b> Equivalent to any project with <code>1950 &le; year &lt; 2000</code> (<code>minInclusive 1950</code> and <code>maxExclusive 2000</code>). Many of ApexBuild's current <code>Reconstruction</code> contracts target structures originally erected during this period.</li>
            <li><b><code>ModernProject</code>:</b> Equivalent to any project with <code>year &ge; 2000</code> (<code>minInclusive 2000</code>). Note that standard ontology classes <code>FamilyHouse</code>, <code>ApartmentBuilding</code>, <code>OfficeBuilding</code>, and <code>IndustrialProject</code> carry explicit restrictions requiring their completion/execution year to be at least 2000 (with standard catalog bounds <code>2000 &le; year &lt; 2026</code>, while specific 2026+ instances such as <code>FamilyHouseExample</code> extend into 2026).</li>
            <li><b><code>FutureProject</code>:</b> Equivalent to any project with <code>year &ge; 2027</code> (<code>minInclusive 2027</code>). This covers next-generation net-zero industrial complexes and hydrogen-ready commercial towers scheduled in the 2027–2030 pipeline.</li>
        </ul>
        """
    },
    {
        "filename": "02_employee_roles_and_safety_manual.pdf",
        "doc_id": "DOC-02-HR-HSE",
        "title": "Employee Roles, Competency Matrix & Occupational Health and Safety Manual",
        "ontology_focus": "Employee, SiteManager, Designer, Architect, ConstructionWorker, Electrician, Plumber, ManagementRole, ManualWorker, worksOn, belongsToProject, usesMaterial",
        "html": """
        <h1>2. Employee Roles, Competency Matrix &amp; Site Safety Manual</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-02-HR-HSE | <b>Version:</b> 5.0 (2026) | <b>Department:</b> Human Resources &amp; HSE<br/>
            <b>Primary OWL Classes:</b> <code>Employee</code>, <code>SiteManager</code>, <code>Designer</code>, <code>Architect</code>, <code>ConstructionWorker</code>, <code>Electrician</code>, <code>Plumber</code>, <code>ManagementRole</code>, <code>ManualWorker</code><br/>
            <b>Primary OWL Properties:</b> <code>worksOn</code>, <code>hasProject</code>, <code>hasEmployee</code>, <code>belongsToProject</code>, <code>usesMaterial</code>
        </div>

        <h2>2.1 Taxonomy of Employees in the Construction Ontology</h2>
        <p>
            Every staff member at ApexBuild Construction Corp. is an instance of <code>Employee</code>, which is a direct subclass of <code>Person</code>. In the OWL ontology, <code>Employee</code> inherits <code>worksOn some Project</code> from <code>Person</code> and adds the restriction <code>hasProject some Project</code>. Employees are divided into supervisory/design specialists and on-site manual execution staff:
        </p>
        <ul>
            <li><b><code>SiteManager</code> (Stavbyvedúci):</b> Subclass of <code>Employee</code> and member of <code>ManagementRole</code>. Must satisfy:
                <ul>
                    <li><code>hasEmployee some Employee</code> (a Site Manager supervises subordinate employees on site).</li>
                    <li><code>hasProject only Project</code> (<code>owl:allValuesFrom Project</code> – all projects managed by a Site Manager must be valid instances of <code>Project</code>).</li>
                    <li><code>worksOn some Project</code> (actively works on assigned construction projects).</li>
                </ul>
            </li>
            <li><b><code>Architect</code> (Architekt):</b> Subclass of <code>Employee</code> and member of <code>ManagementRole</code>. Must satisfy:
                <ul>
                    <li><code>hasProject some CommercialProject</code> (every Architect in our company is assigned to at least one commercial project, such as an <code>OfficeBuilding</code>).</li>
                    <li><code>hasCustomer some Customer</code> (directly consults with the project client).</li>
                    <li><code>worksOn some Project</code>.</li>
                </ul>
            </li>
            <li><b><code>Designer</code> (Projektant):</b> Subclass of <code>Employee</code>. Specializes in residential engineering and interior/structural layouts. Must satisfy:
                <ul>
                    <li><code>hasProject some ResidentialProject</code> (every Designer is responsible for at least one residential project, such as a <code>FamilyHouse</code> or <code>ApartmentBuilding</code>).</li>
                    <li><code>worksOn some Project</code>.</li>
                </ul>
            </li>
            <li><b><code>ConstructionWorker</code> (Stavebný robotník):</b> Subclass of <code>Employee</code> representing field personnel who execute physical works on site. Must satisfy:
                <ul>
                    <li><code>belongsToProject some Project</code> and <code>worksOn some Project</code>.</li>
                </ul>
            </li>
        </ul>

        <h2>2.2 Specialized Manual Workers (Electricians and Plumbers)</h2>
        <p>
            Within the class <code>ConstructionWorker</code>, the ontology defines two certified technical trades that together form the equivalent union class <code>ManualWorker</code>:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axiom (Equivalent Class):</b><br/>
            <code>ManualWorker ≡ Electrician ⊔ Plumber</code> (The union of <code>Electrician</code> and <code>Plumber</code>).
        </div>
        <ul>
            <li><b><code>Electrician</code> (Elektrikár):</b> Subclass of <code>ConstructionWorker</code>. Defined with three key existential restrictions:
                <ol>
                    <li><code>worksOn some BuildingProject</code> (Electricians work on broad building projects, including residential, commercial, and industrial buildings).</li>
                    <li><code>usesMaterial some Material</code> (handles electrical cabling, steel conduits, insulation materials).</li>
                    <li><code>worksOn some Project</code>.</li>
                </ol>
            </li>
            <li><b><code>Plumber</code> (Inštalatér / Vodár):</b> Subclass of <code>ConstructionWorker</code>. Defined with three existential restrictions:
                <ol>
                    <li><code>worksOn some ResidentialProject</code> (Plumbers at ApexBuild are specifically mandated to work on residential projects such as <code>FamilyHouse</code> and <code>ApartmentBuilding</code>).</li>
                    <li><code>usesMaterial some Material</code> (installs piping, thermal insulation, sanitary fixtures).</li>
                    <li><code>worksOn some Project</code>.</li>
                </ol>
            </li>
        </ul>
        <p>
            <b>Key Ontological Distinction between Electrician and Plumber:</b> While an <code>Electrician</code> has the restriction <code>worksOn some BuildingProject</code> (allowing assignment across commercial, industrial, and residential buildings), a <code>Plumber</code> has the stricter restriction <code>worksOn some ResidentialProject</code>. This distinction is frequently queried during HR compliance audits.
        </p>

        <h2>2.3 Directory of Key Personnel and Certifications</h2>
        <table>
            <tr>
                <th>Employee ID</th>
                <th>Full Name</th>
                <th>Ontology Class</th>
                <th>Group Classification</th>
                <th>Certifications &amp; Assigned Projects</th>
            </tr>
            <tr>
                <td>EMP-001</td>
                <td><b>Ing. Martin Kováč</b></td>
                <td><code>SiteManager</code></td>
                <td><code>ManagementRole</code></td>
                <td>SKSI License #4412 (Unlimited Height). Manages <code>EuroveaTower</code> and <code>FamilyHouseExample</code>. Supervises 45 employees.</td>
            </tr>
            <tr>
                <td>EMP-002</td>
                <td><b>Ing. Peter Horváth</b></td>
                <td><code>SiteManager</code></td>
                <td><code>ManagementRole</code></td>
                <td>SKSI License #5190 (Industrial Structures). Manages Trnava <code>IndustrialProject</code> and Bridge <code>Reconstruction</code>.</td>
            </tr>
            <tr>
                <td>EMP-003</td>
                <td><b>Ing. arch. Richard Novák, PhD.</b></td>
                <td><code>Architect</code></td>
                <td><code>ManagementRole</code></td>
                <td>SKA Authorized Architect #1088. Lead on Danube Atrium <code>OfficeBuilding</code> (<code>CommercialProject</code>); advises client CUST-102.</td>
            </tr>
            <tr>
                <td>EMP-004</td>
                <td><b>Ing. Elena Varga</b></td>
                <td><code>Designer</code></td>
                <td>Design Staff (<code>Employee</code>)</td>
                <td>Static &amp; Residential HVAC Specialist. Lead Designer for <code>FamilyHouseExample</code> and Tatry <code>WoodenHouse</code> (<code>ResidentialProject</code>).</td>
            </tr>
            <tr>
                <td>EMP-005</td>
                <td><b>Jozef Marek</b></td>
                <td><code>Electrician</code></td>
                <td><code>ManualWorker</code>, <code>ConstructionWorker</code></td>
                <td>Decree §23 High-Voltage Certification (up to 1000V). Works on <code>EuroveaTower</code> and Danube Atrium <code>BuildingProject</code>.</td>
            </tr>
            <tr>
                <td>EMP-006</td>
                <td><b>Milan Krátky</b></td>
                <td><code>Plumber</code></td>
                <td><code>ManualWorker</code>, <code>ConstructionWorker</code></td>
                <td>Certified Hydronic Heating &amp; Water Supply Installer. Works exclusively on <code>ResidentialProject</code> sites (<code>FamilyHouseExample</code>, <code>EuroveaTower</code>).</td>
            </tr>
            <tr>
                <td>EMP-007</td>
                <td><b>Štefan Baláž</b></td>
                <td><code>ConstructionWorker</code></td>
                <td>General Field Crew</td>
                <td>Reinforced Concrete Formwork &amp; Masonry Specialist. Assigned to <code>FamilyHouseExample</code> (2026) and <code>EuroveaTower</code>.</td>
            </tr>
        </table>

        <h2>2.4 Mandatory Occupational Health and Safety (HSE) Protocols</h2>
        <p>
            All personnel classified under <code>Employee</code> must adhere to ApexBuild HSE Directive 2026-04 when entering any active <code>Project</code> zone:
        </p>
        <ol>
            <li><b>Personal Protective Equipment (PPE):</b> Class EN 397 safety helmets, S3 steel-toe boots, and high-visibility vests are mandatory across all four construction phases (<code>Planning</code> site surveys, <code>Foundation</code>, <code>StructuralWork</code>, and <code>FinishingWork</code>).</li>
            <li><b>Site Manager Authority:</b> No <code>BuildingProject</code> may operate without an appointed <code>SiteManager</code> (enforced by the ontology axiom <code>BuildingProject ⊑ hasSiteManager some SiteManager</code>). If the Site Manager or their certified deputy is absent, crane lifting and deep excavation operations must halt immediately.</li>
            <li><b>Electrical &amp; Plumbing Lockout-Tagout (LOTO):</b> Every <code>Electrician</code> working on a <code>BuildingProject</code> must apply padlocked circuit breakers before handling distribution boards. Every <code>Plumber</code> working on a <code>ResidentialProject</code> must pressure-test manifolds at 1.5x operating pressure (minimum 9.0 bar) prior to concealing pipes under <code>Insulation</code> or <code>Concrete</code> screed.</li>
        </ol>
        """
    },
    {
        "filename": "03_residential_projects_catalog.pdf",
        "doc_id": "DOC-03-RES",
        "title": "Residential Projects Catalog: Family Houses, Wooden Houses & 2026 Model Specifications",
        "ontology_focus": "ResidentialProject, FamilyHouse, FamilyHouseExample, WoodenHouse, ModernProject, Concrete, Brick, Wood, Excavator, ConstructionWorker, year",
        "html": """
        <h1>3. Residential Projects Catalog: Family Houses &amp; Timber Structures</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-03-RES | <b>Version:</b> 3.4 (2026) | <b>Division:</b> Residential Development<br/>
            <b>Primary OWL Classes:</b> <code>ResidentialProject</code>, <code>FamilyHouse</code>, <code>FamilyHouseExample</code>, <code>WoodenHouse</code>, <code>ModernProject</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMaterial</code>, <code>usesMachine</code>, <code>hasEmployee</code>, <code>hasDesigner</code>, <code>hasSiteManager</code>, <code>year</code>
        </div>

        <h2>3.1 Ontological Definition of Residential Projects</h2>
        <p>
            In the ApexBuild ontology, <code>ResidentialProject</code> is a direct subclass of <code>BuildingProject</code> (which in turn is a subclass of <code>Project</code>). Consequently, every <code>ResidentialProject</code> inherits all structural requirements of a <code>BuildingProject</code>:
        </p>
        <ul>
            <li><code>usesMaterial some Material</code> (explicitly stated on both <code>BuildingProject</code> and <code>ResidentialProject</code>).</li>
            <li><code>usesMachine some ConstructionMachine</code> (inherited from <code>BuildingProject</code> and <code>Project</code>).</li>
            <li><code>hasCustomer some Customer</code> and <code>hasSiteManager some SiteManager</code> (inherited from <code>BuildingProject</code>).</li>
            <li>Connections to staff: Every <code>Designer</code> has restriction <code>hasProject some ResidentialProject</code>, and every <code>Plumber</code> has restriction <code>worksOn some ResidentialProject</code>.</li>
        </ul>
        <p>
            The class <code>ResidentialProject</code> branches into two main housing categories: <code>FamilyHouse</code> (single-family detached or semi-detached residences) and <code>ApartmentBuilding</code> (multi-unit residential complexes, covered in Document 04).
        </p>

        <h2>3.2 Standard Family House (Class: FamilyHouse)</h2>
        <p>
            A standard <code>FamilyHouse</code> in our ontology represents modern suburban residences built during the 21st century. Formally, <code>FamilyHouse</code> is a subclass of <code>ResidentialProject</code> with three class restrictions:
        </p>
        <ol>
            <li><b>Chronological Restriction:</b> <code>year some integer[&ge; 2000, &lt; 2026]</code> for standard historical catalog models (automatically making every such instance a <code>ModernProject</code>, since <code>ModernProject ≡ year &ge; 2000</code>).</li>
            <li><b>Machinery Requirement:</b> <code>usesMachine some ConstructionMachine</code>.</li>
            <li><b>Material Requirement:</b> <code>usesMaterial some Material</code>.</li>
        </ol>

        <h2>3.3 Detailed Specification: FamilyHouseExample (2026 Flagship Villa)</h2>
        <p>
            The ontology includes a dedicated flagship class <code>FamilyHouseExample</code> (subclass of <code>FamilyHouse</code>) representing our 2026 Model Villa "Vila Záhorie" constructed in Záhorská Bystrica for client Dr. Tomáš Gregor (CUST-103). This specific project is defined by five explicit OWL restrictions in <code>stavebna_firma_ontology - kópia.owl</code>:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Restrictions for <code>FamilyHouseExample</code>:</b>
            <ul>
                <li><code>rdfs:subClassOf FamilyHouse</code></li>
                <li><code>usesMaterial some Concrete</code> (C25/30 waterproof foundation slab and ceiling monoliths)</li>
                <li><code>usesMaterial some Brick</code> (Porotherm 38 Ti Profi precision ceramic thermal blocks)</li>
                <li><code>usesMachine some Excavator</code> (CAT 320 Hydraulic Crawler Excavator for foundation pit &amp; utility trenches)</li>
                <li><code>hasEmployee some ConstructionWorker</code> (On-site masonry and concrete crew led by Štefan Baláž)</li>
                <li><code>year value 2026</code> (<code>owl:hasValue 2026</code>)</li>
            </ul>
        </div>
        <table>
            <tr>
                <th>Parameter</th>
                <th>Specification for <code>FamilyHouseExample</code> ("Vila Záhorie 2026")</th>
            </tr>
            <tr>
                <td><b>Project Code &amp; Completion Year</b></td>
                <td>PRJ-RES-2026-01 | <code>year = 2026</code> (classified as <code>ModernProject</code>)</td>
            </tr>
            <tr>
                <td><b>Floor Area &amp; Storeys</b></td>
                <td>245 m² usable floor area | 2 storeys + underground technical basement</td>
            </tr>
            <tr>
                <td><b>Primary Structural Materials</b></td>
                <td><code>Concrete</code> (110 m³ of C25/30 XC2 for foundations &amp; slabs) and <code>Brick</code> (4,800 pcs ceramic blocks)</td>
            </tr>
            <tr>
                <td><b>Assigned Machinery</b></td>
                <td><code>Excavator</code> (CAT 320, Fleet ID: EXC-01) for 420 m³ earthworks</td>
            </tr>
            <tr>
                <td><b>Assigned Personnel</b></td>
                <td><code>SiteManager</code>: Ing. Martin Kováč | <code>Designer</code>: Ing. Elena Varga | <code>ConstructionWorker</code>: Štefan Baláž | <code>Plumber</code>: Milan Krátky</td>
            </tr>
            <tr>
                <td><b>Total Turnkey Budget</b></td>
                <td>EUR 485,000 (excl. VAT)</td>
            </tr>
        </table>

        <h2>3.4 Sustainable Timber Housing: Class WoodenHouse</h2>
        <p>
            For ecological construction, the ontology defines <code>WoodenHouse</code> as a specialized subclass of <code>FamilyHouse</code>. Unlike conventional masonry houses, <code>WoodenHouse</code> carries a universal (<code>owl:allValuesFrom</code>) material restriction:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axiom for <code>WoodenHouse</code>:</b><br/>
            <code>WoodenHouse ⊑ FamilyHouse</code> and <code>usesMaterial only Wood</code> (<code>owl:allValuesFrom Wood</code>).<br/>
            <i>Important Ontological Consequence:</i> Because <code>Concrete</code> is declared explicitly disjoint with <code>Wood</code> (<code>Concrete owl:disjointWith Wood</code>), a pure <code>WoodenHouse</code> instance in the ontology cannot have a <code>usesMaterial</code> assertion pointing to an instance of <code>Concrete</code> without triggering a logical inconsistency in an OWL DL reasoner!
        </div>
        <p>
            In practice, our <b>Tatry CLT WoodenHouse Cluster (PRJ-RES-2025-04)</b> utilizes Cross-Laminated Timber (CLT) spruce panels (class <code>Wood</code>, strength grade C24 / GL24h) mounted on screw-pile timber substructures, achieving passive-house thermal performance with a construction time of just 14 weeks per unit and a unit cost of EUR 310,000.
        </p>
        """
    },
    {
        "filename": "04_eurovea_tower_and_apartments.pdf",
        "doc_id": "DOC-04-APT",
        "title": "High-Rise Residential Case Study: Eurovea Tower (2023) & Apartment Buildings",
        "ontology_focus": "ApartmentBuilding, EuroveaTower, FamousProject, ResidentialProject, ModernProject, Concrete, Crane, Excavator, SiteManager, year",
        "html": """
        <h1>4. High-Rise Residential Case Study: Eurovea Tower &amp; Apartment Buildings</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-04-APT | <b>Version:</b> 2.8 (2026) | <b>Division:</b> Commercial &amp; High-Rise / Residential<br/>
            <b>Primary OWL Classes:</b> <code>ApartmentBuilding</code>, <code>EuroveaTower</code>, <code>FamousProject</code>, <code>ResidentialProject</code>, <code>ModernProject</code>, <code>Concrete</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMaterial</code>, <code>usesMachine</code>, <code>hasSiteManager</code>, <code>hasCustomer</code>, <code>year</code>
        </div>

        <h2>4.1 Multi-Unit Residential Engineering (Class: ApartmentBuilding)</h2>
        <p>
            In the Construction Company Ontology, <code>ApartmentBuilding</code> is a direct subclass of <code>ResidentialProject</code> (and therefore also a <code>BuildingProject</code> and <code>Project</code>). Standard catalog instances of <code>ApartmentBuilding</code> satisfy the following formal restrictions:
        </p>
        <ul>
            <li><code>year some integer[&ge; 2000, &lt; 2026]</code> (placing them in the <code>ModernProject</code> period).</li>
            <li><code>usesMachine some ConstructionMachine</code> (typically tower cranes, concrete pumps, and excavators).</li>
            <li><code>usesMaterial some Material</code> (primarily high-strength reinforced concrete, steel reinforcement, glass facades, and acoustic insulation).</li>
        </ul>

        <h2>4.2 Landmark Case Study: Eurovea Tower (Class: EuroveaTower)</h2>
        <p>
            <b>Eurovea Tower</b> in Bratislava is Slovakia's first skyscraper and the flagship residential reference project in our ontology. In <code>stavebna_firma_ontology - kópia.owl</code>, <code>EuroveaTower</code> is modeled with multiple inheritance and specific property restrictions:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axioms for <code>EuroveaTower</code>:</b>
            <ul>
                <li><code>rdfs:subClassOf FamousProject</code> (Categorized alongside iconic global landmarks)</li>
                <li><code>rdfs:subClassOf ApartmentBuilding</code> (Inherits all properties of <code>ResidentialProject</code> and <code>BuildingProject</code>)</li>
                <li><code>usesMaterial some Concrete</code> (Ultra-high-strength monolithic reinforced concrete core and slabs)</li>
                <li><code>year value 2023</code> (<code>owl:hasValue 2023</code>, which also entails classification as a <code>ModernProject</code> because <code>2023 &ge; 2000</code>)</li>
            </ul>
        </div>

        <h2>4.3 Technical &amp; Structural Parameters of Eurovea Tower</h2>
        <table>
            <tr>
                <th>Technical Parameter</th>
                <th>Engineering Specification (Eurovea Tower)</th>
            </tr>
            <tr>
                <td><b>Architectural Height &amp; Floors</b></td>
                <td>168 meters total height | 46 above-ground floors + 3 underground parking levels</td>
            </tr>
            <tr>
                <td><b>Completion Year (<code>year</code>)</b></td>
                <td><code>2023</code> (Ontology datatype restriction: <code>year = 2023</code>)</td>
            </tr>
            <tr>
                <td><b>Residential Capacity</b></td>
                <td>389 luxury apartments (studio to 5-bedroom penthouses), total floor area 52,400 m²</td>
            </tr>
            <tr>
                <td><b>Primary Structural Material</b></td>
                <td><code>Concrete</code>: 65,000 m³ of C50/60 and C60/75 high-performance concrete; foundation raft slab is 3.0 meters thick poured continuously over 54 hours</td>
            </tr>
            <tr>
                <td><b>Complementary Materials</b></td>
                <td><code>Steel</code> (9,200 tons of B500B reinforcing rebar), <code>Glass</code> (triple-glazed wind-resistant curtain wall units), <code>Insulation</code> (non-combustible mineral wool A1 fire rating)</td>
            </tr>
            <tr>
                <td><b>Heavy Machinery Deployed (<code>usesMachine</code>)</b></td>
                <td>3x Liebherr 280 EC-H self-climbing tower cranes (<code>Crane</code>), 4x CAT 336 hydraulic excavators (<code>Excavator</code>), 18x 8x4 concrete mixer trucks (<code>Truck</code>)</td>
            </tr>
            <tr>
                <td><b>Project Leadership &amp; Crew</b></td>
                <td><code>SiteManager</code>: Ing. Martin Kováč | <code>Electrician</code> Lead: Jozef Marek | <code>Plumber</code> Lead: Milan Krátky | Client (<code>Customer</code>): CUST-101</td>
            </tr>
            <tr>
                <td><b>Total Construction Cost</b></td>
                <td>EUR 115,000,000</td>
            </tr>
        </table>

        <h2>4.4 Construction Sequence &amp; Engineering Challenges on Eurovea Tower</h2>
        <p>
            Executing a 168-meter <code>ApartmentBuilding</code> beside the Danube River required specialized procedures across all four ontology <code>ConstructionPhase</code> stages:
        </p>
        <ol>
            <li><b><code>Planning</code> Phase:</b> Wind-tunnel aerodynamic modeling in Munich and 3D BIM clash detection for 389 residential plumbing and electrical risers.</li>
            <li><b><code>Foundation</code> Phase:</b> Secant pile retaining wall around the deep excavation pit to prevent Danube groundwater ingress, followed by drilling 180 large-diameter bored piles (1,200 mm diameter, 28 m depth) beneath the 3.0 m monolithic <code>Concrete</code> foundation mat.</li>
            <li><b><code>StructuralWork</code> Phase:</b> Self-climbing hydraulic formwork system advancing at a pace of one floor every 6 working days using high-early-strength <code>Concrete</code> delivered by Danucem (<code>Supplier</code>).</li>
            <li><b><code>FinishingWork</code> Phase:</b> Installation of unitized <code>Glass</code> facade elements, pressurized fire-escape stairwell ventilation, smart home electrical metering (by <code>Electrician</code> teams), and boosted multi-zone domestic water risers (by <code>Plumber</code> teams).</li>
        </ol>
        """
    },
    {
        "filename": "05_commercial_and_office_buildings.pdf",
        "doc_id": "DOC-05-COM",
        "title": "Commercial & Office Buildings: Architectural Standards & Empire State Building Benchmark",
        "ontology_focus": "CommercialProject, OfficeBuilding, EmpireStateBuilding, FamousProject, HistoricalProject, MidCenturyProject, ModernProject, Architect, Steel, Glass",
        "html": """
        <h1>5. Commercial &amp; Office Buildings: Standards &amp; Historical Benchmarks</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-05-COM | <b>Version:</b> 3.1 (2026) | <b>Division:</b> Commercial &amp; High-Rise<br/>
            <b>Primary OWL Classes:</b> <code>CommercialProject</code>, <code>OfficeBuilding</code>, <code>EmpireStateBuilding</code>, <code>FamousProject</code>, <code>HistoricalProject</code>, <code>Architect</code>, <code>Steel</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMaterial</code>, <code>usesMachine</code>, <code>hasProject</code>, <code>hasCustomer</code>, <code>year</code>
        </div>

        <h2>5.1 Ontological Structure of Commercial Projects</h2>
        <p>
            In `stavebna_firma_ontology - kópia.owl`, <code>CommercialProject</code> is a direct subclass of <code>BuildingProject</code>. It represents non-residential revenue-generating properties such as corporate headquarters, business centers, and retail complexes. Key ontological rules governing <code>CommercialProject</code> and its subclass <code>OfficeBuilding</code> include:
        </p>
        <ul>
            <li><b>Architect Assignment Rule:</b> The class <code>Architect</code> carries the existential restriction <code>hasProject some CommercialProject</code>. In our organizational model, every licensed Architect is mandated to lead the architectural design of at least one <code>CommercialProject</code> and maintain a direct relationship with a client (<code>hasCustomer some Customer</code>).</li>
            <li><b>Material &amp; Machinery Requirements:</b> Every <code>CommercialProject</code> and <code>OfficeBuilding</code> requires <code>usesMaterial some Material</code> and <code>usesMachine some ConstructionMachine</code>.</li>
            <li><b>Standard OfficeBuilding Temporal Restriction:</b> Modern catalog instances of <code>OfficeBuilding</code> have the restriction <code>year some integer[&ge; 2000, &lt; 2026]</code>, while historical benchmark subclasses can define specific historical years.</li>
        </ul>

        <h2>5.2 Famous Historical Benchmark: Empire State Building (1931)</h2>
        <p>
            Just as art ontologies include famous masterpieces to test temporal reasoning, our construction ontology includes <code>EmpireStateBuilding</code> as a canonical benchmark for structural steel high-rise engineering and temporal classification:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axioms for <code>EmpireStateBuilding</code>:</b>
            <ul>
                <li><code>rdfs:subClassOf FamousProject</code> (Shares the <code>FamousProject</code> superclass with <code>EuroveaTower</code>)</li>
                <li><code>rdfs:subClassOf OfficeBuilding</code> (And transitively a subclass of <code>CommercialProject</code>, <code>BuildingProject</code>, and <code>Project</code>)</li>
                <li><code>usesMaterial some Steel</code> (Constructed with a 57,000-ton structural steel frame)</li>
                <li><code>year value 1931</code> (<code>owl:hasValue 1931</code>)</li>
            </ul>
            <b>Automated Temporal Inference (<code>HistoricalProject</code>):</b> Because <code>HistoricalProject</code> is defined via an <code>owl:equivalentClass</code> restriction as any entity with <code>year &lt; 1950</code>, and <code>EmpireStateBuilding</code> has <code>year = 1931</code>, an OWL reasoner automatically classifies <code>EmpireStateBuilding</code> under <code>HistoricalProject</code> (a subclass of <code>ProjectPeriod</code>).
        </div>

        <h2>5.3 Comparison of Famous Projects in the Ontology</h2>
        <table>
            <tr>
                <th>Attribute</th>
                <th><code>EmpireStateBuilding</code></th>
                <th><code>EuroveaTower</code></th>
            </tr>
            <tr>
                <td><b>Superclasses</b></td>
                <td><code>FamousProject</code>, <code>OfficeBuilding</code> (<code>CommercialProject</code>)</td>
                <td><code>FamousProject</code>, <code>ApartmentBuilding</code> (<code>ResidentialProject</code>)</td>
            </tr>
            <tr>
                <td><b>Completion Year (<code>year</code>)</b></td>
                <td><code>1931</code></td>
                <td><code>2023</code></td>
            </tr>
            <tr>
                <td><b>Inferred <code>ProjectPeriod</code></b></td>
                <td><code>HistoricalProject</code> (<code>year &lt; 1950</code>)</td>
                <td><code>ModernProject</code> (<code>year &ge; 2000</code>)</td>
            </tr>
            <tr>
                <td><b>Primary Ontology Material</b></td>
                <td><code>usesMaterial some Steel</code> (riveted structural steel columns &amp; beams)</td>
                <td><code>usesMaterial some Concrete</code> (monolithic C60/75 reinforced concrete)</td>
            </tr>
            <tr>
                <td><b>Roof / Tip Height &amp; Floors</b></td>
                <td>381 m (443.2 m to spire) | 102 floors</td>
                <td>168 m | 46 floors</td>
            </tr>
        </table>

        <h2>5.4 Contemporary Office Projects by ApexBuild (2020–2025)</h2>
        <p>
            ApexBuild's Commercial Division, headed by <b>Ing. arch. Richard Novák, PhD.</b> (<code>Architect</code>) and supervised on site by <b>Ing. Martin Kováč</b> (<code>SiteManager</code>), delivers LEED Platinum certified <code>OfficeBuilding</code> complexes across Central Europe:
        </p>
        <ul>
            <li><b>Danube Atrium Business Center (PRJ-COM-2024-02, <code>year = 2024</code>):</b> 18-storey Class-A <code>OfficeBuilding</code> in Bratislava for client <i>Danube Business Parks</i> (CUST-102). Combines a composite <code>Steel</code>-and-<code>Concrete</code> structural core with a triple-glazed acoustic <code>Glass</code> curtain wall and mineral <code>Insulation</code>. Budget: EUR 42,000,000.</li>
            <li><b>CityGate Technopark (PRJ-COM-2022-05, <code>year = 2022</code>):</b> 12-storey flexible IT campus utilizing long-span castellated <code>Steel</code> beams (supplied by SteelCore Europe, <code>Supplier</code>) that eliminate interior columns across 1,800 m² floor plates. Deployed two tower cranes (<code>Crane</code>) and three wheeled loaders (<code>Loader</code>).</li>
        </ul>
        """
    },
    {
        "filename": "06_industrial_and_reconstruction_projects.pdf",
        "doc_id": "DOC-06-IND-REC",
        "title": "Industrial Facilities, Brownfield Reconstructions & 2027+ Future Pipeline",
        "ontology_focus": "IndustrialProject, Reconstruction, FutureProject, MidCenturyProject, ModernProject, ProjectPeriod, BuildingProject, Project, year",
        "html": """
        <h1>6. Industrial Facilities, Reconstructions &amp; Future Project Pipeline</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-06-IND-REC | <b>Version:</b> 2.5 (2026) | <b>Division:</b> Industrial &amp; Reconstruction<br/>
            <b>Primary OWL Classes:</b> <code>IndustrialProject</code>, <code>Reconstruction</code>, <code>FutureProject</code>, <code>MidCenturyProject</code>, <code>ModernProject</code>, <code>ProjectPeriod</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMaterial</code>, <code>usesMachine</code>, <code>hasSiteManager</code>, <code>year</code>
        </div>

        <h2>6.1 Industrial Projects (Class: IndustrialProject)</h2>
        <p>
            In the ontology, <code>IndustrialProject</code> is a direct subclass of <code>BuildingProject</code> alongside <code>ResidentialProject</code> and <code>CommercialProject</code>. It models manufacturing plants, automotive assembly halls, automated logistics warehouses, and energy infrastructure. Its formal OWL axioms are:
        </p>
        <ul>
            <li><code>rdfs:subClassOf BuildingProject</code> (inheriting <code>hasCustomer some Customer</code> and <code>hasSiteManager some SiteManager</code>).</li>
            <li><code>year some integer[&ge; 2000, &lt; 2026]</code> (standard completed industrial catalog projects fall in the <code>ModernProject</code> era).</li>
            <li><code>usesMachine some ConstructionMachine</code> and <code>usesMaterial some Material</code>.</li>
        </ul>
        <p>
            <b>Featured Project – Trnava Smart Logistics &amp; Assembly Hall (PRJ-IND-2025-01):</b> Completed in <code>year = 2025</code> under Site Manager <b>Ing. Peter Horváth</b> for client <i>Central European AutoLogistics</i> (CUST-105). The hall spans 38,000 m² with a clear internal height of 14.5 meters. It utilizes prefabricated prestressed <code>Concrete</code> columns, 32-meter <code>Steel</code> roof trusses, PIR thermal <code>Insulation</code> sandwich panels, and a fiber-reinforced heavy-duty <code>Concrete</code> floor slab rated for 80 kN/m² point loads. Total budget: EUR 29,400,000.
        </p>

        <h2>6.2 Reconstruction Projects (Class: Reconstruction)</h2>
        <p>
            A critical architectural feature of `stavebna_firma_ontology - kópia.owl` is how <code>Reconstruction</code> is positioned in the class hierarchy:
        </p>
        <div class="ontology-box">
            <b>Key Ontological Distinction (`Reconstruction` vs. `BuildingProject`):</b><br/>
            Whereas <code>ResidentialProject</code>, <code>CommercialProject</code>, and <code>IndustrialProject</code> are subclasses of <code>BuildingProject</code>, the class <b><code>Reconstruction</code> is a direct subclass of <code>Project</code></b> (<code>Reconstruction ⊑ Project</code>), sibling to <code>BuildingProject</code>!<br/>
            <code>Reconstruction</code> explicitly requires:
            <ul>
                <li><code>usesMachine some ConstructionMachine</code></li>
                <li><code>usesMaterial some Material</code></li>
            </ul>
            Because it is a direct subclass of <code>Project</code>, it can represent not only building renovations, but also civil infrastructure rehabilitations (bridges, tunnels, retaining walls, and industrial brownfields).
        </div>
        <p>
            Many of ApexBuild's reconstruction projects involve upgrading structures originally built during the <b><code>MidCenturyProject</code></b> period (defined by the ontology equivalence <code>1950 &le; year &lt; 2000</code>) or the <b><code>HistoricalProject</code></b> period (<code>year &lt; 1950</code>):
        </p>
        <table>
            <tr>
                <th>Project Code</th>
                <th>Project Name</th>
                <th>Original Year &amp; Period</th>
                <th>Scope of <code>Reconstruction</code> Works</th>
            </tr>
            <tr>
                <td>PRJ-REC-01</td>
                <td><b>Old Textile Mill Loft Conversion (Trenčín)</b></td>
                <td>Original: <code>1928</code> (<code>HistoricalProject</code>)</td>
                <td>Underpinning historical <code>Brick</code> masonry vaults with micro-piles, inserting a secondary self-supporting <code>Steel</code> frame, and adding triple-glazed <code>Glass</code> roof skylights.</td>
            </tr>
            <tr>
                <td>PRJ-REC-02</td>
                <td><b>Prievidza District Hospital Thermal Retrofit</b></td>
                <td>Original: <code>1974</code> (<code>MidCenturyProject</code>)</td>
                <td>Asbestos abatement, structural carbon-fiber strengthening of <code>Concrete</code> panels, 200 mm mineral wool facade <code>Insulation</code>, and complete electrical rewiring.</td>
            </tr>
        </table>

        <h2>6.3 Future Projects Pipeline: 2027 and Beyond (Class: FutureProject)</h2>
        <p>
            In the ontology, <code>FutureProject</code> is a subclass of <code>ProjectPeriod</code> defined via an <code>owl:equivalentClass</code> restriction as any project whose <code>year</code> property satisfies:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axiom for <code>FutureProject</code>:</b><br/>
            <code>FutureProject ≡ (year some integer[&ge; 2027])</code> (<code>xsd:minInclusive 2027</code>).
        </div>
        <p>
            ApexBuild Construction Corp. has already contracted three flagship projects scheduled for completion in 2027–2029, all classified under <code>FutureProject</code>:
        </p>
        <ol>
            <li><b>Košice GreenBattery Gigafactory Hall B (<code>year = 2027</code>):</b> A 65,000 m² clean-room industrial facility utilizing low-carbon geopolymer <code>Concrete</code> and recycled green <code>Steel</code> (Budget: EUR 94,000,000).</li>
            <li><b>Bratislava Port Eco-Tower (<code>year = 2028</code>):</b> A 32-storey hybrid timber-concrete commercial tower combining a <code>Concrete</code> core with structural cross-laminated <code>Wood</code> floors and photovoltaic <code>Glass</code> spandrels (Budget: EUR 68,000,000).</li>
            <li><b>Žilina Autonomous Rail Logistics Terminal (<code>year = 2029</code>):</b> Automated intermodal terminal featuring heavy-duty crane gantries and solar-heated warehouse slabs (Budget: EUR 41,500,000).</li>
        </ol>
        """
    },
    {
        "filename": "07_construction_materials_specification.pdf",
        "doc_id": "DOC-07-MAT",
        "title": "Construction Materials Specification, Eurocode Standards & Disjointness Rules",
        "ontology_focus": "Material, Concrete, Brick, Steel, Wood, Insulation, Glass, usesMaterial, suppliesMaterial, disjointWith",
        "html": """
        <h1>7. Construction Materials Catalog &amp; Engineering Standards</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-07-MAT | <b>Version:</b> 6.0 (2026) | <b>Department:</b> Structural Engineering &amp; QA/QC<br/>
            <b>Primary OWL Classes:</b> <code>Material</code>, <code>Concrete</code>, <code>Brick</code>, <code>Steel</code>, <code>Wood</code>, <code>Insulation</code>, <code>Glass</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMaterial</code>, <code>suppliesMaterial</code>, <code>owl:disjointWith</code>
        </div>

        <h2>7.1 Taxonomy of Construction Materials in the Ontology</h2>
        <p>
            The top-level class <code>Material</code> represents all physical construction materials consumed by a <code>Project</code> (via object property <code>usesMaterial</code>) or handled by specialized workers (`Electrician` and `Plumber` both satisfy <code>usesMaterial some Material</code>) and delivered by a <code>Supplier</code> (via object property <code>suppliesMaterial</code>). In `stavebna_firma_ontology - kópia.owl`, <code>Material</code> is disjoint with <code>ConstructionCompany</code>, <code>Person</code>, <code>Project</code>, <code>ConstructionMachine</code>, and <code>ConstructionPhase</code>.
        </p>
        <p>
            The ontology defines exactly <b>six direct subclasses of <code>Material</code></b>:
        </p>
        <ol>
            <li><b><code>Concrete</code> (Betón):</b> Structural ready-mix and precast concrete (EN 206).</li>
            <li><b><code>Brick</code> (Tehla):</b> Fired clay masonry blocks, acoustic bricks, and ceramic lintels (EN 771-1).</li>
            <li><b><code>Steel</code> (Oceľ):</b> Structural carbon steel profiles (S235, S355) and reinforcing rebar (B500B).</li>
            <li><b><code>Wood</code> (Drevo):</b> Structural solid timber (C24), glued laminated timber (Glulam GL24h/GL28h), and Cross-Laminated Timber (CLT).</li>
            <li><b><code>Insulation</code> (Izolácia):</b> Thermal, acoustic, and waterproofing materials (stone mineral wool, EPS/XPS, PIR boards).</li>
            <li><b><code>Glass</code> (Sklo):</b> Architectural float glass, tempered/laminated safety glazing, and triple-glazed curtain wall units.</li>
        </ol>

        <h2>7.2 Formal OWL Disjointness &amp; Restriction Rules on Materials</h2>
        <div class="ontology-box">
            <b>Critical Ontology Rules for <code>Concrete</code>:</b>
            <ul>
                <li><b>Disjointness Axiom 1:</b> <code>Concrete owl:disjointWith Wood</code> (No material instance can simultaneously be both <code>Concrete</code> and <code>Wood</code>).</li>
                <li><b>Disjointness Axiom 2:</b> <code>Concrete owl:disjointWith Glass</code> (No material instance can simultaneously be both <code>Concrete</code> and <code>Glass</code>).</li>
                <li><b>Supplier Restriction on Concrete:</b> <code>Concrete ⊑ suppliesMaterial some Supplier</code> (Every batch of <code>Concrete</code> in the ontology is linked to a certified <code>Supplier</code>).</li>
            </ul>
        </div>
        <p>
            <i>Why Material Disjointness Matters in Reasoning:</i> Consider the class <code>WoodenHouse</code>, which is restricted by <code>usesMaterial only Wood</code> (<code>owl:allValuesFrom Wood</code>). Because <code>Concrete</code> is disjoint with <code>Wood</code>, any project that uses <code>Concrete</code> (such as <code>EuroveaTower</code> or <code>FamilyHouseExample</code>) is mathematically proven by the OWL reasoner not to be a pure <code>WoodenHouse</code>.
        </p>

        <h2>7.3 Technical Specifications &amp; Project Usage Matrix</h2>
        <table>
            <tr>
                <th>Material Subclass</th>
                <th>Standard Grades Used by ApexBuild</th>
                <th>Key Physical Properties</th>
                <th>Explicitly Linked Projects / Classes in Ontology</th>
            </tr>
            <tr>
                <td><b><code>Concrete</code></b></td>
                <td>C25/30 XC2 (foundations), C35/45 (columns), C60/75 (high-rise cores)</td>
                <td>Compressive strength 30–75 MPa; density 2,400 kg/m³</td>
                <td><code>EuroveaTower</code> (<code>usesMaterial some Concrete</code>), <code>FamilyHouseExample</code> (<code>usesMaterial some Concrete</code>)</td>
            </tr>
            <tr>
                <td><b><code>Brick</code></b></td>
                <td>Porotherm 38 Ti Profi, Porotherm 30 AKU (acoustic)</td>
                <td>Thermal conductivity &lambda; = 0.079 W/(m·K); fire class A1</td>
                <td><code>FamilyHouseExample</code> (<code>usesMaterial some Brick</code>), historical masonry reconstructions</td>
            </tr>
            <tr>
                <td><b><code>Steel</code></b></td>
                <td>Structural profiles S355J2 (EN 10025); Rebar B500B (EN 10080)</td>
                <td>Yield strength 355–500 MPa; modulus of elasticity 210 GPa</td>
                <td><code>EmpireStateBuilding</code> (<code>usesMaterial some Steel</code>), commercial office frames, industrial trusses</td>
            </tr>
            <tr>
                <td><b><code>Wood</code></b></td>
                <td>Spruce C24, Glulam GL24h, 5-layer CLT panels</td>
                <td>Bending strength 24 MPa; density 420–480 kg/m³; renewable carbon sink</td>
                <td><code>WoodenHouse</code> (<code>usesMaterial only Wood</code>)</td>
            </tr>
            <tr>
                <td><b><code>Insulation</code></b></td>
                <td>Rockwool Frontrock MAX E (mineral wool), Austrotherm XPS TOP 30</td>
                <td>&lambda; = 0.035 W/(m·K); fire resistance class A1 (mineral wool)</td>
                <td>Used across all <code>ResidentialProject</code>, <code>CommercialProject</code>, and <code>FinishingWork</code> phases</td>
            </tr>
            <tr>
                <td><b><code>Glass</code></b></td>
                <td>Guardian SunGuard Triple IGU (44.2 / 16 Ar / 6 / 16 Ar / 44.2)</td>
                <td>U<sub>g</sub> = 0.5 W/(m²K); acoustic attenuation R<sub>w</sub> = 43 dB</td>
                <td>High-rise facades on <code>EuroveaTower</code> and modern <code>OfficeBuilding</code> curtain walls</td>
            </tr>
        </table>

        <h2>7.4 On-Site Quality Control &amp; Material Testing Protocols</h2>
        <p>
            Every delivery of <code>Material</code> to an ApexBuild <code>Project</code> undergoes mandatory inspection before incorporation into <code>Foundation</code>, <code>StructuralWork</code>, or <code>FinishingWork</code>:
        </p>
        <ul>
            <li><b><code>Concrete</code> Slump &amp; Cube Testing:</b> For every 50 m³ poured, site technicians cast three 150x150x150 mm test cubes for 7-day and 28-day destructive compression testing in an accredited laboratory.</li>
            <li><b><code>Steel</code> Mill Certificates &amp; Weld NDT:</b> All structural <code>Steel</code> requires an EN 10204 Type 3.1 inspection certificate. Load-bearing welds undergo 100% ultrasonic testing (UT).</li>
            <li><b><code>Wood</code> Moisture Verification:</b> CLT and Glulam timber elements delivered for a <code>WoodenHouse</code> must have a measured equilibrium moisture content of 12% &plusmn; 2% prior to assembly.</li>
        </ul>
        """
    },
    {
        "filename": "08_suppliers_and_procurement_policy.pdf",
        "doc_id": "DOC-08-SUP",
        "title": "Approved Suppliers Directory, Supply Chain Governance & Material Procurement",
        "ontology_focus": "Supplier, Person, Material, Concrete, Brick, Steel, Wood, Insulation, Glass, suppliesMaterial, worksOn",
        "html": """
        <h1>8. Approved Suppliers Directory &amp; Procurement Governance</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-08-SUP | <b>Version:</b> 4.1 (2026) | <b>Department:</b> Supply Chain &amp; Procurement<br/>
            <b>Primary OWL Classes:</b> <code>Supplier</code>, <code>Person</code>, <code>Material</code>, <code>Concrete</code>, <code>Brick</code>, <code>Steel</code>, <code>Wood</code>, <code>Insulation</code>, <code>Glass</code><br/>
            <b>Primary OWL Properties:</b> <code>suppliesMaterial</code>, <code>worksOn</code>
        </div>

        <h2>8.1 Modeling Suppliers in the Construction Company Ontology</h2>
        <p>
            In `stavebna_firma_ontology - kópia.owl`, a <code>Supplier</code> is modeled as a direct subclass of <code>Person</code> (representing an accredited supply partner or vendor liaison who collaborates on project logistics, thus inheriting <code>worksOn some Project</code> from <code>Person</code>). The class <code>Supplier</code> is governed by two formal OWL restrictions on the object property <code>suppliesMaterial</code>:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axioms for <code>Supplier</code> and <code>suppliesMaterial</code>:</b>
            <ul>
                <li><b>Domain &amp; Range:</b> <code>suppliesMaterial</code> has domain <code>Supplier</code> and range <code>Material</code>.</li>
                <li><b>Existential Restriction (<code>owl:someValuesFrom</code>):</b> <code>Supplier ⊑ suppliesMaterial some Material</code> (Every supplier must supply at least one construction material).</li>
                <li><b>Universal Restriction (<code>owl:allValuesFrom</code>):</b> <code>Supplier ⊑ suppliesMaterial only Material</code> (Everything supplied via <code>suppliesMaterial</code> by a <code>Supplier</code> must belong to the class <code>Material</code>—a supplier under this property cannot supply non-material entities such as employees).</li>
                <li><b>Concrete Specific Restriction:</b> The class <code>Concrete</code> additionally specifies a restriction linking `Concrete` and `Supplier` via `suppliesMaterial`, ensuring full supply-chain traceability for all structural concrete batches.</li>
            </ul>
        </div>

        <h2>8.2 Master Directory of Approved Suppliers (2026)</h2>
        <p>
            ApexBuild Construction Corp. procures materials exclusively from six ISO 9001 and ISO 14001 certified supply partners, covering all six subclasses of <code>Material</code>:
        </p>
        <table>
            <tr>
                <th>Supplier ID</th>
                <th>Supplier Name &amp; Liaison (<code>Supplier</code>)</th>
                <th>Supplied Ontology Material Class (<code>suppliesMaterial</code>)</th>
                <th>Lead Time &amp; Logistics Capacity</th>
                <th>Key Projects Supplied</th>
            </tr>
            <tr>
                <td>SUP-01</td>
                <td><b>Danucem ReadyMix Slovakia (Ing. Marek Holub)</b></td>
                <td><code>Concrete</code> (C25/30 up to C60/75, waterproof &amp; sulfate-resistant mixes)</td>
                <td>Just-in-Time (JIT) within 45 mins from 3 batching plants (up to 180 m³/hour)</td>
                <td><code>EuroveaTower</code>, <code>FamilyHouseExample</code>, Danube Atrium <code>OfficeBuilding</code></td>
            </tr>
            <tr>
                <td>SUP-02</td>
                <td><b>Wienerberger Ceramic Systems (Ing. Zuzana Krížová)</b></td>
                <td><code>Brick</code> (Porotherm thermal blocks, acoustic bricks, ceramic ceiling beams)</td>
                <td>3–5 business days via flatbed <code>Truck</code> fleet</td>
                <td><code>FamilyHouseExample</code>, Trenčín Heritage <code>Reconstruction</code></td>
            </tr>
            <tr>
                <td>SUP-03</td>
                <td><b>SteelCore Europe / U.S. Steel Partner (Ing. Dávid Urban)</b></td>
                <td><code>Steel</code> (S355 structural H-beams, castellated beams, B500B rebar coils)</td>
                <td>14 days for standard profiles; 28 days for custom pre-cambered trusses</td>
                <td>Danube Atrium <code>OfficeBuilding</code>, Trnava <code>IndustrialProject</code>, <code>EuroveaTower</code></td>
            </tr>
            <tr>
                <td>SUP-04</td>
                <td><b>Carpathian Timber &amp; CLT Works (Ing. Lukáš Oravec)</b></td>
                <td><code>Wood</code> (FSC-certified C24 spruce, Glulam GL24h arches, 5-ply CLT panels)</td>
                <td>21 days CNC pre-cut delivery directly to site</td>
                <td>Tatry CLT <code>WoodenHouse</code> Cluster, Bratislava Port Eco-Tower (<code>FutureProject</code>)</td>
            </tr>
            <tr>
                <td>SUP-05</td>
                <td><b>IsoTherm Central Europe (Mgr. Petra Horská)</b></td>
                <td><code>Insulation</code> (Rockwool A1 facade stone wool, XPS perimeter boards, PIR roof panels)</td>
                <td>48 hours from regional warehouse in Senec</td>
                <td>All <code>ResidentialProject</code>, <code>CommercialProject</code>, and Hospital <code>Reconstruction</code></td>
            </tr>
            <tr>
                <td>SUP-06</td>
                <td><b>Glaverbel Architectural Glazing (Ing. FilipBartoš)</b></td>
                <td><code>Glass</code> (Triple-glazed curtain wall units, laminated safety glass, solar-control IGU)</td>
                <td>4–6 weeks custom fabrication per facade grid elevation</td>
                <td><code>EuroveaTower</code>, Danube Atrium <code>OfficeBuilding</code></td>
            </tr>
        </table>

        <h2>8.3 Procurement SLA, Traceability &amp; Penalty Clauses</h2>
        <ol>
            <li><b>Digital Batch Traceability:</b> Every delivery note from a <code>Supplier</code> must contain the target <code>Project</code> ID, the ontology <code>Material</code> subclass code, and the assigned <code>SiteManager</code> signature upon unloading.</li>
            <li><b>Concrete Window SLA:</b> Because fresh <code>Concrete</code> begins hydration immediately upon mixing, supplier SUP-01 (Danucem) guarantees delivery to the project site within 60 minutes of batching. Any mixer <code>Truck</code> exceeding 90 minutes from batching time is rejected at the gate by the <code>SiteManager</code>.</li>
            <li><b>Sustainability &amp; EPD Mandate:</b> Starting in 2026, all suppliers of <code>Concrete</code>, <code>Steel</code>, and <code>Wood</code> must provide Type III Environmental Product Declarations (EPD) compliant with EN 15804.</li>
        </ol>
        """
    },
    {
        "filename": "09_heavy_machinery_fleet_and_operations.pdf",
        "doc_id": "DOC-09-MACH",
        "title": "Heavy Construction Machinery Fleet, Inverse Property Rules & Site Operations",
        "ontology_focus": "ConstructionMachine, Excavator, Crane, Loader, Truck, usesMachine, belongsToProject, Project, FamilyHouseExample",
        "html": """
        <h1>9. Heavy Machinery Fleet &amp; Site Equipment Operations</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-09-MACH | <b>Version:</b> 3.7 (2026) | <b>Department:</b> Plant &amp; Fleet Management<br/>
            <b>Primary OWL Classes:</b> <code>ConstructionMachine</code>, <code>Excavator</code>, <code>Crane</code>, <code>Loader</code>, <code>Truck</code>, <code>Project</code><br/>
            <b>Primary OWL Properties:</b> <code>usesMachine</code>, <code>belongsToProject</code> (<code>owl:inverseOf usesMachine</code>)
        </div>

        <h2>9.1 Ontological Modeling of Construction Machinery</h2>
        <p>
            In `stavebna_firma_ontology - kópia.owl`, all motorized heavy equipment and site vehicles are represented under the class <code>ConstructionMachine</code>. The ontology enforces strong bidirectional semantics between projects and machinery:
        </p>
        <div class="ontology-box">
            <b>Formal OWL Axioms for <code>ConstructionMachine</code> and Inverse Properties:</b>
            <ul>
                <li><b>Universal Project Requirement:</b> Every <code>Project</code> (and specifically <code>BuildingProject</code>, <code>FamilyHouse</code>, <code>ApartmentBuilding</code>, <code>OfficeBuilding</code>, <code>IndustrialProject</code>, and <code>Reconstruction</code>) satisfies the restriction <code>usesMachine some ConstructionMachine</code>.</li>
                <li><b>Universal Machine Assignment:</b> Every <code>ConstructionMachine</code> satisfies the restriction <code>belongsToProject some Project</code>.</li>
                <li><b>Inverse Property Axiom (<code>owl:inverseOf</code>):</b> The object property <code>belongsToProject</code> (domain: <code>ConstructionMachine</code>, range: <code>Project</code>) is formally declared as the inverse of <code>usesMachine</code> (domain: <code>Project</code>, range: <code>ConstructionMachine</code>). Therefore, if <code>FamilyHouseExample usesMachine EXC_01</code>, an OWL reasoner automatically infers <code>EXC_01 belongsToProject FamilyHouseExample</code>!</li>
                <li><b>Disjointness:</b> <code>ConstructionMachine</code> is disjoint with <code>ConstructionCompany</code>, <code>Person</code>, <code>Project</code>, <code>Material</code>, and <code>ConstructionPhase</code>.</li>
            </ul>
        </div>

        <h2>9.2 The Four Subclasses of ConstructionMachine</h2>
        <p>
            The ontology classifies all heavy equipment into four specialized subclasses of <code>ConstructionMachine</code>:
        </p>
        <ol>
            <li><b><code>Excavator</code> (Bager / Rýpadlo):</b> Tracked and wheeled hydraulic excavators used for earthmoving, trenching, foundation pit excavation, and demolition. Explicitly required by the ontology class <code>FamilyHouseExample</code> (<code>usesMachine some Excavator</code>).</li>
            <li><b><code>Crane</code> (Žeriav):</b> Self-climbing tower cranes, saddle-jib tower cranes, and mobile telescopic all-terrain cranes used for vertical and horizontal lifting of <code>Steel</code>, formwork, precast <code>Concrete</code>, and <code>Glass</code> facade panels during <code>StructuralWork</code>.</li>
            <li><b><code>Loader</code> (Nakladač):</b> Articulated front-end wheel loaders, skid-steer loaders, and backhoe loaders used for aggregate handling, site grading, backfilling, and pallet transport.</li>
            <li><b><code>Truck</code> (Nákladné auto / Domiešavač):</b> Heavy 8x4 tipper dump trucks, flatbed material haulers, and transit concrete mixer trucks used to transport excavated soil and deliver bulk <code>Material</code>.</li>
        </ol>

        <h2>9.3 ApexBuild Active Machinery Fleet Register (2026)</h2>
        <table>
            <tr>
                <th>Fleet ID</th>
                <th>Ontology Subclass</th>
                <th>Make &amp; Model</th>
                <th>Key Technical Specifications</th>
                <th>Assigned Project (<code>belongsToProject</code>)</th>
                <th>Internal Daily Rate</th>
            </tr>
            <tr>
                <td><b>EXC-01</b></td>
                <td><code>Excavator</code></td>
                <td>Caterpillar 320 NextGen Crawler</td>
                <td>Operating weight: 22.5 t | Bucket: 1.19 m³ | Max digging depth: 6.72 m | Engine: 121 kW Stage V</td>
                <td><code>FamilyHouseExample</code> (Záhorská Bystrica, 2026)</td>
                <td>€680 / day</td>
            </tr>
            <tr>
                <td><b>EXC-02</b></td>
                <td><code>Excavator</code></td>
                <td>Liebherr R 938 Litronic</td>
                <td>Operating weight: 38.4 t | Heavy rock bucket: 2.2 m³ | Deep excavation configuration</td>
                <td><code>EuroveaTower</code> &amp; Danube Atrium <code>OfficeBuilding</code></td>
                <td>€950 / day</td>
            </tr>
            <tr>
                <td><b>CRN-01</b></td>
                <td><code>Crane</code></td>
                <td>Liebherr 280 EC-H 12 Litronic</td>
                <td>Max lifting capacity: 12,000 kg | Jib radius: 70 m | Free-standing/climbing height: up to 185 m</td>
                <td><code>EuroveaTower</code> (High-rise core &amp; facade lifting)</td>
                <td>€1,450 / day</td>
            </tr>
            <tr>
                <td><b>CRN-02</b></td>
                <td><code>Crane</code></td>
                <td>Potain MDT 219 J10 Tower Crane</td>
                <td>Max capacity: 10,000 kg | Jib length: 65 m | Anti-collision radar system installed</td>
                <td>Danube Atrium <code>OfficeBuilding</code> &amp; Trnava <code>IndustrialProject</code></td>
                <td>€1,100 / day</td>
            </tr>
            <tr>
                <td><b>LDR-01</b></td>
                <td><code>Loader</code></td>
                <td>Volvo L120H Wheel Loader</td>
                <td>Operating weight: 20.7 t | Bucket capacity: 3.8 m³ | Static tipping load: 14,500 kg</td>
                <td>Trnava <code>IndustrialProject</code> &amp; Hospital <code>Reconstruction</code></td>
                <td>€540 / day</td>
            </tr>
            <tr>
                <td><b>TRK-01</b></td>
                <td><code>Truck</code></td>
                <td>Mercedes-Benz Arocs 4145 8x4 Tipper / Mixer</td>
                <td>Gross vehicle weight: 41 t | 330 kW Euro 6d | 9 m³ Liebherr drum / 18 m³ heated steel dump body</td>
                <td>Shared across <code>EuroveaTower</code>, <code>FamilyHouseExample</code> &amp; <code>Reconstruction</code></td>
                <td>€490 / day</td>
            </tr>
        </table>

        <h2>9.4 Machinery Maintenance &amp; Wind-Speed Safety Thresholds</h2>
        <ul>
            <li><b>Tower Crane Wind Cut-Off:</b> All <code>Crane</code> units (CRN-01, CRN-02) are equipped with ultrasonic anemometers. Lifting of large-surface <code>Glass</code> panels or <code>Wood</code> CLT walls must cease when gusts exceed 13.8 m/s (50 km/h). At 20 m/s (72 km/h), all tower cranes must be placed in free-slewing weathervane mode under the supervision of the <code>SiteManager</code>.</li>
            <li><b>Excavator Underground Utility Clearance:</b> Before any <code>Excavator</code> begins digging in the <code>Foundation</code> phase, the <code>SiteManager</code> must issue a signed Permit-to-Dig confirming ground-penetrating radar (GPR) clearance of gas, water, and high-voltage cables.</li>
        </ul>
        """
    },
    {
        "filename": "10_construction_phases_and_workflows.pdf",
        "doc_id": "DOC-10-PHASE",
        "title": "Standard Construction Phases, Workflows & Quality Gate Checklists",
        "ontology_focus": "ConstructionPhase, Planning, Foundation, StructuralWork, FinishingWork, SiteManager, Architect, Designer, Electrician, Plumber",
        "html": """
        <h1>10. Construction Phases, Standard Workflows &amp; Quality Gates</h1>
        <div class="meta-box">
            <b>Document ID:</b> DOC-10-PHASE | <b>Version:</b> 5.2 (2026) | <b>Department:</b> Project Management Office (PMO)<br/>
            <b>Primary OWL Classes:</b> <code>ConstructionPhase</code>, <code>Planning</code>, <code>Foundation</code>, <code>StructuralWork</code>, <code>FinishingWork</code><br/>
            <b>Related OWL Classes:</b> <code>Project</code>, <code>Material</code>, <code>ConstructionMachine</code>, <code>ManagementRole</code>, <code>ManualWorker</code>
        </div>

        <h2>10.1 Ontological Representation of Construction Phases</h2>
        <p>
            In `stavebna_firma_ontology - kópia.owl`, the lifecycle of every engineering project is structured under the top-level class <code>ConstructionPhase</code>. To preserve strict conceptual separation, <code>ConstructionPhase</code> is declared formally disjoint with both <code>Material</code> and <code>ConstructionMachine</code> (<code>ConstructionPhase owl:disjointWith Material</code> and <code>ConstructionPhase owl:disjointWith ConstructionMachine</code>).
        </p>
        <p>
            The class <code>ConstructionPhase</code> is divided into four sequential subclasses representing the complete execution workflow of a project:
        </p>
        <ol>
            <li><b>Stage 1: <code>Planning</code> (Príprava a projektovanie)</b></li>
            <li><b>Stage 2: <code>Foundation</code> (Zakladanie stavby)</b></li>
            <li><b>Stage 3: <code>StructuralWork</code> (Hrubá stavba)</b></li>
            <li><b>Stage 4: <code>FinishingWork</code> (Dokončovacie práce a odovzdanie)</b></li>
        </ol>

        <h2>10.2 Detailed Breakdown of the Four Construction Phases</h2>

        <h3>Phase 1: Planning (Class: <code>Planning</code>)</h3>
        <p>
            The <code>Planning</code> phase encompasses architectural feasibility, structural statics, BIM modeling, hydrogeological surveys, and building permit acquisition.
        </p>
        <ul>
            <li><b>Key Responsible Roles:</b> <code>Architect</code> (leads commercial planning and client consultations with <code>Customer</code>), <code>Designer</code> (leads residential engineering for <code>ResidentialProject</code>), and <code>SiteManager</code> (prepares the Site Mobilization &amp; HSE Plan).</li>
            <li><b>Deliverables:</b> Approved Building Permit, 4D BIM Execution Plan, Bill of Quantities (BoQ) for all <code>Material</code> subclasses, and signed procurement schedules with each <code>Supplier</code>.</li>
            <li><b>Typical Duration &amp; Cost Share:</b> 15–20% of total timeline | 6–8% of total project budget.</li>
        </ul>

        <h3>Phase 2: Foundation (Class: <code>Foundation</code>)</h3>
        <p>
            The <code>Foundation</code> phase transfers the building's design loads safely into the load-bearing subsoil.
        </p>
        <ul>
            <li><b>Key Responsible Roles:</b> <code>SiteManager</code> (geodetic layout and concrete pour sign-off) and <code>ConstructionWorker</code> crews.</li>
            <li><b>Primary Machinery Deployed:</b> <code>Excavator</code> (topsoil stripping, deep excavation pits, utility trenches), <code>Loader</code> (gravel sub-base compaction), and <code>Truck</code> (soil haulage and transit concrete delivery).</li>
            <li><b>Primary Materials Consumed:</b> Waterproof <code>Concrete</code> (C25/30 XC2 to C35/45), B500B reinforcing <code>Steel</code> cages, and perimeter XPS <code>Insulation</code>.</li>
            <li><b>Typical Duration &amp; Cost Share:</b> 15–20% of total timeline | 12–18% of total project budget.</li>
        </ul>

        <h3>Phase 3: StructuralWork (Class: <code>StructuralWork</code>)</h3>
        <p>
            The <code>StructuralWork</code> phase erects the primary load-bearing skeleton, floors, roof structure, and external envelope (shell and core).
        </p>
        <ul>
            <li><b>Key Responsible Roles:</b> <code>SiteManager</code>, <code>ConstructionWorker</code> (formwork carpenters, ironworkers, masons, timber assemblers), and structural <code>Architect</code> / <code>Designer</code> for stage inspections.</li>
            <li><b>Primary Machinery Deployed:</b> <code>Crane</code> (tower cranes lifting rebar, formwork, steel beams, and CLT panels) and <code>Truck</code>.</li>
            <li><b>Primary Materials Consumed:</b>
                <ul>
                    <li>On <code>EuroveaTower</code> (<code>ApartmentBuilding</code>): High-strength <code>Concrete</code> and reinforcing <code>Steel</code>.</li>
                    <li>On <code>FamilyHouseExample</code> (<code>FamilyHouse</code>): Ceramic <code>Brick</code> masonry and <code>Concrete</code> floor slabs.</li>
                    <li>On <code>EmpireStateBuilding</code> &amp; modern <code>OfficeBuilding</code>: Structural <code>Steel</code> frames and composite slabs.</li>
                    <li>On <code>WoodenHouse</code>: Cross-Laminated Timber (<code>Wood</code>) panels.</li>
                </ul>
            </li>
            <li><b>Typical Duration &amp; Cost Share:</b> 30–35% of total timeline | 35–42% of total project budget.</li>
        </ul>

        <h3>Phase 4: FinishingWork (Class: <code>FinishingWork</code>)</h3>
        <p>
            The <code>FinishingWork</code> phase transforms the structural shell into a fully habitable, energy-efficient, and code-compliant building ready for client handover.
        </p>
        <ul>
            <li><b>Key Responsible Roles:</b> Specialized <code>ManualWorker</code> trades—specifically <code>Electrician</code> (wiring, switchboards, lighting, fire alarms on <code>BuildingProject</code>) and <code>Plumber</code> (water supply, underfloor heating, drainage on <code>ResidentialProject</code>)—supervised by the <code>SiteManager</code> and inspected by the <code>Customer</code>.</li>
            <li><b>Primary Materials Consumed:</b> Triple-glazed <code>Glass</code> windows and curtain walls, thermal and acoustic <code>Insulation</code>, interior plasters, flooring, and MEP fixtures.</li>
            <li><b>Typical Duration &amp; Cost Share:</b> 25–35% of total timeline | 35–45% of total project budget.</li>
        </ul>

        <h2>10.3 Summary Matrix: ConstructionPhase vs. Roles, Machines &amp; Materials</h2>
        <table>
            <tr>
                <th>Ontology Phase (<code>ConstructionPhase</code>)</th>
                <th>Lead Ontology Personnel</th>
                <th>Dominant <code>ConstructionMachine</code></th>
                <th>Dominant <code>Material</code> Subclasses</th>
                <th>Mandatory Quality Gate Sign-Off</th>
            </tr>
            <tr>
                <td><b>1. <code>Planning</code></b></td>
                <td><code>Architect</code>, <code>Designer</code>, <code>Customer</code></td>
                <td>Survey vehicles (pre-mobilization)</td>
                <td>Specification of all 6 material classes</td>
                <td>Gate QG-1: Building Permit &amp; BIM Approval</td>
            </tr>
            <tr>
                <td><b>2. <code>Foundation</code></b></td>
                <td><code>SiteManager</code>, <code>ConstructionWorker</code></td>
                <td><code>Excavator</code>, <code>Loader</code>, <code>Truck</code></td>
                <td><code>Concrete</code>, <code>Steel</code> (rebar), <code>Insulation</code> (XPS)</td>
                <td>Gate QG-2: Geodetic &amp; 28-Day Concrete Cube Test</td>
            </tr>
            <tr>
                <td><b>3. <code>StructuralWork</code></b></td>
                <td><code>SiteManager</code>, <code>ConstructionWorker</code></td>
                <td><code>Crane</code>, <code>Truck</code>, <code>Loader</code></td>
                <td><code>Concrete</code>, <code>Brick</code>, <code>Steel</code>, <code>Wood</code></td>
                <td>Gate QG-3: Structural Topping-Out &amp; Statics Audit</td>
            </tr>
            <tr>
                <td><b>4. <code>FinishingWork</code></b></td>
                <td><code>Electrician</code>, <code>Plumber</code> (<code>ManualWorker</code>), <code>SiteManager</code></td>
                <td><code>Truck</code>, <code>Loader</code> (site landscaping)</td>
                <td><code>Glass</code>, <code>Insulation</code>, MEP piping &amp; cables</td>
                <td>Gate QG-4: Pressure/Electrical Revision &amp; Occupancy Permit</td>
            </tr>
        </table>
        """
    }
]


def build_pdf(doc_info: dict, output_path: str) -> int:
    full_html = f"""<!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{CSS_STYLE}</style></head>
    <body>{doc_info["html"]}</body>
    </html>
    """
    story = pymupdf.Story(html=full_html)
    writer = pymupdf.DocumentWriter(output_path)
    mediabox = pymupdf.paper_rect("a4")
    # Leave margins: left=42, top=52, right=42, bottom=48
    where = mediabox + (42, 52, -42, -48)

    more = 1
    while more:
        device = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(device)
        writer.end_page()
    writer.close()

    # Open the generated PDF to add clean headers, footers, and PDF metadata
    pdf = pymupdf.open(output_path)
    total_pages = len(pdf)
    pdf.set_metadata({
        "title": doc_info["title"],
        "author": "ApexBuild Construction Corp. - Knowledge Engineering Team",
        "subject": f"Ontology Classes: {doc_info['ontology_focus']}",
        "keywords": doc_info["ontology_focus"],
        "creator": "ApexBuild Ontology-RAG Document Generator"
    })

    for page_idx, page in enumerate(pdf):
        # Header line and text
        header_y = 32
        page.draw_line(pymupdf.Point(42, header_y + 6), pymupdf.Point(mediabox.width - 42, header_y + 6), color=(0.75, 0.80, 0.88), width=0.7)
        page.insert_text(
            pymupdf.Point(42, header_y),
            f"ApexBuild Construction Corp. | {doc_info['doc_id']} | {doc_info['title'][:65]}",
            fontsize=8,
            fontname="helv",
            color=(0.35, 0.42, 0.52),
        )
        # Footer line and text
        footer_y = mediabox.height - 26
        page.draw_line(pymupdf.Point(42, footer_y - 10), pymupdf.Point(mediabox.width - 42, footer_y - 10), color=(0.75, 0.80, 0.88), width=0.7)
        page.insert_text(
            pymupdf.Point(42, footer_y),
            f"Ontology Focus: {doc_info['ontology_focus'][:85]}",
            fontsize=7.5,
            fontname="helv",
            color=(0.40, 0.45, 0.55),
        )
        page_label = f"Page {page_idx + 1} of {total_pages}"
        page.insert_text(
            pymupdf.Point(mediabox.width - 42 - 55, footer_y),
            page_label,
            fontsize=8,
            fontname="helv",
            color=(0.30, 0.35, 0.45),
        )

    temp_path = output_path + ".tmp"
    pdf.save(temp_path, deflate=True)
    pdf.close()
    os.replace(temp_path, output_path)
    return total_pages


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating 10 PDF documents in: {OUTPUT_DIR}\n" + "-" * 70)
    for item in DOCUMENTS:
        out_file = os.path.join(OUTPUT_DIR, item["filename"])
        pages = build_pdf(item, out_file)
        size_kb = os.path.getsize(out_file) / 1024.0
        print(f"[OK] {item['filename']:45s} | {pages} pages | {size_kb:6.1f} KB")
    print("-" * 70 + "\nAll 10 PDF documents successfully generated!")


if __name__ == "__main__":
    main()

