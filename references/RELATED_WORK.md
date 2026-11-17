# Related work and the retained contribution

This project asks for a better specimen of the **same unknown physical maximally entangled state**. The output promise matters when comparing it with protocols that produce a known standard Bell pair. The construction assumes isotropic noise about a common fixed target; its quality-floor extension still requires that common target and a pointwise promise on product-source components.

## The inherited two-copy obstruction

Zhao, Chen, Zhao, Zhu, Chiribella and Wang, *Power and limitations of distributed quantum state purification*, [Physical Review Letters **136**, 090203 (2026)](https://doi.org/10.1103/3bb1-pmtp), [arXiv:2509.08691v2](https://arxiv.org/html/2509.08691v2), establish the two-to-one LOCC no-go for the full unknown two-qubit maximally entangled orbit. Their Definition 1 and Corollary 4, together with supplemental Corollary 7 and the local/global depolarization relation, give the lower specimen threshold used here. A useful map is nondegrading on the entire target family and strictly improves at least one member. The present three-copy map improves every member throughout the entangled isotropic interval. The two-copy lower bound is credited to that paper.

Their Appendix K.4 reports numerical three-to-one protocols for four states in a common known Schmidt basis. That finite menu does not supply the continuous unknown-target, covariant map studied here.

## Local Schur filters are an established architecture

Ahmad et al., *Distillation of supersinglet states*, [arXiv:2509.20962v3](https://arxiv.org/html/2509.20962v3), use local three-qubit spin-half filtering, Schur decoding and classical postselection. Their Eqs. (9) and (21)–(25), and the intertwining identity (63), are close architectural antecedents. The Schur decomposition and its covariance are established tools.

Here the two spin-half multiplicities are combined with an imaginary relative phase. The [paired-filter calculation](../science/chirality.md) shows that every real choice in this rank-one family leaves isotropic target fidelity unchanged, whereas the conjugate chiral choices amplify it. The retained addition is this operational filter, its exact unknown-target gain, and its unequal-quality floor guarantee. The comparison does not claim that Schur projection itself is new, or that the chiral choice is globally optimal over LOCC.

## Cross-copy spin chirality is an established observable

Tulewicz, Bartkiewicz and Nori, *Spin chirality across quantum state copies detects hidden entanglement*, [arXiv:2605.14515v1](https://arxiv.org/html/2605.14515v1), connect partial-transpose moment corrections to cross-copy chirality correlators. Their main Eq. (2) and Supplement S2 supply controlled-SWAP measurement procedures for scalar entanglement diagnostics. This establishes a relevant physical-observable antecedent: cross-copy chirality itself is not introduced here. The retained present task is a quantum-output local instrument that selects conjugate chirality sectors and returns a more faithful specimen of the same unknown target. A scalar diagnostic alone does not supply that output map or its recurrence guarantee.

## Universal coding has a different output register

Rizzo, Girardi, Lami, Eisert and Leone, *Universal quantum coding*, [arXiv:2609.38038v2](https://arxiv.org/html/2609.38038v2), develop universal Schur–Weyl coding and distillation without tomography. Their Appendix C, Eq. (162) and Theorem 16, operate on permutation registers after tracing the unitary registers, and certify fidelity to a standard maximally entangled output. Local input rotations act on the discarded unitary registers. This is a substantial universal coding result, but its output promise does not directly preserve the unknown physical target required here. Our output is instead the fundamental spin-half representation carrying that target orientation.

Kálmán, Gábris, Jex and Kiss, *Universal, Unambiguous Concentration and Distillation of Bell pairs*, [Physical Review Letters **135**, 260202 (2025)](https://doi.org/10.1103/rcx1-w6j7), supply a four-pair unknown-pure-state concentration protocol and an eight-pair moderately mixed-state extension. Both target the known standard Bell state. Their operation count and stronger noise suppression address that output task. They do not directly imply the present three-pair same-target map. The indexed abstract of the subsequent Kinyó–Kiss–Kálmán [imperfect-operations study](https://arxiv.org/abs/2610.35699) concerns that protocol; a full comparison of its detailed hardware model is outside the present bounded literature review.

## Quality variation does not remove the source promise

Liu, Sun and Tong, *No universal LOCC entanglement purification*, [arXiv:2611.17809v1](https://arxiv.org/abs/2611.17809), consider universal finite-input purification across unrestricted entangled families, including potentially different inputs and a guarantee against the best input. The present method assumes a common target and restricted isotropic noise, and amplifies a certified common floor. It can perform worse than the best member of an unequal-quality batch. These distinct promises prevent an implication or contradiction based only on the word “universal.”

## Interpretation of the advance

The method crosses the inherited two-copy obstruction using a fixed, explicit three-copy LOCC operation, while keeping the target unknown. It covers every entangled isotropic visibility, rather than a perturbative high-fidelity region. Successful outputs can be recursively regrouped without learning the target; the [resource theorem](../science/resources.md) charges all rejected batches and gives a finite-confidence cap. The [implementation](../science/implementation.md) compiles the local instrument into one-qubit gates and CNOTs, and the [error account](../science/robustness.md) states sufficient control precision and its limits.

The comparisons are targeted and versioned, not an exhaustive priority certificate. No optimal yield, optimal three-copy LOCC fidelity, minimum coherent memory, positive asymptotic rate, arbitrary-noise purification, or calibrated Bell-channel advantage follows from this result. The complete same-target constructive statement and its resource qualifications are the contribution assessed here.

[Scientific reading route](../science/README.md) · [Bibliography](references.bib)
