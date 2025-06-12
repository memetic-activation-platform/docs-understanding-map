## The MAP Choreographer

The **Choreographer** is the MAP’s native coordination engine. It manages the invocation and sequencing of modular dances across agents, spaces, and roles using **declarative [Dance Flows](glossary.md#dance-flow)** that respect sovereignty, promise boundaries, and contextual cues.

Each dance performs a single task and emits a completion signal. The Choreographer listens for these signals and, based on the active flow specification and local context, invokes the next appropriate step. By keeping sequencing logic outside of individual dances, MAP enables complex behaviors to be composed from simple, intelligible parts.

---

### Dance Flows

A **Dance Flow** is a named, shareable specification that defines the sequence of steps — individual dances — that make up a collaborative process. Dance Flows are:

- **Composable**: Built from reusable, single-purpose dances
- **Context-aware**: Adapt their path based on agent state, space governance, or prior actions
- **Membrane-respecting**: Operate within or across Agent Spaces with full visibility of boundaries
- **Promise-aligned**: Flows often represent the unfolding of a Promise Weave

Rather than embedding sequencing logic inside each dance, MAP separates it out into the Choreographer layer. This dramatically simplifies each dance while enabling rich, adaptive flows to emerge.

---

### How It Works

1. **Trigger**: A signal is emitted — a promise is fulfilled, a role is activated, a time threshold is reached.
2. **Evaluation**: The Choreographer assesses the active Dance Flow, current state, and membrane context.
3. **Invocation**: It formally requests the next dance in the flow to execute.
4. **Completion**: The dance completes and emits a signal, triggering the next step.
5. **Continuation or Termination**: The flow proceeds, branches, pauses, or concludes, based on its logic.

Each invocation is a **real request**, not a loose suggestion. The agent or space receiving the request is expected to respond — though the MAP always honors boundaries and role agreements.

---

### Example Use Cases

- A regenerative land commons uses a Dance Flow for onboarding new stewards — including invitation, agreement, orientation, and role activation.
- A bioregional network launches a seasonal review flow across nested Agent Spaces, each contributing insights and adjustments.
- A commons decision-making flow choreographs proposal initiation, round-robin input, consent checking, and final commitment.
- The MAP platform itself uses Dance Flows to manage offer acceptance, Agreement instantiation, and space access configuration.

---

### Integration and Interactions

#### Ecosystem Connections

- **Global Meme Pool**: Common Dance Flows (e.g., consent decision cycles) may be curated and versioned as reusable cultural patterns, discoverable via the Global Meme Pool.

- **Visualizer Commons**: Dance Flows do not rely on a single MAP-defined interface. The Visualizer ecosystem invites HX designers and developers to imagine and contribute diverse, no-code visual languages — enabling non-technical agents to define and evolve their own coordination flows in ways that are intuitive, expressive, and culturally aligned.

- **Global Service Registry**: The Choreographer helps fulfill promises embedded in service offerings. It supports Agreement honoring and protocol completion by sequencing Dance Flows associated with GSR-registered services. It can also be used by MAP itself to manage offer acceptance, instantiate Agreements and Agreement Spaces, and handle service (i.e., dance) requests — all while enforcing membrane boundaries and roles.

- **Empowered Agents Holarchy**: The Choreographer plays a critical role in shaping agency at every level — by orchestrating join processes, managing role activation, and weaving governance dance flows. It helps Agent Spaces evolve into living, trustable holarchies.

#### Core MAP Interactions

- **Agent Spaces**: The Choreographer runs within and across spaces, always respecting membrane permissions and role boundaries.
- **Promises**: Many Dance Flows are structured as sequences of promises — either formal or informal.
- **Notification Center**: Requests, reminders, or updates generated during flows are routed according to each agent’s notification policies and preferences.

#### Additional Capabilities

- **Hybrid Dance Steps**: Dance Flows may include both agent-performed and system-performed steps — allowing automation to be composed alongside human action in a coherent and relationally aligned way.

---

### Summary

The Choreographer brings coordination intelligence to the MAP —  
not by controlling agents, but by enabling **rich flows to unfold** through clear structure, lightweight signaling, and deep contextual awareness.

It doesn’t script behavior.  
It sequences **relational steps** that respect each agent’s sovereignty —  
and in doing so, makes distributed cooperation not only possible, but graceful.

Like the DAHN for lived experience and self-describing holons for meaning,  
**agent-defined Dance Flows** allow coordination logic itself to evolve —  
unbound by the constraints or assumptions of the MAP’s original designers.  
They are an invitation to co-create new rhythms of collaboration,  
as the needs of life and context demand.