# **Glossary: Organ (MAP)**
### *Version 4 — With caching, open-ended organ ecosystem, and extension rules*

### **Organ (MAP)**
**A MAP Organ is a stewarded, versioned bundle of HolonTypes and Dances that a Space may adopt to expand its internal functional capacities.**  
When embodied, an Organ becomes part of a Space’s bio-socio-techno organism, extending what it can perceive, understand, coordinate, commit, and accomplish.

---

# **1. Formal Structure: What an Organ Is**

An Organ is formally defined by an **Organ Descriptor**, a holon stored in exactly one **Stewardship Space**. The Descriptor:

- **Consists of → HolonTypes** (schema, properties, relationships, dances)
- Defines the Organ’s **behavioral affordances** (DanceDescriptors)
- Is **versioned** using semantic versioning
- Is **never copied** into other Spaces as part of embodiment
- **May be locally cached** like any holon, giving the appearance of a copy but *not* altering provenance, mutability, or ownership

Caching enables offline or intermittent operation without violating MAP’s principle that each holon has exactly one Home Space.  
HolonReferences ensure that the Organ Descriptor’s authoritative definition always resides in its Stewardship Space.

---

# **2. Organ Embodiment (Expression Inside a Space)**

A Space adopts an Organ by:

1. Installing a **HolonReference** to the Organ Descriptor
2. Configuring required **SpaceProxies / TrustChannels** so the Space can resolve all $refs
3. Beginning to use the Organ’s HolonTypes and Dances within its own membrane

The result is an:

### **Organ Embodiment**
The **operational expression** of an Organ inside a specific Space.  
This is not a cloned instance; it is the Space’s **living usage** of the Organ’s definition.

Organ Embodiments arise purely through referencing, caching, and local use — never through duplication of the Organ Descriptor.

---

# **3. The Organ Life Cycle: Stewardship → Connection → Agreement Spaces**

Organ creation, discovery, matching, and embodiment take place across three different Spaces:

---

## **3.1. Stewardship Space**
The Organ’s **development and governance home**.

- Maintains the Organ Descriptor
- Evolves it through branches, merges, and version releases
- Contains a small membership (stewards and collaborators)
- Functions like a development repository for meaning and behavior

This is where the Organ **lives and evolves**.

---

## **3.2. Connection Space**
A large, high-reach Space where **inquiries** are placed and matched via the **Connect Organ**.

Organ stewards publish **Service inquiries** describing:

- commitments required
- capabilities offered
- access permissions and roles
- Life Code assertions
- version upgrade policies

Prospective adopters place their own inquiries; matching occurs through the **Promise Weave Protocol**.

> **Note:**  
> The *Discover Organ* discovers **memes** in the global meme pool — not Organs.  
> Organ offers are discovered exclusively through **Connection Spaces**.

Connection Spaces are MAP’s **service registry and matching infrastructure**.

---

## **3.3. Agreement Space**
When a match succeeds, a dedicated **Agreement Space** is created containing only:

- the adopting Space
- the Organ’s stewarding agents
- any additional roles named in the agreement

Inside this Agreement Space:

- The Organ embodiment is formalized
- Information access permissions are established
- TrustChannels are provisioned
- Responsibilities and flows of vital capital are defined
- Upgrade policies (major/minor/patch) are negotiated

The Organ becomes fully embodied only within this Agreement Space.

---

# **4. MAP Core Organs and the Open-Ended Organ Ecosystem**

The MAP Stewardship Space maintains a set of **Core Organs**, which every new agent receives at onboarding.  
These include foundational subsystems such as the Connect, Sense, Discover, Dispatch, Sustain, and Flow/Choreograph Organs.

But MAP’s organ ecosystem is **open and extensible**:

- Any Stewardship Space may publish new Organs into Connection Spaces
- Any agent or organization may become an Organ developer or steward
- Organs are **Commons artifacts**, not proprietary apps

This ensures MAP remains **evolutionary** and **commons-centered**, not a closed vendor-controlled platform.

---

# **5. Extending Organs: A Commons-Friendly Model**

Contributed Organs may **extend** existing Organs — including MAP Core Organs.

Extensions may:

- add new HolonTypes
- add properties to existing HolonTypes
- add relationships
- add new dances or variations of existing dances

Extensions may **not**:

- remove properties
- remove relationships
- remove dances
- redefine prior dance semantics

This ensures:

- backward compatibility
- stable meaning across the network
- preservation of shared behaviors
- avoidance of fragmentation

Organs grow like biological organs: elaborating and branching, never breaking existing anatomy.

---

# **6. Behavioral Role of Organs**

Inside a Space, Organs serve as:

- **metabolic subsystems** (Sustain Organ)
- **sensors** (Sense Organ)
- **coordination mechanisms** (Connect Organ)
- **meaning-processing modules** (Discover Organ)
- **execution orchestrators** (Flow, Dispatch)

A Space does not “run” Organs.  
A Space **grows** Organs as internal components of its own living identity.

---

# **7. Summary: The Essence of an Organ**

**An Organ is:**

- a stewarded, versioned, reference-based subsystem
- defined in a Stewardship Space
- offered via inquiries in large Connection Spaces
- adopted through negotiated Agreements
- embodied without duplication
- cached locally for resilience
- extensible through additive evolution
- a Commons artifact, not a proprietary silo

**Organs form the internal anatomy of MAP Spaces — the organelles and organs of the digital-social organism.**