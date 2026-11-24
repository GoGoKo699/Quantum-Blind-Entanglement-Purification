# Finite budgets and recursive use

The one-step map can be repeated without estimating the target orientation or the individual input qualities. This section supplies a finite input budget, including rejected batches, and an explicit sequential implementation. It treats ideal operations; [circuit errors](robustness.md) must be charged to the complete adaptive procedure rather than inserted into the isotropic recurrence without justification.

## Source promise and levels

Fix a common unknown two-qubit maximally entangled target $`\Phi_U`$ and a supplied visibility-floor promise $`1/3\lt p_0\lt 1`$. The supplied pairs are independent isotropic states about that target, or a classical mixture of global product states for which **every latent input visibility** is at least $`p_0`$. A promise on marginal fidelities alone is insufficient. The target does not drift between specimens. No extra shared entanglement or quantum communication is supplied.

The floor is an input assumption, not a certification experiment performed by this protocol. If it is obtained by a separate source-calibration procedure, that procedure's specimens and confidence allowance must be added. The one-step filter needs neither the floor nor the actual visibility; a quantitative finite stopping rule needs the supplied floor. No target-orientation estimation is required in either case.

Write

```math
f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},\qquad
s(p)=\frac{(p+1)(2p^2-p+1)}8,
\qquad p_{\ell+1}=f(p_\ell).
```

A level-zero pair is a native source pair. A level-$`\ell+1`$ attempt consumes three completed level-$`\ell`$ pairs, applies the local filter, and keeps its one output only when the chirality records are accepted. A rejected attempt loses all three inputs. Both accepted chirality outcomes give the same isotropic output and the same probability; keeping their individual records does not invalidate the floor theorem.

The exact unequal-quality map is increasing in each visibility. Therefore every level-$`\ell`$ output has visibility at least $`p_\ell`$, and every level-$`\ell+1`$ attempt has conditional success probability at least $`s(p_\ell)`$. This assertion remains true after conditioning on the entire preceding classical record. To see this for the mixture promise, condition first on the latent product-source component: the surviving disjoint branches are still product pairs about the same target, with the stated pointwise floors. Measurement records only reweight the mixture of such components.

## A concrete protocol with a hard input cap

Choose a target squared-overlap infidelity $`0\lt \epsilon\lt 3(1-p_0)/4`$ and failure allowance $`0\lt \delta\lt 1`$. Compute the smallest integer $`j\ge1`$ such that

```math
\frac34(1-p_j)\le\epsilon.
```

Define

```math
E_0=1,\qquad E_j=\prod_{\ell=0}^{j-1}\frac3{s(p_\ell)},\qquad
B=\lceil2E_j\rceil,\qquad
R=\left\lceil\log_2\frac1\delta\right\rceil,\qquad N=BR.
```

The protocol performs at most $`R`$ runs. In each run it recursively prepares one level-$`j`$ pair, retrying a failed node with newly prepared children. It aborts that run just before requesting native pair $`B+1`$, discards its remaining stored pairs, and starts the next run using fresh unused inputs. It stops at the first completed output. The hard cap counts **every native pair requested**, including all children of failed nodes and all discarded pairs in aborted runs.

**Finite-budget guarantee.** At most $`N`$ native pairs suffice for probability at least $`1-\delta`$ of producing an output. Conditioned on producing one, its overlap with the same unknown target is at least $`1-\epsilon`$. The circuit and acceptance rule do not use $`U`$ or the actual visibilities; only the certified floor and requested accuracies enter the stopping level and budget. If the requested infidelity already exceeds the initial floor infidelity, one native pair suffices and no filtering is needed. If $`p_0=1`$, the source is already perfect.

### Why this budget is valid

First consider an uncapped recursive preparation. Let $`C_\ell`$ count its native inputs. Uniformly over any prior classical history satisfying the source promise,

```math
\mathbb E[C_\ell\mid\text{history}]\le E_\ell.
```

The level-zero statement is exact. For a level-$`\ell+1`$ preparation, the chance of needing attempt $`k`$ is at most $`(1-s(p_\ell))^{k-1}`$, even when attempts are classically dependent. Conditional on reaching it, its three child preparations have total expected cost at most $`3E_\ell`$. Summing the nonnegative costs gives

```math
\mathbb E[C_{\ell+1}\mid\text{history}]
\le 3E_\ell\sum_{k\ge1}(1-s(p_\ell))^{k-1}
=\frac{3E_\ell}{s(p_\ell)}.
```

This is a conditional-expectation argument; it assumes neither that attempt costs are independent of outcomes nor that hidden input qualities are independent. For identical visibility $`p_0`$, equality holds throughout, so $`E_j`$ is the exact mean cost of this recursive architecture.

Markov's inequality now gives

```math
\Pr(C_j>B\mid\text{history})\le\frac{E_j}{B}\le\frac12.
```

A run is aborted precisely when uncapped preparation would require more than $`B`$ inputs. Therefore every run fails with conditional probability at most $`1/2`$, even given all previous aborts. All $`R`$ runs fail with probability at most $`2^{-R}\le\delta`$. Conditioning on the cap or choosing the first completed run only changes classical mixture weights, so the accepted-output floor survives. For a finite supplied stream, the uncapped routine is only an analysis device: append hypothetical floor-quality pairs to that stream. The actual capped execution never accesses them.

The conclusion is heralded. An abort is an explicit failure flag, not an uncharged or silently omitted event. On success the output is isotropic, so its half-trace distance to $`\Phi_U`$ equals its squared-overlap infidelity. Preparing a fixed local product output on final failure instead gives unconditional target infidelity at most $`\epsilon+\delta`$ and half-trace distance at most $`\epsilon+\delta`$; that different output convention also charges the two local output initializations.

## Different noise axes

The [sharp heterogeneous floor](anisotropic-noise.md) supplies a recurrence for independent pairs with maximally mixed marginals, a shared unknown dominant Bell eigenvector and a certified overlap floor $`w_0\gt1/2`$. Use only the pooled chirality success flag at every node. At level $`\ell`$, put

```math
w_{\ell+1}=W(w_\ell),\qquad s_\ell=\frac{w_\ell^3}{2},\qquad
E_j=\prod_{\ell=0}^{j-1}\frac{3}{s_\ell}.
```

The floor refers to fidelity, rather than the isotropic visibility used above. Every reached node succeeds with probability at least $`s_\ell`$ conditional on the preceding pooled record. The same conditional-expectation proof gives mean native-pair consumption at most $`E_j`$. For the least $`j`$ with $`w_j\ge1-\epsilon`$, the previous cap-and-restart rule uses $`B=\lceil 2E_j\rceil`$ and $`R=\lceil \log_2(1/\delta)\rceil`$. The success probability is at least $`1-\delta`$ and the hard native input cap is $`BR`$. The argument also applies to the stated latent product mixtures, using the pointwise bounds and reweighting the components by the record.

For $`w_0=0.70`$, $`\epsilon=0.01`$ and $`\delta=0.05`$, six levels give $`w_6\simeq0.99347798`$. The conservative mean bound is about $`909{,}650.24`$, the per-run cap is $`1{,}819{,}301`$, and five runs cap the input at $`9{,}096{,}505`$ native pairs. The depth-first schedule holds at most 13 incoming pair halves per laboratory, plus compiler workspace. These guarantees use the sharp floor for one application and a lower bound on success. The protections against heterogeneous sources make this cap larger than the isotropic cap in the [worked example](#a-numerical-budget-example).

For fixed $`w_0`$, the update increases to one. Its near-pure error ratio is $`1/3+O(1-w_\ell)`$. The errors become summable, so the constant-factor comparison with $`3^{-\ell}`$ holds by multiplying the successive ratios. Also $`3/s_\ell=6(1+O(1-w_\ell))`$. The same architecture thus has a hard cap of order at most $`\epsilon^{-\log_3 6}\log(1/\delta)`$ for fixed $`w_0`$, with constants depending on that floor. Near the separability boundary the gain is only $`3(w-1/2)^2+O((w-1/2)^3)`$.

A [schedule of larger blocks](near-pure-limit.md#expected-specimen-cost-at-fixed-isotropic-input-quality) bounds expected specimen cost by a constant times inverse target error after initial chiral preparation for iid isotropic inputs. The local basis changes and storage differ from the three-pair circuit.

## Accuracy dependence at a fixed initial floor

Put $`x_\ell=1-p_\ell`$ and

```math
q(p)=\frac{3-p}{3(2p^2-p+1)}.
```

Then

```math
x_{\ell+1}=x_\ell q(p_\ell),\qquad
\frac13\le q(p_\ell)\le q(p_0)\lt 1.
```

The derivative of $`q`$ is negative on $`[p_0,1]`$. Hence $`\sum_\ell x_\ell\le x_0/(1-q(p_0))`$. Moreover

```math
3q(p)-1=\frac{2(1-p^2)}{2p^2-p+1}=O_{p_0}(1-p).
```

Consequently the product $`\prod_{\ell\lt j}3q(p_\ell)`$ converges to a finite positive constant. Thus

```math
x_j=\Theta_{p_0}(3^{-j}),\qquad
j=\log_3(1/\epsilon)+O_{p_0}(1).
```

For the cost, $`s(p)\le1/2`$ and

```math
1-2s(p)=\frac{(1-p)(2p^2+3p+3)}4=O(1-p).
```

Therefore $`\prod_{\ell\lt j}(2s(p_\ell))^{-1}`$ also converges to a finite positive constant, and

```math
E_j=\Theta_{p_0}(6^j)
=\Theta_{p_0}\!\left(\epsilon^{-\log_3 6}\right),
\qquad \log_3 6\simeq1.63093.
```

The hard-budget construction above consequently uses

```math
N=O_{p_0}\!\left(\epsilon^{-\log_3 6}\log\frac1\delta\right)
```

for $`0\lt \delta\le1/2`$. This is the cost of the displayed architecture, not an optimal distillation law. The constants depend on the initial floor and are not uniform as $`p_0\downarrow1/3`$. The yield of this recursively purified single-output construction vanishes as the requested fidelity approaches one; no positive asymptotic communication rate follows.

For an explicit, conservative finite bound without asymptotic notation, let $`D_0=2p_0^2-p_0+1`$ and $`q_0=q(p_0)`$. The inequalities above give

```math
1-p_j\le (1-p_0)3^{-j}
\exp\!\left[\frac{4(1-p_0)}{D_0(1-q_0)}\right],
\qquad
E_j\le6^j\exp\!\left[\frac{1-p_0}{s(p_0)(1-q_0)}\right].
```

Iterating the exact scalar recurrence gives much smaller useful budgets than these uniform envelopes.

## Circuit, communication and storage costs

Depth-first preparation holds at most two completed children at each ancestor while constructing the third child. If $`M_j`$ is the maximum number of retained pair registers, then $`M_0=1`$ and $`M_j=M_{j-1}+2=2j+1`$. Thus each laboratory needs at most $`2j+1`$ physical pair-half qubits, plus any constant workspace used by its chosen fixed three-qubit compiler. This is an available architecture, not a memory lower bound. Stored outputs require ideal memory over the preparation time in the present model.

Let $`L`$ be the total acquired native pairs, $`S`$ the successful elementary filters, $`Q`$ the failed elementary filters, $`D`$ the pairs discarded on aborts, and $`M`$ the live pairs. Register accounting gives

```math
L=2S+3Q+D+M.
```

Every elementary filter therefore contributes at least two units to the input count, so the total number of filter attempts $`A=S+Q`$ is at most $`\lfloor N/2\rfloor`$ under the hard cap. This pathwise bound also covers aborted runs and does not depend on average success probabilities.

Each attempt applies one fixed local three-qubit unitary and measures two qubits in each laboratory. The parties exchange their two-bit status/chirality records, using at most four transmitted classical bits and one simultaneous exchange per attempt. If a chosen local compiler uses $`G`$ elementary gates, the whole protocol uses at most $`G\lfloor N/2\rfloor`$ gates per laboratory, at most $`2\lfloor N/2\rfloor`$ measured qubits per laboratory, and at most $`4\lfloor N/2\rfloor`$ transmitted bits. Initial source acquisition, failed attempts and stored-qubit lifetimes are separate resources rather than a free preparation oracle.

If a native pair takes at most $`t_{\rm src}`$ to acquire and a complete elementary attempt, including its local circuit, readout and classical comparison, takes at most $`t_{\rm att}`$, the serial depth-first implementation has elapsed time at most

```math
Nt_{\rm src}+\lfloor N/2\rfloor t_{\rm att}.
```

No claim about an optimal latency, thermodynamic work, fault-tolerant overhead or hardware crossover is made by this count. Classical control can discard old outcomes after the comparison; it needs a recursion stack of $`O(j)`$ small counters and an input counter of $`O(\log N)`$ bits.

## A numerical budget example

Starting from $`p_0=3/5`$, the guaranteed input fidelity is $`7/10`$. Five successful levels give output infidelity at most $`0.007994`$. The exact uncapped mean input count of the recursive architecture is approximately $`54005.20`$. For requested $`\epsilon=0.01`$ and $`\delta=0.05`$, the conservative cap-and-restart construction uses $`B=108011`$, $`R=5`$, hence at most $`N=540055`$ native pairs. It needs at most eleven pair-half qubits per laboratory, plus constant compiler workspace. These large counts are part of the method's resource account; the three-copy onset does not imply high yield at very high fidelity.

The [resource check](../verification/check_resources.py) reproduces these finite values, reconstructs the first two levels' actual cost distribution independently of the expectation formula, and checks register accounting in seeded recursive executions. Those finite checks support the formulas at their tested points; the conditional arguments above establish the stated uniform guarantee.
