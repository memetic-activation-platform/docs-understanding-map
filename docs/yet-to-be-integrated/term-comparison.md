# 🔄 MAP Terms vs. Conventional Information Systems Terms

Here is a high-level comparison of some of the key terms used in the MAP and how they are both similar to and different from terms in conventional informations systems architectures.

More detailed comparisons of each are provided following the table.

| **MAP Term**           | **What It Means in MAP**                                                                                                                                                     | **Closest Counterpart in Conventional Architectures**                    | **Key Difference / Novelty**                                                                                                                                                                                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dance**              | Atomic software action — the smallest unit of invocation/activation, declared by any type (holon, relationship, value type).                                                 | **API call / method invocation / affordance**                            | Dances are *self-describing holons* with consent and provenance built in. They are always contextualized by agreements and membranes.                                                                                                                                                       |
| **Application (Mapp)** | A bundle of related holons exposing a coherent set of capacities, embodied as dances. Each application is a software agent deployable in multiple Spaces.                    | **Microservice-based App**                                               | Like microservice apps, Mapps are compositions of reusable, shared components — but they run on a holonic substrate, hosted on Holochain. All data and behavior are self-describing holons, integrated directly into knowledge graphs, Spaces, and agreements rather than siloed databases. |
| **Service**            | A framework for offering capacities (human or software) under specified commitments and reciprocal value flows. Can include gifts, transactions, or non-transactional flows. | **Service (SOA / SaaS) / Contract / API-as-a-service**                   | Broader scope: includes *human services* and *social capacities*, not just software. Service offers always produce Agreements (and often Agreement Spaces).                                                                                                                                 |
| **Service Offer**      | A declaration that a capacity is available, with terms of reciprocity and value flow.                                                                                        | **Service contract / SLA (Service Level Agreement)**                     | Always grounded in agent sovereignty and consent. It’s not “terms imposed” but “commitments offered.”                                                                                                                                                                                       |
| **Agreement Space**    | A membrane-bound context created when a service offer is accepted. Holds commitments, value flows, and governance logic.                                                     | **Contract workspace / Shared database schema / Project team site**      | Immutable, cryptographically signed, and agent-centric. Defined strictly by the Agreement itself, not by an app provider.                                                                                                                                                                   |
| **Connection Space**   | A high-reach venue where needs and offers are surfaced, matched, and refined.                                                                                                | **Marketplace / Bulletin board / Matching service**                      | Privacy-preserving needs/offer matching protocol; planetary scope possible without sacrificing sovereignty.                                                                                                                                                                                 |
| **Discovery Space**    | A venue where memes/ideas are stewarded into visibility and can be browsed.                                                                                                  | **Knowledge base / Library / Registry / App store**                      | Stewardship and provenance are attached to each idea/meme. Discovery doesn’t confer modification rights.                                                                                                                                                                                    |
| **Space (general)**    | A living social organism — a collaboration of agents with persistence, governance, and memetic identity.                                                                     | **Organization / Tenant / Namespace / Multi-tenant container**           | Not just a container — Spaces are **sovereign agents** in their own right (social holons). Apps live inside Spaces, not the other way around.                                                                                                                                               |
| **LifeCode**           | The memetic signature of a Space or Agent: its values, principles, and commitments.                                                                                          | **Org charter / Mission statement / Policy framework / Schema metadata** | Both human-readable and machine-readable; can evolve and fork; actively governs membrane behavior.                                                                                                                                                                                          |
| **Trust Channel**      | Selective conduit across a membrane for sharing commitments and flows.                                                                                                       | **Secure channel / VPN / ACL (access control list)**                     | Not just technical security; also social trust + consent-based access. Built into the fabric of how information and value flow.                                                                                                                                                             |
| **Vital Capital**      | The multidimensional forms of value that can flow (knowledge, care, trust, materials, time, money, meaning).                                                                 | **Assets / Resources / Capital (usually financial)**                     | Explicitly tracks *non-financial* value in software — care, trust, memetics — alongside financial.                                                                                                                                                                                          |

# Detailed Comparisons

## ⚖️ Mapps vs. Conventional Applications

### Closest Counterpart
**Microservice-based Applications** — both Mapps and microservice apps are **compositions of reusable, shared components**. But they diverge fundamentally in their substrate and ontology.

---

### 1. Execution Context
- **Monolithic Apps** run on conventional operating systems, bundling presentation, logic, and persistence in one silo.
- **Microservices** run on containerized or cloud operating systems, virtualizing the underlying OS and exposing APIs for bounded contexts.
- **Mapps** run on a **holonic core**, hosted on **Holochain**:
    - Every element (data, behavior, relationship) is a **self-describing, active holon**.
    - Persistence is not in external databases but in a **distributed knowledge graph** co-hosted by participating agents.

---

### 2. Native Ontology
- **Conventional Apps/Microservices**: schemas and APIs are defined externally. Data models must be interpreted by code; the models do not describe themselves.
- **Mapps**: the substrate is **self-describing**. Holons declare their own types, properties, relationships, provenance, and dances.
    - This enables **open-ended extensibility** and schema evolution without brittle migrations.

---

### 3. Agency
- **Conventional Apps/Microservices**: Applications are tools external to the organizations that use them. They don’t act as first-class agents in a system.
- **Mapps**: Each application is itself a **software agent**.
    - A Mapp can join Spaces, form Agreements, and participate directly in value flows.
    - They don’t just provide functionality — they embody agency in the ecosystem.

---

### 4. Integration & Composition
- **Conventional**: Integration happens by wiring APIs together. Semantics, provenance, and trust must be coordinated externally (through middleware, contracts, documentation).
- **Mapps**: Composition is **graph-native**.
    - Holons from different Mapps can interlink directly in the knowledge graph.
    - Semantics, provenance, and access are embedded in the holons and enforced by membranes.

---

### 5. Persistence & Provenance
- **Conventional Apps/Microservices**: State is persisted in databases owned and controlled by the app or provider. Provenance/audit must be added on top.
- **Mapps**: State is **holochain-hosted** across all participating agents.
    - Data has cryptographic provenance, immutability, and distributed availability by default.
    - There is no external database siloed under provider control.

---

### ✨ Key Difference Summary
**Mapps resemble microservice-based applications in that they are compositions of reusable, shared components. But they are deployed on a holonic substrate, hosted on Holochain, where every element is a self-describing holon. This gives them native provenance, extensibility, and agency within Spaces — enabling them to participate directly in agreements and multidimensional value flows, rather than acting as siloed tools bound to external databases.**