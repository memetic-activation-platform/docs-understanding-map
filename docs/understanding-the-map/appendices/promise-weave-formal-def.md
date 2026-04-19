# Promise Weave Protocol — Formal Definition (v0.3)

## 1. Purpose

The **Promise Weave Protocol (PWP)** is a decentralized coordination protocol that enables autonomous agents to discover, evaluate, and voluntarily converge on mutually compatible sets of promises under shared normative constraints, without requiring centralized brokers, global identities, durable reputation systems, or premature disclosure of capabilities.

PWP is explicitly designed to preserve agent sovereignty, exploratory freedom, and the ability to disengage without penalty. All coordination remains non-binding until an explicit commitment transition occurs.

---

## 2. Core entities

**Agent**  
An autonomous actor capable of making, evaluating, and honoring promises. An agent may participate in multiple Spaces using distinct cryptographic identities.

**I-Space (Individual Space)**  
An agent’s private execution and evaluation space. All promise matching, qualifier gating, role interpretation, threshold evaluation, and decision-making occur within the agent’s I-Space.

**ConnectionSpace**  
A shared broadcast space in which Placed Enquiries are published and observed by participating agents.

**Promise**  
A declarative commitment regarding future behavior, subject to acceptance and fulfillment.

**LifeCode Promise (LC)**  
A promise expressing normative, ethical, or principled constraints that must be jointly honored by all parties participating in a coordination.

**Role**  
A declared mode of participation within an Enquiry that shapes expectations, responsibilities, and promise interpretation, without asserting identity, authority, or binding obligation.

Roles:
- are defined by the Enquiry Template,
- structure how Needs and Offers are interpreted,
- and may be proposed, accepted, or declined by agents during refinement.

**PromiseWeaver**  
An agent-local process responsible for interpreting roles, evaluating qualifiers, matching promises, refining terms, and negotiating participation within the Promise Weave Protocol.

---

## 3. Enquiry structure

An **Enquiry** is defined by an **Enquiry Template** and instantiated as a tuple:

- **LC (LifeCode)**  
  A set of normative promises that must be jointly honored by all participants.

- **R (Roles)**  
  A set of roles defined by the Enquiry Template.

- **Nᵣ (Role-Specific Needs)**  
  For each role *r ∈ R*, a set of promises that an agent committing to role *r* seeks from agents in other roles.

- **Oᵣ (Role-Specific Offers)**  
  For each role *r ∈ R*, a set of promises that an agent committing to role *r* is willing to make to agents in other roles.

### 3.1 Role commitment

When placing an Enquiry, the originating agent MUST explicitly commit to **one** of the roles defined by the Enquiry Template.

This commitment:
- determines which **Nᵣ** and **Oᵣ** apply to the originator,
- does not imply exclusivity or permanence,
- and remains non-binding until an explicit commitment transition occurs.

---

### 3.2 Qualifiers

Within an Enquiry, the originating agent MAY designate any subset of its **role-specific Needs (Nᵣ)** and **LifeCode (LC)** promises as **Qualifiers**.

A **Qualifier** is a response-gating declaration that specifies conditions under which a response is considered meaningful enough to initiate engagement.

Qualifiers:
- are evaluated locally and fuzzily by receiving agents,
- do not require exact syntactic matching,
- do not imply rigidity or non-negotiability in later refinement phases,
- and apply *only* to determining whether a response should be sent at all.

Silence is the only negative signal; no null or rejection responses are ever emitted.

---

## 4. Placement phase

When an agent places an Enquiry into a ConnectionSpace, it becomes a **PlacedEnquiry (PEn)** with the following properties:

- The PEn is signed using the originator’s ConnectionSpace-local cryptographic identity.
- The PEn is broadcast to all members of the ConnectionSpace.
- The PEn contains **only**:
    - LC (LifeCode), including any LC-Qualifiers
    - R (Roles)
    - The originator’s committed role *r*
    - Nᵣ (role-specific Needs), including any Nᵣ-Qualifiers
- The PEn explicitly excludes all Offers (Oᵣ).

This phase establishes asymmetric disclosure and prevents premature exposure of agent capabilities.

---

## 5. Declarative Evaluation Semantics

Upon receipt of a **Placed Enquiry (PEn)**, an agent evaluates it against **all active Enquiries** it currently holds within its I-Space.

Evaluation is **declarative**, not procedural. The protocol defines *what must be true* for a response to be generated, not *how* an agent arrives there. No ordering, obligation, disclosure, or side effects are implied.

Let:

- **PEn** be the received Placed Enquiry
- **𝔼** be the receiving agent’s set of active Enquiries
- **QualLC(PEn)** be the set of qualifying LifeCode promises declared in PEn
- **Template(PEn)** be the Enquiry Template used by PEn
- **Role(PEn)** be the role committed to by the originator
- **QualN(PEn, r)** be the set of qualifying Needs for role *r* in PEn

All evaluation occurs privately within the agent’s membrane.

---

### 5.1 LifeCode Admissibility (revised)

An Enquiry **E ∈ 𝔼** is *LifeCode-admissible* with respect to **PEn** based on **LifeCode matches**.

A **LifeCode match** for a LifeCode promise **LCₓ** occurs iff:

- **LCₓ ∈ QualLC(PEn)** *and* **LCₓ ∈ E.LC**

That is, both **PEn** and **E** include the same LifeCode promise **LCₓ**.

Define the LifeCode-admissible subset as:

- **𝔼ᴸᶜ = { E ∈ 𝔼 | ∀ LCₓ ∈ QualLC(PEn), LCₓ ∈ E.LC }**

An Enquiry **E** is LifeCode-admissible iff it matches **all** qualifying LifeCode promises declared in **PEn**.

If **𝔼ᴸᶜ** is empty, no response is generated.

---

### 5.2 Template Compatibility

From the LifeCode-admissible set, retain only Enquiries whose template matches the template of **PEn**.

An Enquiry **E** is *template-compatible* iff:

- **Template(E) = Template(PEn)**

Define:

- **𝔼ᵀ = { E ∈ 𝔼ᴸᶜ | Template(E) = Template(PEn) }**

---

### 5.3 Role Compatibility

For each **E ∈ 𝔼ᵀ**, the agent determines whether **E** commits to a role that is compatible with the role committed to by the originator of **PEn**.

An Enquiry **E** is *role-compatible* iff:

- **E** commits to a role **r′** defined in **Template(PEn)**, and
- **r′ ≠ Role(PEn)** (unless explicitly allowed by the template)

Define:

- **𝔼ᴿ = { E ∈ 𝔼ᵀ | E commits to a role compatible with Role(PEn) }**

---

### 5.4 Needs Admissibility

For each **E ∈ 𝔼ᴿ**, evaluate the qualifying Needs declared by **PEn** for role *r*.

A **Need match** for **Nₓ ∈ QualN(PEn, r)** occurs iff:

- **E** includes at least one Offer that plausibly satisfies **Nₓ**

A **Need miss** occurs when **Nₓ** is present in **PEn** and **E** offers no plausible match.

An Enquiry **E** is *Needs-admissible* iff it matches **all** qualifying Needs for the relevant role.

Define:

- **𝔼ᴺ = { E ∈ 𝔼ᴿ | E satisfies all QualN(PEn, r) }**

---

### 5.5 Candidate Enquiries

The resulting set **𝔼ᴺ** constitutes the agent’s **Candidate Enquiries** for **PEn**.

Each **E ∈ 𝔼ᴺ**:

- Meets all qualifying LifeCode requirements,
- Is compatible with the Enquiry Template,
- Commits to a compatible role,
- Meets all qualifying Need requirements for that role.

For each Candidate Enquiry, the PromiseWeaver MAY generate a response.

Multiple responses MAY be generated from a single agent if multiple Enquiries in **𝔼ᴺ** qualify.

If **𝔼ᴺ** is empty, the agent remains silent.

Silence is the only negative signal.

### 5.6 Match Result Semantics

For each **Candidate Enquiry E ∈ 𝔼ᴺ**, the PromiseWeaver computes a **Match Result** describing the relationship between **PEn** and **E**.

Match Results are computed for **all** LifeCode and Need promises declared in **PEn**, not only those designated as Qualifiers.

This enables reflection, refinement, and co-sensing, while preserving the rule that **only qualifying promises determine whether a response is generated at all**.

---

#### 5.6.1 LifeCode Match Results

For every LifeCode promise **LCₓ ∈ PEn.LC**, a LifeCode match result is computed:

- **LCₓ : match**  
  iff **LCₓ ∈ E.LC**

- **LCₓ : no-match**  
  iff **LCₓ ∉ E.LC**

This includes:
- qualifying LifeCode promises (which gated the response), and
- non-qualifying LifeCode promises (which inform alignment and refinement).

---

#### 5.6.2 Need Match Results

For every role-specific Need **Nₓ ∈ PEn.Nᵣ**, a Need match result is computed:

- **Nₓ : match**  
  iff **E** includes at least one Offer that plausibly satisfies **Nₓ**

- **Nₓ : no-match**  
  iff **E** includes no such Offer

This includes:
- qualifying Needs (which gated the response), and
- non-qualifying Needs (which inform refinement and potential relaxation).

---

#### 5.6.3 Response Payload

For each Candidate Enquiry **E**, the response sent to the originator of **PEn** includes:

- The responder’s Enquiry identifier **E.id**
- The responder’s proposed role **r′**
- The responder’s declared **LC** and **Nᵣ′**
- The full set of **LifeCode match results** for all **PEn.LC**
- The full set of **Need match results** for all **PEn.Nᵣ**

Responses are sent only to the originator of **PEn**.

---

#### 5.6.4 Interpretive Note (non-normative)

Qualifiers determine **whether a response exists**.  
Match Results determine **what the response says**.

This separation preserves:
- asymmetric disclosure,
- exploratory safety,
- and reflective co-evolution of Enquiries and LifeCodes.

---

## 5. Initial evaluation phase

Upon receipt of a PEn, each receiving agent’s PromiseWeaver performs the following steps within its I-Space:

1. **Qualifier gating**
    - Evaluate whether all LC-Qualifiers and Nᵣ-Qualifiers are plausibly satisfiable *for at least one role the receiving agent is willing to consider*.
    - If any Qualifier is not satisfied, the PromiseWeaver MUST NOT respond.

2. **Role selection**
    - Identify one or more roles *r′ ∈ R* the receiving agent is willing to tentatively commit to.
    - Determine the corresponding Nᵣ′ and Oᵣ′ sets.

3. **Compatibility evaluation**
    - Evaluate overlap between:
        - PEn-LC and the agent’s own LifeCode promises.
    - Evaluate compatibility between:
        - PEn-Nᵣ and the agent’s Oᵣ′.

4. **Local recording**
    - Record shared LifeCode promises.
    - Record proposed role alignment.
    - Record matched role-specific Need–Offer promise pairs.

If the evaluation exceeds an agent-local acceptance threshold, the PromiseWeaver sends a response to the PEn originator containing:

- The responder’s proposed role *r′*,
- The responder’s corresponding **LC**, **Nᵣ′**, and **Oᵣ′**,
- The evaluation results.

No Offers (Oᵣ) are disclosed globally during this phase.

---

## 6. Reciprocal evaluation phase

Upon receiving a response, the PEn originator’s PromiseWeaver performs a reciprocal evaluation within its I-Space:

1. Evaluate the responder’s proposed role *r′* against the Enquiry Template.
2. Evaluate the responder’s Nᵣ′ against the originator’s Oᵣ.
3. Evaluate mutual compatibility of LC promises.
4. Record the resulting role alignment, promise matches, and LifeCode coherence.
5. Send the evaluation results back to the responding agent.

Completion of this exchange concludes the initial evaluation round for the PEn.

---

## 7. Iterative refinement phase

Agents whose evaluations exceed their local thresholds may voluntarily enter one or more refinement rounds.

In each refinement round, an agent may choose to:

- Add or relax it's LC promises.
- Add or relax its role-specific Nᵣ promises.
- Add or relax its role-specific Oᵣ promises.
- Decline further refinement -- effectively withdrawing themselves from the matching process for that Enquire.

All refinements are:
- voluntary,
- symmetric,
- locally evaluated,
- and reversible through disengagement.

No agent is obligated to continue participation across refinement rounds.

---

## 8. Termination conditions

An enquiry concludes for a given agent when any of the following conditions occur:

- A mutually satisfactory promise weave is achieved.
- The agent declines further refinement.
- The agent explicitly withdraws participation.

Withdrawal requires no justification and incurs no protocol-level penalty.

---

## 9. Binding transition

A Promise Weave becomes binding only when all participating agents explicitly commit to the finalized set of promises and roles through a distinct commitment action or protocol transition, which is outside the scope of the Promise Weave Protocol.

Until such a transition occurs, all participation remains exploratory and non-binding.

---

## 10. Enquiry types (non-exhaustive)

Different Enquiry types may be defined as Enquiry Templates over this protocol, including:

- **Join Enquiries** — role-structured affiliation and participation.
- **Service Enquiries** — reciprocal value flows across defined roles.
- **Co-Creation Enquiries** — multi-role collaborative exploration.

Enquiry types do not alter the core protocol semantics.

# Open Issues

This section is used to identify enhancements or corrections to this doc that have not yet been incorporated:

