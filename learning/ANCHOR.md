# Educational anchor and bridge

The selected educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, **10th Anniversary Edition (2010)**, Cambridge University Press, ISBN **9781107002173**, DOI [10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667). Cambridge's [official book record](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantuminformation/01E10196D0A682A6AEFFEA52D53BE9AE) identifies the 2010 edition; its digital publication listing dates from 2012. The bridge uses the selected edition, rather than treating that digital date as a different educational source.

Use the book to supply foundations when they become needed. Reading it cover to cover is not a prerequisite. The project's explicit constructions and proofs supply the steps beyond those foundations.

## Focused reading map

The chapter titles below follow Cambridge's [official contents](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE/contents/729A1063B8E18926B2B83C43A9D3F892). Within each chapter, read the indicated topic rather than unrelated applications. Section 9.2 covers state distance; its trace-distance and fidelity subsections are also listed in the publisher's [table of contents](https://assets.cambridge.org/97811070/02173/toc/9781107002173_toc.pdf).

| Foundation to take from the anchor | Focused location | Bridge supplied by this project |
| --- | --- | --- |
| State vectors, tensor products, measurement, density operators and bipartite pure states | Chapter 2, *Introduction to quantum mechanics* | [Model](../science/model.md) defines the unknown target orbit and the isotropic source; [protocol](../science/protocol.md) fixes all register orders. |
| Controlled gates, local measurement and decomposition of known unitaries | Chapter 4, *Quantum circuits* | [Implementation](../science/implementation.md) specifies the actual eight-dimensional unitary, its ancilla-free compiler and gate accounting. |
| Quantum operations, operator sums, discarded systems and depolarizing noise | Chapter 8, *Quantum noise and quantum operations* | [Protocol](../science/protocol.md) completes the success branches with a reject branch; [algebra](../science/algebra.md) computes the unnormalized output before division by success probability. |
| State comparison, fidelity and trace distance | Chapter 9, *Distance measures for quantum information*, especially §9.2 | The notation translation below fixes squared-overlap fidelity; [robustness](../science/robustness.md) supplies the conditioning and complete-experiment error arguments. |
| Entanglement as a processing resource and entanglement distillation | Chapter 12, *Quantum information theory* | [Model](../science/model.md) and [interpretation](../science/interpretation.md) specify preservation of an unknown physical target and distinguish a known standard Bell output. |
| Conditional probabilities and expectation | Appendix 1, *Notes on basic probability theory* | [Resources](../science/resources.md) counts rejected preparations, bounds conditional expected cost, then derives a hard cap and confidence guarantee. |
| Representations, equivalent copies and reducibility | Appendix 2, *Group theory* | [Protocol](../science/protocol.md) explicitly constructs the three-qubit spin decomposition and verifies the intertwiner identities; [chirality](../science/chirality.md) analyzes the complex multiplicity phase. |

These are topic pointers, not a claim that the textbook contains the present purification theorem or all its research-level ingredients. In particular, the concrete spin-half maps and their chiral optimization are worked out locally. The general two-copy obstruction is a separate cited research theorem.

## Translate the notation before using a formula

| Object | Convention in this repository | Consequence for reading |
| --- | --- | --- |
| Canonical Bell vector | $`\lvert\Phi\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2`$ | Its projector is $`P=\lvert\Phi\rangle\langle\Phi\rvert`$. Some overview formulas write the target projector as $`\Phi_U`$; the model page defines it explicitly as $`P_U`$. |
| Unknown target | $`\lvert\Phi_U\rangle=(I\otimes U)\lvert\Phi\rangle`$, with fixed $`U\in SU(2)`$ | Unknown orientation is retained in the output; it is not a gate supplied to the apparatus. |
| Visibility and noise | $`\rho_p(U)=pP_U+(1-p)I_4/4`$ | Larger $`p`$ means less noise. A depolarizing *noise probability* uses $`1-p`$ instead. |
| Target fidelity | $`F_U(\rho)=\langle\Phi_U\rvert\rho\lvert\Phi_U\rangle`$ | This is the square of the root-fidelity convention used in the textbook for a pure target. For this source it equals $`(1+3p)/4`$, not $`p`$. |
| State error | $`D(\rho,\sigma)=\lVert\rho-\sigma\rVert_1/2`$ | Trace-distance and fidelity statements must retain their different conventions. |
| Successful quantum operation | $`\mathcal E(X)=\sum_{s=\pm}K_sXK_s^\dagger`$ | Its output is unnormalized. Trace gives success probability; divide only after computing that probability. |
| Complete local instrument | Success labels plus the reject flag | Error bounds compare the complete trace-preserving flagged operation before postselection. |
| Three-copy register order | $`A_1A_2A_3:B_1B_2B_3`$ for the displayed local product Kraus maps | Regrouping source-pair tensor factors in the algebra does not require a remote quantum gate. |

The [model](../science/model.md) explains why two-qubit isotropic inputs are entangled precisely above $`p=1/3`$. That criterion and the research impossibility theorem have their own justification; they should not be inferred from a generic textbook discussion of pure-state entanglement.

## The missing scientific steps

First turn the physical task into an instrument. The anchor's operator-sum framework permits a heralded local filter, but validity requires a positive reject effect as well as a useful accepted branch. The four rows of $`C_+`$ and $`C_-`$ are orthonormal. Their remaining orthogonal complement is the reject sector. This supplies a complete physical measurement and decoding, rather than merely an algebraic map with a favorable fidelity.

Next identify what can be processed without learning the target. The three-qubit spin-half sector has two equivalent copies of the same rotation representation. The unknown rotation acts on the retained spin qubit; the multiplicity label distinguishes the copies. The two real intertwiners $`A,B`$ obey the same covariance law. Consequently their complex combinations do as well. [Protocol](../science/protocol.md) verifies the collective-spin generator identities and exponentiates them to every $`U`$.

Covariance then reduces the exact output calculation to the canonical target while preserving its interpretation for every unknown orientation. [Algebra](../science/algebra.md) contracts all eight pure/mixed input terms. The resulting success and overlap polynomials determine the full isotropic output. [Chirality](../science/chirality.md) varies the relative phase and shows precisely why a real paired filter has no gain, while the two opposite chiral outcomes can both be retained.

Finally connect a one-step gain to a finite usable procedure. A visibility-floor theorem supports recursive grouping even for the stated classical product-source mixtures. Conditional expectation and a cap-and-restart construction count the failures. A separate error analysis compares complete finite experiments, since arbitrary implementation errors need not preserve isotropy. These extensions and their assumptions are supplied in [resources](../science/resources.md) and [robustness](../science/robustness.md).

## Attribution and scope

Nielsen and Chuang is the sole educational anchor. Primary research citations remain necessary: Zhao et al. supply the general two-copy obstruction; earlier Schur filtering and cross-copy chirality work supply relevant architecture and detection precedents. [Related work](../references/RELATED_WORK.md) records those comparisons and their distinct output promises.

The construction and paired-family optimization do not prove all-LOCC optimality. The exact specimen onset does not prove a minimum coherent-memory width. The finite recursive cost is an achieved upper bound, and the stated control-error requirements are not an experimental hardware certificate. The [30-milestone map](MILESTONES.md) ends by integrating those distinctions with the positive result.

[Learning entry point and worked example](README.md) · [Scientific reading route](../science/README.md)
