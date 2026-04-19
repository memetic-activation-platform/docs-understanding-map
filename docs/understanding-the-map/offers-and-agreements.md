# 🤝 Offers and Agreements

**Offers** and **Agreements** are the foundational mechanisms by which Agents coordinate action, exchange value, and create shared context in the MAP.

While this section explores expressive forms capable of supporting complex, multi-party, even legally significant Agreements, **many Offers in MAP will be lightweight, informal, and intuitive**. A quick pledge, a mutual aid exchange, or a casual collaboration between neighbors — all of these fit comfortably in the same model.

> 🧘 *You don’t need a treaty to water your neighbor’s tomatoes.*  
> MAP simply gives you the grammar to coordinate trustably — whether your promise is simple or sophisticated.

What follows dives into the deeper architecture — not because coordination must be complex, but because the MAP must support **trustable complexity** when it matters.

---

## 📦 What is an Offer?

An **Offer** is a structured proposal composed of reciprocal **Promises**, organized by **roles**. It serves as the **template for an Agreement** — laying out who is involved, what each party promises, and under what conditions.

Each Offer defines:

- A set of **roles** that participating Agents may occupy (e.g., provider, recipient, funder)
- For each role, a set of **required Promises** (a.k.a., requirements) — specific commitments expected from Agents in that role
- **Aspirational Promises** that express values or alignment criteria (e.g., "Fair Trade Certified")
- **Vital Capital Flow Promises** — detailing the kinds of capital that will move (e.g., data, care, money, knowledge)
- Optional constraints — timing, thresholds, or conditional triggers
- **Governance Promises** — such as how disputes will be resolved, how roles may be amended, or how an agreement may be exited
- **Interaction Protocol Promises** — specifying how agents will interact (e.g., using [JLINC](https://jlinc.org/), [JLINX](https://jlinx.dev/), [Beckn Protocol](https://becknprotocol.io/), [Secure Scuttlebutt](https://scuttlebutt.nz/), or MAP-native protocols)

> When an Agent accepts an Offer, they step into a role and adopt the full set of Promises associated with it.

This role-based structure allows Offers to support **multi-party Agreements**. For example, a learning cohort might include roles for facilitator, learner, and funder — each with distinct Promises and flows.

Offers can span diverse types of value and coordination. A Promise might track a flow of care, reputation, presence, funds, or shared data — and do so differently for each participant.

Importantly, **each Agent defines the terms of their own Offers**. This supports MAP’s commitment to **empowered agency** — enabling participants to express and exchange value on their own terms. At the same time, a shared pool of reusable **Promise Types** and **Offer Templates** (see: [Promise Weaves](../../archive/promise-weaves.md)) allows new Offers to build on proven structures.

---

## 🛰 Where Offers Are Placed

To be matched, an Offer must be placed into a specific **AgentSpace** — the context in which it is discoverable and interpretable.

AgentSpaces vary widely in:

- **Reach** — from small private circles to global directories
- **Trust level** — from intimate, high-context groups to open public spaces
- **Purpose and filtering logic** — some are commons, some are marketplaces, some are ceremonial

> A single Offer might be published in a **high-reach, low-trust space** (like the Exosphere) for visibility — while being intended for execution only within **high-trust subspaces**.

Agents decide where to place their Offers based on intended audience, visibility preferences, and discovery strategy.

Future tooling may support Offer propagation, adaptation, or invitation across adjacent AgentSpaces — enabling ecosystems to **route Offers to the places they are most likely to be accepted**.

---

## 🔁 Matching Offers to Offers

In conventional platforms, we often speak of **matching “needs” to “offers.”** But the MAP model is more symmetrical: **every Offer includes both**.

When an Agent posts an Offer into an AgentSpace, they specify:

- **Which roles they are prepared to adopt** (i.e., which Promises they are making)
- **Which roles they seek others to fulfill** (i.e., which Promises they expect to be met)

> You can think of these as:
> 
> - The **requirements** of the Offer — Promises you are looking for others to fulfill
> - The **contributions** or **attributes** of the Offer — Promises you’re committing to fulfill yourself

For example:

> A **Grower** wants help assessing their soil’s capacity to grow heirloom tomatoes.  
> They publish an Offer with two roles:
> - **Grower** — promises to provide samples, location, and context
> - **Soil Expert** — expected to promise expertise, analysis, and recommendations
>
> The Grower signs the Offer in the Grower role and publishes it into a local regenerative farming AgentSpace.

Meanwhile, other Agents may have Offers advertising “Soil Assessment” services in the **Soil Expert** role. When the roles and promises across these Offers align — a **match** can be proposed, negotiated, or auto-suggested.

---

## 🤖 The Three Phases of Offer Matching

To support this matching process, a dedicated **Offer Matching mapp** guides Offers through three key phases: **preliminary matching**, **connection**, and **signing**.

### 1. Preliminary Matching (Anonymous Discovery)

Offers can be placed **anonymously** into an AgentSpace. In this phase:

- The **Offer Matching mapp** evaluates compatibility across all Offers in the space
- It highlights:
  - **Over-constrained Offers** — too many requirements, resulting in zero matches
  - **Under-specified Offers** — too few constraints, leading to too many mismatches

For example:

> “Relaxing the timing requirement or certification criteria would open up 3 more matching Offers.”
>
> “Adding a Promise around ecological region or method used could eliminate a large number of incompatible matches.”

The goal of this phase is to help Agents arrive at a **manageable candidate set** — ideally **5 to 7 potential matches** — while preserving privacy and agency.

No identities are revealed at this stage. Matching remains **possibility-oriented, not commitment-bound**.

---

### 2. Connection (Mutual Visibility and Alignment)

Once promising matches are identified, participating Agents may **move into a shared exploration phase**.

- Agents **reveal their identities** to one another
- Offers may be **fine-tuned** — small adjustments made to better align expectations or clarify edge cases
- The goal is not full negotiation, but **adaptive convergence**: aligning Promises and roles just enough to lock in a shared commitment

This phase establishes the social and technical trust necessary to move forward, without rushing to finality.

---

### 3. Signing (Commitment and Activation)

Each Agent **digitally signs** the Offer to formally accept a specific role.

- Offers may specify some roles as **mandatory** and others as **optional**
- Once **all mandatory roles have been signed**, the **Agreement is considered Accepted**
- At this point:
  - A new **Agreement-Based AgentSpace** is instantiated
  - All logic, interactions, and capital flows are governed by the terms of the Agreement

> This phase marks the shift from “provisional possibility” to **active commitment**.

It also activates the Agreement’s LifeCode, access protocols, and any associated Dances or governance logic.

---

## ✍️ What is an Agreement?

An **Agreement** is formed when one or more Agents accept roles defined in an Offer — formally committing to fulfill the Promises associated with those roles.

Each Agreement includes:

- A reference to the originating Offer and its terms
- A list of participating Agents and their accepted roles
- The **governing context** for all future interactions — such as service invocations, data access, and Promise fulfillment
- Optionally, a new **Agreement-Based AgentSpace** for coordinating action and tracking outcomes

> Agreements in MAP **transcend but include the functionality of Smart Contracts**.  
> Like Smart Contracts, they provide structured, enforceable commitments — but unlike blockchain-based contracts, they are not confined to purely software-enforceable scopes, nor do they require centralized consensus or global ledgers.  
> Agreements can include informal social promises, legally-binding terms, and interaction protocols — all anchored in shared consent and local sovereignty.

---

## 🧱 Three-Layered Representation: From Offer to Agreement

Both Offers and Agreements are expressed using a **three-layered architecture**, inspired by the [Creative Commons licensing model](https://creativecommons.org/licenses/). Just as Creative Commons defines a license through a human-readable deed, a machine-readable schema, and a legal code, MAP uses a layered approach to ensure legibility and enforceability across all domains of interaction.

1. **Human-Readable Layer**
  - A narrative or visual summary describing roles, Promises, and intentions
  - Supports shared understanding and informed consent

2. **Machine-Readable Layer**
  - A structured Holon with formal types, roles, and thresholds
  - Governs execution, trust, permissioning, and audits within the MAP infrastructure

3. **Legal-Form Layer** *(optional)*
  - A formal legal document aligned with the other layers
  - Enables engagement with courts, insurance systems, or regulatory institutions

> 🧩 *The three layers ensure Offers and Agreements are clear to humans, computable by systems, and actionable across jurisdictions.*

### 🔐 Cryptographic Integrity

The entire bundle — for both Offers and Agreements — is **cryptographically digested and signed** by all participating Agents. This provides:

- **Immutability**: the record cannot be altered without detection
- **Non-forgeability**: only valid Agents could have created the signature
- **Non-repudiability**: no Agent can deny their participation

---

## Promise Weaves as the Offer to Agreement Protocol

The _MAP's [Promise Weaver sub-system](promise-weaver.md)_ supports a coordination protocol by which Offers can become Agreements. If you are curious how this process could work in practice, Promise Weaver may be worth a look.

But you can also safely skip this section and [go directly to Vital Capital Flows](vital-capital-flows.md).