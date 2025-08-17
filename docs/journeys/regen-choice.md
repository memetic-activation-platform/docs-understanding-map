# RegenCHOICE

This section intends to demonstrate how the [RegenCHOICE model](https://www.simongrant.org/RegenCHOICE/) as developed by Simon Grant could be expressed in the MAP. 
The RegenCHOICE model can be seamlessly implemented within the MAP framework, using RegenCHOICE’s unique terminology and approach to matchmaking. This document not only demonstrates how RegenCHOICE’s concepts integrate with the MAP, but also highlights an exciting capability of the MAP: the ability to translate between different terminologies using ontological maps. This means that users can effortlessly recast RegenCHOICE offers into Promise Weaver terms, and vice versa, ensuring a cohesive and flexible experience for all users.

**RegenCHOICE** is a MAP-powered application that supports alignment and coordination across diverse areas of life. It allows people and groups to post and respond to structured Enquiries, defining what they are looking for and what they are offering, across relationships such as friendship, employment, collaboration, or shared living.

RegenCHOICE builds entirely on the **Promise Weaver** subsystem. Each Enquiry is implemented as a Promise Weaver Offer — consisting of publicly shared Requirements (Required Promises) and private Answers (Promises), held confidential until a match threshold is met. Enquiry Types serve as Offer Templates, hosted in the Global Meme Pool, aligned with LifeCodes and norms of associated AgentSpaces.

---

## 🎯 Purpose

RegenCHOICE enables:
- Memetic alignment before disclosure of identity or resources
- Structured negotiation of commitments
- Multidimensional value matching
- Legal and ethical sensitivity in socially nuanced domains

It supports a values-centered, privacy-respecting, and agent-centric form of choosing that empowers trust-based connection and reciprocity.

---

## 🧠 How RegenCHOICE Behavior Maps to Promise Weaver

RegenCHOICE is not a separate matching engine — it is a **narrative and user-facing layer** that configures and contextualizes the general-purpose functionality of Promise Weaver.

- An **Enquiry** is a Promise Weaver Offer with a human-friendly framing and domain-specific templates
- A **Requirement** is a Required Promise — something the Enquirer is asking others to promise
- An **Answer** is a Promise — something the Enquirer is willing to do or give in return
- The **matching protocol** is the same as Promise Weaver: privacy-preserving broadcasting of Requirements, local filtering of Responses, iterative refinement if needed, then mutual reveal and agreement

What RegenCHOICE adds:
- Enquiry Types tailored to life contexts (e.g., Collaborating, Sharing)
- Regulatory scaffolding (e.g., legal constraints on employment questions)
- Social framing that makes these relationships intelligible and familiar
- Cultural alignment mechanisms (LifeCodes, Rituals, Norms)

---

## 🧩 Architecture Overview

| RegenCHOICE Layer          | MAP Subsystem or Concept         | Description                                   |
|---------------------------|----------------------------------|-----------------------------------------------|
| Enquiry                   | Offer                            | Structured Offer containing Promises and Requirements |
| Enquiry Type              | Offer Template (Global Meme Pool)| Predefined structure with domain-specific fields |
| Chooser / Actor           | Agent                            | Person or group issuing or responding to Enquiry |
| Answer                    | Promise                          | What an Agent is willing to do or offer         |
| Requirement               | Required Promise                 | What an Agent is asking others to promise       |
| Match / Candidate         | Matching via Promise Weaver      | Mutual satisfaction of Requirements and Promises |
| Space / Domain            | AgentSpace                       | Context in which Enquiries circulate            |
| Roles (e.g. employer)     | Role expectations in LifeCode    | Role patterns defined by the Space's LifeCode   |

---

## 📒 Enquiry Types

Each Enquiry Type is tailored to a specific area of life and defines the symmetry/asymmetry, expected commitment, and legal/cultural expectations of the relationship.

### 🤝 Sharing
Mutual interests, friendships, non-commercial relationships
- Peer-to-peer, symmetric
- No financial exchange
- May involve intimacy filters

### 👥 Collaborating
Starting ventures, co-ops, mutual work projects
- Symmetric among peers
- May include revenue or legal structures
- High trust, co-stewardship

### 🏠 Living Together
Co-housing, communes, or shared homes
- Group ↔ individual or symmetric among peers
- Long-term commitment
- Emphasizes location and lifestyle alignment

### ✋ Helping
Short-term support, tutoring, care, or service exchange
- Asymmetric (helper ↔ helped)
- May be paid or volunteered
- Time-bounded, clear scope

### 🧑‍💼 Employing
Job-seeking and hiring with formal compensation
- Organization ↔ individual
- Jurisdiction-sensitive
- Legal compliance and role expectations

### 🪷 Joining Groups
Finding affinity groups, clubs, spiritual orgs
- Individual ↔ organization
- Varies in commitment and purpose
- May involve codes of conduct, rituals, or dues

---

## 📘 Implementation Notes

- All Enquiry Types are defined as Offer Templates in the Global Meme Pool
- Answer and Requirement fields are schema-linked and privacy-aware
- LifeCodes govern what roles, disclosures, and thresholds are required within each AgentSpace
- Promise Weaver’s matching protocol enables iterative refinement, threshold tuning, and mutual consent before reveal

---

## 🧪 Detailed Scenario: Collaborating on a Regenerative Venture

**Setting the Stage:**  
Jordan is eager to launch a regenerative agriculture venture. They create a *Collaborating* enquiry to find a values-aligned co-creator.

### Step 1: Initial Enquiry
- Jordan selects “Collaborating” as the Enquiry Type
- They specify Requirements like:
    - Experience in permaculture or regenerative agriculture
    - Capacity to co-invest at least 15 hours/week
    - Comfort with shared decision-making
- Jordan also writes Answers (Promises), including:
    - Access to land in a bioregion
    - Initial capital for startup costs
    - Local distribution relationships

### Step 2: Broadcast Requirements
- Jordan’s Requirements are shared (anonymously) in a bioregion-specific AgentSpace
- Other Agents’ software evaluates whether they can commit to meeting some or all of the Requirements

### Step 3: Threshold Matching
- Alex sees Jordan’s Enquiry and can meet 3 of the 4 Requirements
- Alex’s software evaluates that this exceeds their “response threshold” and replies with:
    - The subset of Requirements they can meet
    - Their own Requirements (e.g., equitable co-ownership)
- No identities are exchanged yet

### Step 4: Iterative Refinement
- Jordan receives multiple partial matches
- Their client interface highlights:
    - Which Requirements filtered out potential matches
    - Which adjustments might yield better fit
- Jordan relaxes the time commitment slightly and rebroadcasts

### Step 5: Threshold Met, Reveal
- After refinement, 3 Candidates meet the new Requirements
- Jordan and Alex mutually agree to reveal:
    - Full Answers
    - Identity and contact information

### Step 6: Agreement Formation
- With mutual understanding in place, Jordan and Alex:
    - Compose an Agreement via MAP’s Agreement subsystem
    - Include their negotiated commitments and any governance terms
    - Sign cryptographically for immutability and auditability

---

## 🧭 Ontological Mapping Summary

| RegenCHOICE Term   | MAP Equivalent           | Notes                                                      |
|--------------------|--------------------------|------------------------------------------------------------|
| Enquiry            | Offer                    | Includes public Requirements and private Answers          |
| Answer             | Promise                  | Only revealed when mutual fit threshold is met            |
| Requirement        | Required Promise         | Expresses what chooser asks others to promise             |
| Question           | Match Constraint         | Either about an agent (property) or about the relationship |
| Candidate          | Match                    | Another Agent whose Answers meet the Requirements         |
| Chooser / Actor    | Agent                    | RegenCHOICE restricts to humans acting for themselves      |
| Enquiry Type       | Offer Template           | Defines structure, defaults, and legal framing            |

RegenCHOICE narrows and contextualizes the general-purpose substrate provided by Promise Weaver. It gives people a vocabulary, legal boundary-awareness, and curated starting points for building regenerative, reciprocal, and trust-aligned relationships.