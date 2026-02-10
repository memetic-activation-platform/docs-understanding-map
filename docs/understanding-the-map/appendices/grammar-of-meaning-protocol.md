# Grammar of Meaning — Protocol Specification

## 0. Purpose

The Grammar of Meaning defines the generative processes by which **Memes**, **MemeGroups**, and **MemePlexes** are created, referenced, evolved, stewarded, versioned, and composed across the MAP.

It enables Agents and Spaces to co‑create **shared meaning** without sacrificing sovereignty, contextual nuance, or lineage.

This grammar is **generative**, not prescriptive; it describes *how new meaning emerges*, not what it must be.

---

## 1. Core Memetic Constructs

The MAP memetic model distinguishes between two layers:

- **Semantic layer** — the **meaning itself** (concepts, distinctions, principles)
- **Semiotic layer** — the **expression** of that meaning (words, symbols, images)

A **Meme** exists at the **semantic layer**. It defines what a thing means, independent of how it is expressed. A single Meme may have many **memetic expressions**, and different communities may annotate or reinterpret it in context.

### 1.1 Meme

A **Meme** is an immutable, stewarded unit of meaning. It is not a string of text, but a concept, distinction, value, schema, principle, or narrative construct. It may have many memetic expressions but retains a stable referential identity.

Memes may link to other Memes via an extensible set of named `HolonRelationships`, forming a **web of meaning**. Some of these relationships are **definitional**—their presence defines what a particular version of the Meme means (see §7).

**Examples:**
- The concept of **regenerative agriculture**
- A principle like **“Power with, not power over”**
- A governance model
- A standard Enquiry template
- A pattern such as **trust channel**
- A schema for **data consent levels**
- A distinction between **cooperation** and **coordination**

### 1.2 Memetic Expression (Semiotic Layer)

Cultural artifacts that *express* the meaning of a Meme:
- A blog post explaining a Meme
- An icon used to represent it
- A diagram illustrating a trust boundary
- A song or gesture embodying a value

These are linked via `Expresses → Meme`, but are not themselves Memes.

### 1.3 MemePlex

A **MemePlex** is a set of Memes that replicate more effectively together than they do individually.

**Examples:**
- Ostrom’s 8 Core Design Principles
- The 12 Permaculture Principles
- A three-part pattern language for regenerative governance

MemePlexes are curated bundles of semantically reinforcing Memes.

### 1.4 MemeGroup

A **MemeGroup** is a curated, versioned collection of Memes stewarded by a group. It is the primary unit of **release** and **adoption**.

**Examples:**
- The working vocabulary of a DAO or movement
- A shared definition set for a digital commons
- A civic design pattern set for community governance

MemeGroups are published into `ReferenceSpaces` for reuse, remix, or uptake.

### 1.5 MemeFamily

A **MemeFamily** is a loose semantic grouping of related Memes, often sharing a conceptual root or domain.

**Examples:**
- Memes derived from the concept of “sovereignty”
- Variants of “life code” across different communities
- All distinctions involving “trust” in governance models

### 1.6 MemeStewardshipGroup

A **MemeStewardshipGroup** is a defined set of Memes that are **stewarded and released together** under shared governance within a `StewardshipSpace`.

It is the semantic unit of versioned release.

**Examples:**
- A shared vocabulary bundle curated by a DAO
- A core schema of governance terms
- A set of civic design patterns managed together

Each MemeStewardshipGroup exists within exactly one `StewardshipSpace`, and its releases are published to one or more `ReferenceSpaces`.

### 1.7 StewardshipSpace

A **StewardshipSpace** is a type of `AgentSpace` that serves as a **semantic commons and governance venue** for one or more `MemeStewardshipGroup`s.

It is a **SocialOrganism** with:
- A declared `LifeCode` (including purpose, values, and governance structure)
- One or more participating stewarding agents
- Authority over which versions of Memes are adopted or published

StewardshipSpaces manage:
- Pull requests and proposals
- Semantic versioning decisions
- Publishing of MemeGroups to ReferenceSpaces

**Examples:**
- A bioregional council managing place-based vocabulary
- An ontological working group stewarding a pattern library
- A translocal network co-governing a civic terminology framework

---

## 2. Core Holon Types and Relationships

### 2.1 Meme

Immutable unit of meaning.

Key Relationships:
- `StewardedIn → StewardedMemePool` (exactly one)
- `Includes → Meme` (0..n)
- `VersionOf → Meme` (optional)
- `DerivedFrom → Meme` (optional)
- `ClonedFrom → Meme` (optional, cross-space lineage)

### 2.2 MemeReference

Local use of a Meme.

Key Relationships:
- `RefersTo → Meme` (exactly one)
- `AnnotatedBy → Annotation` (0..n)
- `ContextualizedIn → AgentSpace` or `Agent`

### 2.3 DerivedMeme

A Meme created via additive-only derivation.

Key Relationships:
- `DerivedFrom → Meme`
- `AddedComponents → Meme`
- `VersionOf → Meme` (optional)

### 2.4 MemeGroup

Versioned set of Memes stewarded together.

Key Relationships:
- `Includes → Meme`
- `GovernedBy → StewardedMemePool`

### 2.5 StewardedMemePool

The stewarding agent for Memes.

Key Relationships:
- `Stewards → Meme`
- `Publishes → MemeGroup`
- `PublishedTo → ReferenceSpace`

---

## 3. Meaning Flow Model

### 3.1 Immutability

Once a Meme is published, it cannot be changed. All updates require a new `DerivedMeme` or `VersionOf`.

### 3.2 Read-Only Use

Memes can be reused through:
- `MemeReference`
- `Includes` composition
- Annotation without mutation

### 3.3 Lineage

Lineage is captured through:
- `DerivedFrom`
- `VersionOf`
- `ClonedFrom` (if cross-space)

---

## 4. Permitted Operations

### 4.1 Reference

Create `MemeReference` holons and attach annotations.

### 4.2 Annotation

Add interpretation, critique, commentary, or constraints.

### 4.3 Composition

Use `Includes → Meme` to compose new Memes or MemePlexes.

### 4.4 Derivation

Create `DerivedMeme` holons with additive changes only.

### 4.5 Version Proposal

Propose a new `VersionOf` an existing Meme to the stewarding group.

---

## 5. Derivation Constraints

### 5.1 Additive-Only Rule

`DerivedMeme`s may add relationships but cannot subtract or override.

### 5.2 Disagreement Handling

Disagreeing with a Meme? Compose a new one from primitives.

### 5.3 Transparency

All derivations must be lineage-explicit and traceable.

---

## 6. Semantic Versioning Rules

### 6.1 Meme-Level Versioning

- **Patch (`x.y.z`)** — Metadata, clarifications, non-normative notes
- **Minor (`x.y`)** — Additive meaning, extended scope
- **Major (`x`)** — Subtractive or redefinitional meaning

### 6.2 MemeGroup-Level Versioning

Release-level deltas:
- Patch: label, metadata, typos
- Minor: new Memes or updated versions
- Major: removals or incompatible replacements

Governance assigns versions during release.

---

## 7. Semantic Stability and Versioning Guarantees

### 7.1 Definitional Relationships

Some `HolonRelationships` are marked `is_definitional = true`.  
**Any change to the set of targets of a definitional relationship requires a new version of the source Meme.**

Examples:
- `Includes`
- `Specifies`
- `ClassifiedBy` (in some contexts)

### 7.2 Semantic Boundary

The **transitive closure** of definitional relationships defines the semantic boundary of a Meme version.

### 7.3 Permissive Relationships

Non-definitional relationships (e.g., `AnnotatedBy`, `HasExample`) may change without version bump.

### 7.4 Enforcement

- Enforced at governance and import-time
- Diff-based audits
- Ensures trustable referencing

### 7.5 Guarantees

- Stable meaning
- Predictable versioning
- Safe reuse
- Structural auditability

---

## 8. Stewardship Lifecycle (with Git-Like Workflow)

### 8.1 Checkout

Agents `Checkout` a Meme into their `ISpace`.

### 8.2 Commit

Changes are `Committed` locally—this creates new holons in `ISpace`.

### 8.3 Push to WeSpace (Branch)

Changes can be `Pushed` to a `WeSpace` for shared review.

### 8.4 Pull Request

A `PullRequest` submits a Meme to a `StewardshipSpace` for governance.

### 8.5 Release

Accepted Memes form a `MemeGroupReleaseCandidate`.  
Upon approval, it becomes an official version and is published to one or more `ReferenceSpaces`.

---

## 9. Local-First Usage

### 9.1 Sovereign Interaction

Agents can:
- Reference
- Annotate
- Remix
- Derive

…without requesting permission.

### 9.2 Non-Forking Usage

Local use via `MemeReference` does not fork or fragment Memes.

---

## 10. Distributed Uptake & Enquiries

### 10.1 MemeUpgradeEnquiry

Agents or Pools may issue an `Enquiry` offering a new version of a Meme or MemeGroup.

Other agents may `PromiseToAdopt`.

### 10.2 Git-Like Integration

- `Commit` in `ISpace`
- `Push` to `WeSpace`
- `PullRequest` to `StewardshipSpace`
- Enquiry invites distributed adoption

---

## 11. Shared Meaning Emergence

Shared meaning arises through:
- Saturated referencing
- MemeGroup convergence
- Alignment of `Annotation`s
- Common inclusion in memetic signatures

MAP enables convergence without coercion.

---

## 12. Protocol Guarantees

This protocol guarantees:
1. Immutable meaning artifacts
2. Structured lineage via derivation/versioning
3. Safe referencing via `MemeReference`
4. Stable governance over shared vocabularies
5. Semantic versioning and definitional audit
6. Pluralism, remixability, and divergence support

---

## 13. Git-Like Protocol Overlay

### 13.1 Role Mapping

| Git Term     | MAP Concept                           |
|--------------|---------------------------------------|
| Working Copy | `ISpace`                              |
| Branch       | `WeSpace` (`IsStewardshipSubSpaceOf`) |
| Origin Repo  | `StewardshipSpace`                    |
| Commit       | Local holon commit                    |
| Push         | Committed holons to WeSpace           |
| Pull Request | Submit Meme to StewardshipSpace       |
| Merge        | Governance selects `VersionOf`        |
| Clone        | Copy holon into new `HomeSpace`       |
| Fork         | Derive from prior Meme                |

### 13.2 Commit and Identity

Holons committed to `ISpace` are owned locally. Push and PR preserve identity until governance accepts, at which point:
- Meme is cloned into `StewardshipSpace`
- `HasPredecessor →` added
- Version assigned

### 13.3 Merge Without Conflicts

No merge conflicts due to separate `HolonId`s. Multiple candidates can be proposed, reviewed, and accepted independently.

---