# Related work and the retained contribution

This project asks for a better specimen of the **same unknown physical maximally entangled state**. The output promise matters when comparing it with protocols that produce a known standard Bell pair. The three-pair theorem allows different error strengths and axes across independent pairs with maximally mixed marginals and one common Bell eigenvector.

## The inherited two-copy obstruction

Zhao, Chen, Zhao, Zhu, Chiribella and Wang, *Power and limitations of distributed quantum state purification*, [Physical Review Letters **136**, 090203 (2026)](https://doi.org/10.1103/3bb1-pmtp), [arXiv:2509.08691v2](https://arxiv.org/html/2509.08691v2), establish the two-to-one LOCC no-go for the full unknown two-qubit maximally entangled orbit. Their Definition 1 and Corollary 4, together with supplemental Corollary 7 and the local/global depolarization relation, give the lower specimen threshold used here. A useful map is nondegrading on the entire target family and strictly improves at least one member. The present three-copy map improves every member throughout the entangled isotropic interval. The two-copy lower bound is credited to that paper.

Their Appendix K.4 reports numerical three-to-one protocols for four states in a common known Schmidt basis. That finite menu does not supply the continuous unknown-target, covariant map studied here.

## Local Schur filters are an established architecture

Ahmad et al., *Distillation of supersinglet states*, [arXiv:2509.20962v3](https://arxiv.org/html/2509.20962v3), use local three-qubit spin-half filtering, Schur decoding and classical postselection. Their Eqs. (9) and (21)–(25), and the intertwining identity (63), are close architectural antecedents. The Schur decomposition and its covariance are established tools.

Here the two spin-half multiplicities are combined with an imaginary relative phase. The [paired-filter calculation](../science/chirality.md) shows that every real choice in this rank-one family leaves isotropic target fidelity unchanged, whereas the conjugate chiral choices amplify it. The relative phase gives an operational same-target filter. Its sharp heterogeneous guarantee follows from the Pauli compression of this specific instrument.

## Cross-copy spin chirality is an established observable

Tulewicz, Bartkiewicz and Nori, *Spin chirality across quantum state copies detects hidden entanglement*, [arXiv:2605.14515v1](https://arxiv.org/html/2605.14515v1), connect partial-transpose moment corrections to cross-copy chirality correlators. Their main Eq. (2) and Supplement S2 supply controlled-SWAP measurement procedures for scalar entanglement diagnostics. This establishes a relevant physical-observable antecedent: cross-copy chirality itself is not introduced here. The retained present task is a quantum-output local instrument that selects conjugate chirality sectors and returns a more faithful specimen of the same unknown target. A scalar diagnostic alone does not supply that output map or its recurrence guarantee.

## Universal coding has a different output register

Rizzo, Girardi, Lami, Eisert and Leone, *Universal quantum coding*, [arXiv:2609.38038v2](https://arxiv.org/html/2609.38038v2), develop universal Schur–Weyl coding and distillation without tomography. Their Appendix C, Eq. (162) and Theorem 16, operate on permutation registers after tracing the unitary registers, and certify fidelity to a standard maximally entangled output. Local input rotations act on the discarded unitary registers. This is a substantial universal coding result, but its output promise does not directly preserve the unknown physical target required here. Our output is instead the fundamental spin-half representation carrying that target orientation.

Kálmán, Gábris, Jex and Kiss, *Universal, Unambiguous Concentration and Distillation of Bell pairs*, [Physical Review Letters **135**, 260202 (2025)](https://doi.org/10.1103/rcx1-w6j7), supply a four-pair unknown-pure-state concentration protocol and an eight-pair moderately mixed-state extension. Both target the known standard Bell state. Their operation count and stronger noise suppression address that output task. They do not directly imply the present three-pair same-target map. The indexed abstract of the subsequent Kinyó–Kiss–Kálmán [imperfect-operations study](https://arxiv.org/abs/2610.35699) concerns that protocol; a full comparison of its detailed hardware model is outside the present bounded literature review.

## Heterogeneous inputs and the choice of benchmark

Liu, Sun and Tong, *No universal LOCC entanglement purification*, [arXiv:2611.17809v1](https://arxiv.org/abs/2611.17809), consider independent, potentially different inputs across unrestricted families and require nondegradation against the best input. C. L. Liu, [*No-Go Theorems for Ordered Universal Entanglement Purification*, arXiv:2611.24603v1](https://arxiv.org/html/2611.24603v1), shows in Corollary 1 that even knowing the fidelity ordering and a floor cannot give strict best-input gain over a whole Bell-diagonal family. Proposition 2 gives best-input gain for a known Bell target on a more restricted isotropic family. That family consists of the pure target and a separated range of mixed-state fidelities.

The heterogeneous theorem keeps the target and the individual fidelities unknown and improves a common input floor. It accepts unequal fidelities and unaligned error axes throughout that floor class. An input that exceeds the common floor can still exceed the output fidelity. The exact envelope and the explicit orthogonal-axis witness belong to the three-pair chiral instrument. The [model](../science/model.md) describes the guarantee.

Yao et al., [*Protocols and Trade-Offs of Quantum State Purification*, arXiv:2404.01138v3](https://arxiv.org/html/2404.01138v3), use joint state-processing maps and include fixed Pauli and amplitude-damping examples in Section 2.3. The three-pair result here uses separated laboratory operations and optimization over a class whose strengths and error axes may differ among specimens.

## Joint purification and the first-order limit

Zhao et al., Appendix A, give cyclic symmetrization of the joint pairs. Their Eq. (A.5) already attains the leading infidelity factor `1/n` when both halves of every pair can be processed jointly. The [fixed-block result](../science/near-pure-limit.md) derives a directional lower bound from exact preservation of the physical target orbit, and reaches it with local block measurements for every block size of at least three. Appendix G of Zhao et al. separately supplies the inherited weighted-average bound that governs the two-pair worst-target limit.

Childs et al., [*Streaming quantum state purification*, Quantum **9**, 1603 (2025)](https://quantum-journal.org/papers/q-2025-01-21-1603/), use global swap-test recursion for unknown pure qudits and establish the corresponding final-error sample law. Here specimen cost is charged to two-party recurrence that keeps the physical target register. The construction uses familiar spin intertwiners and cyclic projection, with the project accounting for which virtual factor carries the target and which one is discarded.

[Scientific reading route](../science/README.md) · [Bibliography](references.bib)
