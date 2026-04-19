# 💧 Vital Capitals in the MAP
### Modeling value as flow in regenerative coordination

---

## 🌱 Why Vital Capitals?

In the MAP, any **agent can offer services** to other agents -- defining their own terms by specifying reciprocal promises
about what flows between participants through the act of engagement.

In most systems of coordination, value is flattened into narrow forms — usually financial. This flattens our capacity to name, honor, or exchange the full range of what we care about.


The MAP takes a different approach.

> We aim to support the richest possible spectrum of human and ecological value — without collapsing it into a single metric or logic.

To do this, MAP introduces the concept of **Vital Capitals**:

- A **plural**, extensible way to represent what matters
- A **layered abstraction** that supports meaning, coordination, and measurement
- An **extensible foundation for promises, offers, thresholds, and sustainability quotients (SQs)**

> Vital Capital is the lifeblood of the MAP.

MAP’s capital model draws from the work of:

- **Context-Based Sustainability (CBS)** (McElroy, 2008)
- **Multi-Capital Frameworks** in integrated reporting
- **Doughnut Economics** (Kate Raworth, 2017)
- **Regenerative Economics** (e.g. John Fullerton, Capital Institute)

These sources offer a **multi-capital lens** for understanding and tracking value beyond financial metrics.

> 📘 Curious about the term's origins? See [Why the MAP Uses the Term “Vital Capitals”](appendices/vital-capital-lineage.md)

### What This Enables
Vital Capitals let us:

- Model **gifts, services, commitments, or contributions** — from **relational to transactional**
- Express value in **multiple dimensions** at once
- Coordinate with **symbolic** or **quantitative** logic — or both
- Sustain **local ecosystems** through stock/flow dashboards and threshold awareness
- Extend value expression to **rituals, meaning, care, attention, trust, and presence**

MAP offers a scaffold:

- General enough for emergent use
- Specific enough for software coordination
- Extensible enough for diverse cultural, economic, and spiritual paradigms

> By minimizing ontological imposition, we **maximize expressive freedom** —  
> empowering communities to define, steward, and regenerate what they value most.

To support this, MAP introduces a layered abstraction of value —  
rooted in real-world flows, inspired by regenerative economics,  
and extensible enough to include both measurable assets and symbolic presence.

---

## 🧭 A Layered Landscape of Value

MAP organizes value across several layers to honor different forms of meaning, coordination, and measurement:

| **Layer**                            | **Definition**                                                                                | **Purpose in MAP**                         |
|--------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------|
| **Relational Value**                 | Anything an agent or Space may care about — whether or not it’s modeled.                      | Philosophical grounding (not scaffolded)   |
| **Vital Capitals**                   | Declared types of value that may be flowed, promised, stewarded, or referenced in agreements. | Core MAP abstraction for coordination      |
| **Sustainability-Eligible Capitals** | Subset of Vital Capitals that are **measurable** and suitable for SQ computation.             | Enables contextual thresholds and tracking |
| **Assets / Resources**               | Specific, instantiable representations of value (where applicable).                           | Enables flow logic and operational roles   |

> Some Vital Capitals can be directly flowed or exchanged.
Others, like love or trust, can flow without depletion — they are amplified through sharing.
Still others, like presence or silence, may not flow in the traditional sense,
but can be held, invoked, or honored within coordination.

---

## 🔠 Vital Capital Types (Initial Set)

MAP defines a common set of **Vital Capital Types** to get started. Communities are encouraged to extend this list.

| **Capital Type**         | **Description**                                                       |
|--------------------------|-----------------------------------------------------------------------|
| **Natural Capital**      | Ecosystem services, land, water, air, biodiversity                   |
| **Human Capital**        | Skills, labor, knowledge, health, attention                          |
| **Social Capital**       | Trust, reputation, relationships, group cohesion                     |
| **Cultural Capital**     | Stories, rituals, traditions, symbols, identity                      |
| **Built Capital**        | Tools, infrastructure, digital systems, physical assets              |
| **Financial Capital**    | Currency, tokens, credit, investments                                |
| **Experiential Capital** | Aesthetic, emotional, and lived experiences                          |
| **Memetic Capital**      | Values, beliefs, narrative codes, memetic signatures                 |
| **Temporal Capital**     | Time, availability, scheduling of attention                          |
| **Spiritual Capital**    | Purpose, presence, connection to meaning (optional but supported)    |

> 🌿 **Extensible by communities** — define your own: *Ancestral Capital*, *Environmental Capital*, *Play Capital*, *Ritual Space*, *Silence*, *Emergence*, etc.

---

## 🔁 Multi-Dimensional Capital Flows in MAP Agreements

Every **Agreement** in MAP is structured as a bundle of **Promises** made by each participating Agent, each of which can involve specific flows of **Vital Capital**. These Promises may reference different capital types — such as time, care, knowledge, or financial instruments — and together they define the **multi-dimensional value exchange** represented by the Agreement.

A Promise might say: "I will contribute 4 hours per week of mentoring (Human Capital)," or "I will share community data insights (Memetic Capital)," or even, "I will transfer 100 tokens upon completion (Financial Capital)." But it is the **collection of Promises** across all roles that articulates the full dimensionality of the exchange.

This is a core differentiator of MAP Agreements: instead of reducing coordination to a **single monetary price**, Agreements can specify **many types of value flows** in parallel — each explicitly described, contextualized, and governed.

Agreements may specify for each flow:

* `capitalType`: What kind of capital is involved
* `direction`: Incoming / outgoing (from the perspective of the Agent making the commitment)
* `quantity`: Scalar (e.g. 10 hours), symbolic (e.g. “ongoing”), or subjective (“sufficient”)
* `conditions`: Rules or thresholds that gate the flow
* `impact`: Intended or observed outcomes of the flow

---

## 🔄 Patterns of Flow

MAP supports several **flow archetypes**, encoded in Agreement and Promise structures:

| **Pattern**              | **Description**                                                                   |
|--------------------------|-----------------------------------------------------------------------------------|
| **Gift Flow**            | Unconditional giving (e.g. "I will share this value freely.")                     |
| **Reciprocal Flow**      | Mutual exchange based on parity or complementarity                                |
| **Mutualism**            | Coordinated flows for shared benefit (e.g. co-creation of a shared resource)      |
| **Stewardship Flow**     | One party promises to care for or maintain value on behalf of others              |
| **Commons Contribution** | Value flows into a collectively accessible pool                                   |
| **Conditional Flow**     | Value flows only if certain criteria are met (e.g. trust, role, proposal outcome) |

---


## 🔧 Functional Dimensions of Vital Capitals

Each **Vital Capital Type** can optionally declare **functional dimensions** —  
flags that trigger specific capabilities in the extensible set of services offered by your fellow Travelers.

These dimensions are used by DAHN, Agreements, Protocols, and Dashboards to dynamically offer appropriate behaviors.

| **Dimension**           | **Definition**                                                                  | **Example Values** | **Enables...**                                        |
|-------------------------|---------------------------------------------------------------------------------|--------------------|-------------------------------------------------------|
| `quantifiable`          | Can this capital be expressed using numbers or scalar amounts?                  | `true` / `false`   | SQs, thresholds, dashboards, quantities in agreements |
| `transferable`          | Can this capital move between agents or be reassigned?                          | `true` / `false`   | Stewardship, offers, exchange flows                   |
| `durable`               | Does it persist over time (like a stock) after being received or offered?       | `true` / `false`   | Stock/flow tracking, sustainability modeling          |
| `replenishable`         | Can it be restored, renewed, or regenerated after use?                          | `true` / `false`   | Restoration flows, regenerative practice tracking     |
| `formalizable`          | Can its use or exchange be governed by structured logic or agreements?          | `true` / `false`   | Access constraints, thresholds, smart agreements      |
| `tangible`              | Is it materially embodied or physically instantiated?                           | `true` / `false`   | Logistics, location specificity, inventory management |
| `observable`            | Can others perceive or attest to its presence or expression?                    | `true` / `false`   | Reputation, trust signals, witness attestations       |
| `symbolic_only`         | Exists purely in narrative, ritual, or symbolic space (not material or digital) | `true` / `false`   | Rituals, role enactments, meaning flows               |
| `consumable`            | Is it used up or diminished through participation or sharing?                   | `true` / `false`   | Scarcity logic, usage constraints, restoration logic  |
| `uniquely_identifiable` | Can individual instances be tracked distinctly (e.g., books, artworks)?         | `true` / `false`   | Asset tracking, provenance, serialization             |

---

## 🧰 Example Vital Capitals Across Dimensions

Below is a curated set of examples showing how different Vital Capitals vary across **multiple functional dimensions**. These examples include edge cases that clarify what it means for something to be **replenishable**, **formalizable**, or **uniquely identifiable**.

| **Vital Capital**  | `quantifiable` | `transferable` | `durable` | `replenishable` | `formalizable` | `tangible` | `observable` | `symbolic_only` | `consumable` | `uniquely_identifiable` | **Notes**                    |
|--------------------|----------------|----------------|-----------|-----------------|----------------|------------|--------------|-----------------|--------------|-------------------------|------------------------------|
| **Water**          | true           | true           | true      | true            | true           | true       | true         | false           | true         | false                   | Physical, metered            |
| **Presence**       | false          | false          | false     | false           | false          | false      | false        | true            | false        | false                   | Emergent, relational         |
| **Reputation**     | partial        | false          | true      | partial         | false          | false      | true         | false           | false        | false                   | Attested, social             |
| **Love**           | false          | false          | true      | true            | false          | false      | true         | true            | false        | false                   | Grows through sharing        |
| **Time**           | true           | false          | false     | false           | true           | false      | true         | false           | true         | false                   | Scarce, not renewable        |
| **Labor**          | true           | true           | true      | true            | true           | true       | true         | false           | true         | false                   | Formalizable service         |
| **Trust**          | partial        | false          | true      | true            | false          | false      | true         | false           | false        | false                   | Built or broken relationally |
| **Sacred Silence** | false          | false          | false     | false           | false          | false      | false        | true            | false        | false                   | Symbolic, emergent           |
| **Book (printed)** | true           | true           | true      | false           | true           | true       | true         | false           | false        | true                    | Tangible, trackable asset    |

---

### 💡 Notes on Interpretation

- Some values (like **Love** or **Reputation**) are **non-rivalrous** and not depleted by sharing.
- Others (like **Time** or **Labor**) are **consumable** and must be carefully allocated or replenished.
- **Formalization** applies to resources that can be governed by agreements or policies (e.g., time, water, money).
- **Symbolic-only** value types support meaning-making and ritual without requiring measurement or exchange.
- The `uniquely_identifiable` dimension tracks whether distinct instances matter — e.g., serialized artifacts vs. bulk commodities.

---

## ⚙️ MAP Affordances Enabled by Functional Dimensions

The MAP Core provides a flexible scaffold for defining and coordinating Vital Capitals —  
but it does **not** prescribe fixed behaviors for all types.

> **Extensions to the MAP Core** (e.g. DAHNs, visualizers, smart agreements) may introduce  
> specific behaviors — such as dashboards, constraints, or rituals — **when certain functional dimensions are present**.

The table below summarizes potential affordances that can be layered on *if* the relevant dimensions are true:

| **Affordance**                     | **Requires...**                                  |
|------------------------------------|--------------------------------------------------|
| **Sustainability Quotients (SQ)**  | `measurable: true`, `persistent: true`           |
| **Threshold-Constrained Promises** | `measurable: true`, `formalizable: true`         |
| **Stock Dashboards**               | `persistent: true`                               |
| **Transfer & Stewardship Flows**   | `transferable: true`                             |
| **Restoration Protocols**          | `replenishable: true`, `depletes_with_use: true` |
| **Observer Attestations**          | `observable: true`                               |
| **Ritual-Based Agreements**        | `symbolic_only: true`                            |
---

## 🔗 Example Holon Declaration

```json
{
  "type": "#VitalCapitalType",
  "key": "Love",
  "display_name": "Love",
  "description": "A generative, relational force that increases through sharing",
  "functional_dimensions": {
    "measurable": false,
    "transferable": false,
    "persistent": true,
    "observable": true,
    "replenishable": false,
    "formalizable": false,
    "tangible": false,
    "symbolic_only": true,
    "depletes_with_use": false
  }
}
```

---
---

## 📏 Thresholds, Sustainability Quotients, and Dashboards

To support meaningful regenerative coordination, the MAP integrates key ideas from **Context-Based Sustainability (CBS)**, including:

* **Sustainability Thresholds**: Context-specific boundaries (ecological, social, economic) that define what constitutes a *sustainable state* for an Agent or Agent Space.
* **Sustainability Quotients**: Metrics that compare actual behavior to defined thresholds.
* **Dashboards**: DAHN modules that surface these metrics to support awareness, reflection, and adaptive coordination.

> 🧠 *An Agent Space is **sustainable** to the extent that its Vital Capital flows and stocks remain within the thresholds that define what it can justly and safely take, give, or impact — in context.*

---

### 🔹 What Is a Threshold?

A **Threshold** defines the **contextually appropriate limit** for a particular Vital Capital flow or stock. Examples include:

* **Ecological**: How much water can be used without degrading the watershed?
* **Social**: What level of care ensures dignity and belonging?
* **Economic**: What balances ensure resilience without extraction?

Thresholds are defined per capital type and may come from:

* Governance within Agent Spaces
* Commons stewardship principles
* Scientific knowledge or traditional wisdom
* Memetic codes embedded in LifeCodes

---

### 🔹 Sustainability Quotient (SQ)

The **Sustainability Quotient** compares actual behavior to the defined threshold:

* If SQ ≤ 1 → the flow is within sustainable bounds
* If SQ > 1 → the flow exceeds the sustainable threshold (overshoot)

Each Vital Capital type can have its own SQ, offering a multi-dimensional portrait of sustainability. MAP doesn't collapse this into a single score — it supports holistic, context-aware feedback.

---

### 🔹 Example: Water Use

* **Capital Type**: Natural Capital (Water)
* **Threshold**: 50L/day/person
* **Actual Use**: 40L/day/person
* **Result**: SQ = 0.80 → Sustainable (20% headroom)

In DAHN, this could be visualized as:

* A green arc showing 80% fill
* Narrative insight: “Usage within sustainable limits”
* Suggestion: “Consider contributing surplus to a commons”

---

### 🔹 Capital Dashboards for Every Agent Space

Each Agent Space — whether individual or collective — can activate dashboards in DAHN to track:

| **Dimension**                | **What It Shows**                                 |
| ---------------------------- | ------------------------------------------------- |
| **Vital Capital Flows**      | Inflows and outflows by type and period           |
| **Capital Stocks**           | What is being stored, cultivated, or depleted     |
| **Sustainability Quotients** | Performance relative to thresholds                |
| **Trend Arcs**               | Direction and velocity of change                  |
| **Alerts and Prompts**       | When nearing or exceeding safe limits             |
| **Regenerative Insights**    | Suggestions for rebalancing or restorative action |

These dashboards are configurable and privacy-aware. They can be kept private for self-awareness, shared selectively with trusted peers, or integrated into governance decisions.

---

## 🧷 Conclusion: Why Vital Capital Matters

Most coordination systems reduce value to monetary terms, hiding the richness of what actually flows between people and across communities. The MAP elevates **Vital Capital** as a first-class, memetically expressive structure for meaningful exchange.

- It makes visible the many forms of value that support life and relationship.
- It invites regenerative action based on sufficiency, not extraction.
- It enables stewardship and reciprocity within the commons.
- **Vital Capitals** are plural, diverse, and community-defined.
- They are modeled in MAP as **flows between agents and Spaces** — not just static resources.
- **Sustainability Quotients (SQs)** are fully supported where appropriate, grounding coordination in CBS’s context-aware model.
- Communities can define their own capital types, declare functional behaviors, and use MAP to coordinate **what they value — in their own terms**.


> MAP doesn’t just move information or money.  
> It makes it possible to coordinate around what really matters — in all its dimensions.

---

## 📚 Acknowledgements

The MAP concept of **Vital Capitals** is directly inspired by the work of  
**Mark W. McElroy** and the **Center for Sustainable Innovation**,  
especially the framework of **Context-Based Sustainability (CBS)**:

> McElroy, M. W. (2008) [Social Footprints: Measuring the Social Sustainability Performance of Organizations.](https://research.rug.nl/en/publications/social-footprints-measuring-the-social-sustainability-performance)  
> [Essence of Context-Based Sustainability](https://www.sustainableorganizations.org/Essence_of_CBS.pdf)

MAP extends CBS with a holonic, flow-native, consent-based coordination layer —  
preserving its rigor while opening to ritual, meaning, and regeneration.

[The Metacurrency Project](https://metacurrency.org)