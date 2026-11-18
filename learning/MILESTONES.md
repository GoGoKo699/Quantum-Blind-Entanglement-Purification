# Thirty milestones: from a noisy pair to a blind purifier

This map follows the scientific task: improve a noisy entangled specimen while preserving its unknown physical target. It has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The background joins individual states, local operations and symmetry into the precise task. The narrative joins the chiral filter, its proof, recursive use and apparatus requirements into the complete contribution. The allocation gives the extra space to the new mechanism and its consequential resource and error qualifications.

The one educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition (2010), abbreviated **N&C** below. Chapter pointers identify foundations, not textbook proofs of the new results. The canonical project files supply the additional representation theory, calculations and resource arguments. Research-level imported results retain their primary citations. This is a common understanding map; it does not claim coverage of every technical lemma.

## Background/preliminaries: local objects to the complete task

### M01 — One physical qubit and its description

- **Phase:** Background/preliminaries.
- **Central question:** What is the difference between a physical qubit and a classical description of its state?
- **Understanding target:** Explain how a state vector or density operator describes preparation and measurement statistics, while an available specimen need not come with that description.
- **Dependencies and story role:** No earlier milestone. Establish the objects that the source distributes and the laboratories process.
- **Conceptual connection:** The target can be a valid physical input even when its orientation is unavailable to the classical controller.
- **Source pointers:** N&C Ch. 2, quantum states and measurements; [source and target model](../science/model.md).

### M02 — A pair shared between laboratories

- **Phase:** Background/preliminaries.
- **Central question:** What makes an entangled pair a joint resource rather than two independently described local qubits?
- **Understanding target:** Relate the tensor-product description, reduced states and joint correlations; explain why a maximally entangled pure pair has maximally mixed local states.
- **Dependencies and story role:** M01. Extend the local object to the distributed specimen that the task concerns.
- **Conceptual connection:** Each laboratory can manipulate its half, but neither local half by itself specifies the shared pure target.
- **Source pointers:** N&C Ch. 2, composite systems and Schmidt decomposition; Ch. 12, entanglement; [model](../science/model.md).

### M03 — An unknown maximally entangled target

- **Phase:** Background/preliminaries.
- **Central question:** Which uncertainty does the word “blind” describe here?
- **Understanding target:** Explain the locally rotated Bell-state family and distinguish one fixed unknown target from a target that changes between specimens.
- **Dependencies and story role:** M01–M02. Give the unknown object a precise family and hold it fixed across the source stream.
- **Conceptual connection:** A universal fixed circuit must transport the unknown local rotation into its output rather than use a target-dependent correction.
- **Source pointers:** N&C Ch. 2, unitary transformations and composite systems; [source and output conventions](../science/model.md).

### M04 — Isotropic noise and a quality parameter

- **Phase:** Background/preliminaries.
- **Central question:** How does the source model separate uncertainty about the target from noise around it?
- **Understanding target:** Interpret an isotropic pair as a mixture of its target projector and the completely mixed two-qubit state; distinguish visibility from knowledge of orientation.
- **Dependencies and story role:** M02–M03. Add the exact noise promise under which purification is established.
- **Conceptual connection:** All specimens can share one unknown target while having different visibilities; orientation and quality are separate variables.
- **Source pointers:** N&C Ch. 8, quantum noise and operations; [isotropic source](../science/model.md); [unequal-quality inputs](../science/algebra.md).

### M05 — Fidelity and the entangled interval

- **Phase:** Background/preliminaries.
- **Central question:** What quantity must increase for this purification task to succeed?
- **Understanding target:** Use squared overlap with the same pure target as the repository's fidelity convention; connect the visibility threshold of one third to fidelity one half and to the two-qubit separability boundary.
- **Dependencies and story role:** M02–M04. Turn “better specimen” into a comparison with a specified target and regime.
- **Conceptual connection:** Distinguishing the squared-overlap convention prevents confusing a reported gain with the square-root fidelity convention used in parts of the anchor.
- **Source pointers:** N&C Ch. 9, fidelity; Ch. 12, entanglement; [fidelity convention and partial-transpose argument](../science/model.md).

### M06 — A measurement can retain a quantum output

- **Phase:** Background/preliminaries.
- **Central question:** How can a laboratory obtain a classical record while leaving a useful qubit?
- **Understanding target:** Explain a Kraus branch, its probability and its normalized output; distinguish an accepted branch from the complete instrument that also records rejection.
- **Dependencies and story role:** M01 and M05. Supply the language of heralded quantum processing before constructing the filter.
- **Conceptual connection:** A postselected output has both a conditional quality and a success probability; neither specifies the whole experiment alone.
- **Source pointers:** N&C Ch. 2, generalized measurements; Ch. 8, operator-sum representation; [local instrument](../science/protocol.md); [flagged channels](../science/robustness.md).

### M07 — Local operations and classical comparison

- **Phase:** Background/preliminaries.
- **Central question:** Which resources may the separated laboratories use to process their pairs?
- **Understanding target:** Explain why local circuits, local measurements and communicated outcome labels form an LOCC protocol, and identify where source specimens are consumed.
- **Dependencies and story role:** M02 and M06. Put the measurement model into the distributed operational setting.
- **Conceptual connection:** Comparing records can coordinate acceptance without a quantum gate between laboratories or extra shared entanglement.
- **Source pointers:** N&C Ch. 12, entanglement processing; [allowed operations](../science/model.md); [acceptance rule](../science/protocol.md).

### M08 — Covariance as target transport

- **Phase:** Background/preliminaries.
- **Central question:** How can one fixed operation preserve every unknown orientation in a continuous family?
- **Understanding target:** Read a covariance identity as saying that a common input rotation becomes the corresponding output rotation; distinguish it from estimating that rotation.
- **Dependencies and story role:** M03 and M06–M07. Introduce the symmetry condition that makes blindness provable.
- **Conceptual connection:** Exact covariance can move a canonical-target calculation to every target in the family while retaining a physical quantum output.
- **Source pointers:** N&C Ch. 2, unitary transformations; [generator identities and covariance](../science/protocol.md); [output meaning](../science/interpretation.md).

### M09 — Three specimens at one laboratory

- **Phase:** Background/preliminaries.
- **Central question:** How does having three local qubits create degrees of freedom absent from one qubit?
- **Understanding target:** Distinguish the three source-pair labels from the Alice–Bob division; interpret the local eight-dimensional tensor-product space and collective rotations.
- **Dependencies and story role:** M02–M03 and M08. Build the local block on which the filter acts.
- **Conceptual connection:** Reordering tensor factors for a calculation changes notation, not the physical locality of the protocol.
- **Source pointers:** N&C Ch. 2, tensor products; [three-input instrument and tensor order](../science/protocol.md); [basis convention](../science/implementation.md).

### M10 — Representation and multiplicity carry different information

- **Phase:** Background/preliminaries.
- **Central question:** What can be measured without discarding the degree of freedom carrying the unknown target?
- **Understanding target:** Explain the three-qubit decomposition into one spin-three-halves sector and two spin-half copies; distinguish the spin representation from the label identifying its repeated copies.
- **Dependencies and story role:** M08–M09. Identify the symmetry-compatible workspace that the new operation will exploit.
- **Conceptual connection:** The unknown rotation acts on the retained spin qubit, while the multiplicity label can be filtered independently of that rotation.
- **Source pointers:** N&C Ch. 2 supplies tensor-product and unitary foundations; the additional decomposition and intertwiners are supplied in [protocol](../science/protocol.md), with architectural attribution in [related work](../references/RELATED_WORK.md).

### M11 — Conditional improvement and charged failures

- **Phase:** Background/preliminaries.
- **Central question:** Why is a better accepted pair not yet a complete resource guarantee?
- **Understanding target:** Separate per-attempt fidelity, per-attempt success, the mean consumption of repeated attempts and a deterministic input cap.
- **Dependencies and story role:** M05–M07. Join output quality to the cost of obtaining that output before recursive purification is introduced.
- **Conceptual connection:** Failed and aborted preparations still consume specimens; a small elementary block need not have high yield at high requested accuracy.
- **Source pointers:** N&C Ch. 2, outcome probabilities; Ch. 12, entanglement processing; [finite-budget definitions](../science/resources.md); [interpretation](../science/interpretation.md).

### M12 — The complete blind-purification question

- **Phase:** Background/preliminaries.
- **Central question:** What precisely would a construction have to establish to solve this task?
- **Understanding target:** State the fixed common unknown target, isotropic source promise, local operations, retained same-target output, heralded gain and charged resources together; distinguish that task from producing a known standard Bell pair.
- **Dependencies and story role:** M01–M11. Integrate the background into one operational question rather than another isolated prerequisite.
- **Conceptual connection:** The target promise, noise promise, output register and success convention determine which constructions and no-go theorems actually apply.
- **Source pointers:** N&C Chs. 8, 9 and 12 supply operations, quality and entanglement foundations; [model and exact claims](../science/model.md); [model-level literature comparisons](../references/RELATED_WORK.md).

## Narrative/innovation: a local phase to the complete construction

### M13 — Decoding either spin-half copy

- **Phase:** Narrative/innovation.
- **Central question:** How do the explicit real maps turn a three-qubit sector into one physical output qubit?
- **Understanding target:** Explain what the two real intertwiners select, why their rows are orthonormal and how their collective-spin identities certify the output transformation.
- **Dependencies and story role:** M09–M10 and M12. Start the construction with its local maps and their algebraic contract.
- **Conceptual connection:** The matrices realize the representation–multiplicity separation concretely; their covariance is proved by generator identities rather than by sampled targets.
- **Source pointers:** N&C Chs. 2 and 8, isometries and operation elements; [explicit intertwiners](../science/protocol.md); [exact symbolic checks](../verification/check_exact.py).

### M14 — Choosing a chiral multiplicity basis

- **Phase:** Narrative/innovation.
- **Central question:** What does an imaginary relative phase change when two multiplicity copies carry the same spin representation?
- **Understanding target:** Explain the conjugate combinations of the real intertwiners, their orthogonal supports and their opposite eigenphases under a three-cycle of specimens.
- **Dependencies and story role:** M10 and M13. Identify the new operation inside the inherited Schur architecture.
- **Conceptual connection:** A relative phase in multiplicity changes the filtering effect while retaining the same covariance of the physical spin output.
- **Source pointers:** N&C Ch. 2, phases and orthogonal measurement; [chiral maps and specimen permutations](../science/protocol.md); [phase mechanism](../science/chirality.md).

### M15 — Completing the physical instrument

- **Phase:** Narrative/innovation.
- **Central question:** How do the chiral maps become a valid local experiment with explicit rejection?
- **Understanding target:** Combine the two rank-two success projectors with the symmetric-sector reject projector; explain why opposite chirality labels are accepted and why both accepted records count toward success.
- **Dependencies and story role:** M06–M07 and M13–M14. Assemble the local pieces into an LOCC attempt.
- **Conceptual connection:** The complete outcome inventory makes the map physically implementable and prevents losing a factor of two in its announced success probability.
- **Source pointers:** N&C Ch. 8, complete operator-sum maps; [local instrument and acceptance](../science/protocol.md); [measurement-bit realization](../science/implementation.md).

### M16 — Preserving every unknown physical target

- **Phase:** Narrative/innovation.
- **Central question:** Why does this particular accepted map preserve the target rather than conjugate it or replace it?
- **Understanding target:** Combine each intertwiner's covariance with the product acceptance rule; explain how independent local input rotations pass to the two retained output qubits without target-dependent correction.
- **Dependencies and story role:** M08, M12 and M15. Lift the local construction to the global blindness guarantee.
- **Conceptual connection:** Covariance also reduces the remaining output calculation to the canonical target, without making that target known to the apparatus.
- **Source pointers:** N&C Chs. 2 and 8, unitary channels; [exact covariance](../science/protocol.md); [same-target interpretation](../science/interpretation.md).

### M17 — Two scalar traces determine the output

- **Phase:** Narrative/innovation.
- **Central question:** Why are success and target-overlap numerator enough to determine the whole accepted isotropic state?
- **Understanding target:** Explain the symmetry that fixes the output's form and interpret the exact contraction table for zero, one, two or three pure factors.
- **Dependencies and story role:** M04–M06 and M16. Connect the physical map to an exact, checkable output calculation.
- **Conceptual connection:** Multilinearity joins finitely many pure/mixed contractions into a formula valid over the full visibility range; a fidelity sample alone would not give that operator identity.
- **Source pointers:** N&C Ch. 8, linear quantum operations; [contraction table and full operator](../science/algebra.md); [entrywise verifier](../verification/check_exact.py).

### M18 — Gain over the entire entangled isotropic interval

- **Phase:** Narrative/innovation.
- **Central question:** Which inputs improve, and how much does one accepted attempt achieve?
- **Understanding target:** Relate the exact visibility update, success probability and fidelity gain; explain the fixed separable boundary, preservation of pure input and strict gain throughout the noisy entangled interval.
- **Dependencies and story role:** M05, M11 and M17. Turn the output identity into the central purification theorem.
- **Conceptual connection:** The example with input fidelity 0.70, accepted fidelity approximately 0.785714 and success 0.224 displays both the improvement and its heralded cost.
- **Source pointers:** N&C Ch. 9, fidelity; [equal-visibility theorem and endpoints](../science/algebra.md); [worked elementary example](../science/model.md).

### M19 — What the chiral choice optimizes

- **Phase:** Narrative/innovation.
- **Central question:** Why do real multiplicity filters give no gain while the chiral choices do?
- **Understanding target:** Interpret the chirality parameter of a general paired rank-one multiplicity filter, its zero value for real coefficients and the monotone fidelity gain up to its chiral maximum.
- **Dependencies and story role:** M14 and M18. Isolate the mechanism from generic Schur projection and identify the exact optimization domain.
- **Conceptual connection:** Maximization within this paired-filter family explains a consequential phase choice; it supplies no all-LOCC fidelity or success optimum.
- **Source pointers:** N&C Chs. 2 and 8, complex amplitudes and operations; [full paired-filter family and optimization](../science/chirality.md); [architectural and chirality antecedents](../references/RELATED_WORK.md).

### M20 — Why the specimen onset is three

- **Phase:** Narrative/innovation.
- **Central question:** What turns a three-input construction into a sharp minimum block-size statement?
- **Understanding target:** Combine the inherited general two-copy no-go with this three-copy achiever under the same unknown-target promise; distinguish heralded specimen onset from minimum coherent memory and always-output purification.
- **Dependencies and story role:** M12 and M18–M19. Place the constructive mechanism against the exact obstruction it crosses.
- **Conceptual connection:** The lower bound is an imported research theorem with a model-specific scope, while the present operation supplies the matching constructive endpoint.
- **Source pointers:** N&C Ch. 12 supplies entanglement-processing context; [threshold and cited Zhao et al. theorem](../science/model.md); [attribution and comparison](../references/RELATED_WORK.md).

### M21 — Amplifying a floor when qualities differ

- **Phase:** Narrative/innovation.
- **Central question:** What guarantee survives if the three source pairs have unequal and unknown qualities?
- **Understanding target:** Explain the exact symmetric-polynomial output and coordinatewise monotonicity; use them to distinguish amplification of a certified common floor from improvement over the best input.
- **Dependencies and story role:** M04, M17–M18. Remove equality of qualities without dropping the restricted source model.
- **Conceptual connection:** The circuit remains unchanged, while the floor theorem enables later recursion on outputs whose actual visibilities need not be known.
- **Source pointers:** N&C Ch. 8, linearity; [unequal-quality map and monotonicity proof](../science/algebra.md); [best-input comparison boundary](../references/RELATED_WORK.md).

### M22 — Conditioning on a classically varying source

- **Phase:** Narrative/innovation.
- **Central question:** Why can some classical quality correlations be allowed while marginal fidelity floors are insufficient?
- **Understanding target:** Explain a mixture of global product inputs with a pointwise floor in every latent component, and why acceptance reweights components without violating that floor.
- **Dependencies and story role:** M06 and M21. State the source promise that remains stable after the protocol observes records.
- **Conceptual connection:** The conditional product-mixture structure permits recursive regrouping; arbitrary quantum-correlated errors or drifting targets do not follow from this argument.
- **Source pointers:** N&C Chs. 2 and 8, mixtures and selective operations; [classical-mixture extension](../science/algebra.md); [conditional-history promise](../science/resources.md).

### M23 — Recursion toward the same pure target

- **Phase:** Narrative/innovation.
- **Central question:** How can accepted outputs become inputs without learning their orientation or actual quality?
- **Understanding target:** Explain successful purification levels, increasing visibility floors and convergence to purity; distinguish conditional convergence from the probability and cost of completing a level.
- **Dependencies and story role:** M18 and M21–M22. Extend the elementary mechanism into a reusable construction.
- **Conceptual connection:** Covariance preserves the target and the floor theorem preserves the input promise at each successful level; failures still have to be charged.
- **Source pointers:** N&C Ch. 12, recursive entanglement processing; [fixed points and convergence](../science/algebra.md); [level construction](../science/resources.md).

### M24 — From an expected cost to a hard budget

- **Phase:** Narrative/innovation.
- **Central question:** How can one promise finite input consumption and a specified probability of obtaining an output?
- **Understanding target:** Explain the conditional expected-cost recurrence, the Markov bound for one capped run and the cap-and-restart guarantee, including all rejected children and aborted runs.
- **Dependencies and story role:** M11 and M22–M23. Turn conditional purification into a complete finite experiment.
- **Conceptual connection:** A uniform conditional failure bound composes across runs even with the allowed classical quality dependence; no independence of hidden qualities is silently added.
- **Source pointers:** N&C Ch. 2 supplies probability conventions; the conditional-expectation and cap proofs are supplied in [finite resources](../science/resources.md); [independent cost-distribution check](../verification/check_resources.py).

### M25 — Accuracy has a specimen cost

- **Phase:** Narrative/innovation.
- **Central question:** What does approaching a pure target cost in this particular recursive architecture?
- **Understanding target:** Connect the late-stage threefold infidelity contraction, success approaching one half and sixfold mean cost per level; interpret the achieved accuracy exponent and its dependence on the initial floor.
- **Dependencies and story role:** M18 and M23–M24. Relate the local mechanism to its global efficiency and the conservative numerical budget.
- **Conceptual connection:** Three-copy onset coexists with a large high-fidelity resource bill; the achieved exponent establishes neither optimality nor positive asymptotic yield.
- **Source pointers:** N&C Ch. 12 provides distillation context; [accuracy scaling and finite example](../science/resources.md); [resource interpretation](../science/interpretation.md).

### M26 — A fixed elementary-gate implementation

- **Phase:** Narrative/innovation.
- **Central question:** How does the abstract local filter become a specified circuit on the received qubits?
- **Understanding target:** Explain the orthonormal-row completion, two measured status/chirality bits, retained spin qubit and deterministic QR/two-level synthesis; interpret the emitted CNOT and arbitrary one-qubit counts.
- **Dependencies and story role:** M13–M16. Connect the mathematical instrument to a finite local apparatus.
- **Conceptual connection:** The gate sequence is independent of the unknown target and actual visibility; its non-Clifford rotations need precision and possible discrete-library synthesis costs.
- **Source pointers:** N&C Ch. 4, controlled operations and universal circuits; [matrix, compiler and counts](../science/implementation.md); [full-unitary circuit check](../verification/check_circuit.py).

### M27 — Storage, messages and time across the whole run

- **Phase:** Narrative/innovation.
- **Central question:** Which resources beyond native pairs are needed by the finite recursive protocol?
- **Understanding target:** Explain depth-first storage, pathwise register accounting, the deterministic attempt cap, communicated outcome bits and serial elapsed-time bound.
- **Dependencies and story role:** M24–M26. Join the elementary implementation to the complete preparation schedule.
- **Conceptual connection:** Counting live registers and discarded pairs bounds operations even on failed trajectories; the supplied quality-floor promise and apparatus calibration remain separate inputs.
- **Source pointers:** N&C Chs. 4 and 12 provide circuit and distributed-processing context; [storage, communication and time](../science/resources.md); [gate model](../science/implementation.md).

### M28 — Robustness before and after acceptance

- **Phase:** Narrative/innovation.
- **Central question:** Why should apparatus errors be bounded on complete flagged instruments before conditioning?
- **Understanding target:** Explain half trace distance, complete-instrument half-diamond error and the success-denominator conditioning bound; identify a sufficient error budget for one-attempt fidelity gain.
- **Dependencies and story role:** M05–M06, M18 and M26. Add physical imperfections without assuming they preserve isotropic output form.
- **Conceptual connection:** Postselection can magnify deviations, so a small unnormalized error and a high ideal fidelity do not alone certify the accepted state's quality.
- **Source pointers:** N&C Ch. 9, distance measures; Ch. 8, complete channels; [conditioning lemma and one-attempt error bound](../science/robustness.md).

### M29 — Finite precision for a complete adaptive experiment

- **Phase:** Narrative/innovation.
- **Central question:** How can imperfect recursive use be bounded when its intermediate states need not stay isotropic?
- **Understanding target:** Explain the complete-experiment hybrid argument, deterministic call cap and allocation of source, storage, gate and classical errors; distinguish uniform conditional channel bounds from arbitrary hidden-memory noise.
- **Dependencies and story role:** M24 and M26–M28. Compose the apparatus requirements with the finite success and fidelity guarantees.
- **Conceptual connection:** Comparing the full actual and ideal experiments before conditioning avoids applying the ideal visibility recurrence to uncontrolled noisy states; fixed adverse final noise still imposes a purity floor.
- **Source pointers:** N&C Chs. 8–9, channels and distinguishability; [adaptive error budget, gate precision and final-noise example](../science/robustness.md); [finite attempt cap](../science/resources.md).

### M30 — The contribution as one operational account

- **Phase:** Narrative/innovation.
- **Central question:** What has the complete construction established, and which stronger conclusions remain unsupported?
- **Understanding target:** Explain the path from chiral multiplicity filtering to same-target gain, sharp heralded specimen onset, unequal-quality floor amplification, finite-budget preparation and explicit implementation requirements; separate those results from hardware advantage and unrestricted-noise or all-LOCC optimality claims.
- **Dependencies and story role:** M12–M29. Integrate the narrative from local phase choice to the global scientific proposition and its boundaries.
- **Conceptual connection:** The value is a constructive target-preserving processor with a charged finite account; known Bell-channel calibration, memory optimality and positive asymptotic yield are separate questions.
- **Source pointers:** N&C Chs. 8, 9 and 12 support the foundational language; [scientific reading route](../science/README.md), [interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md) and [verification boundary](../verification/README.md) connect the full account.

[Repository](../README.md) · [Scientific reading route](../science/README.md)
