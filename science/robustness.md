# Imperfect controls and finite precision

The exact amplification theorem concerns isotropic inputs and ideal local instruments. Its robustness is quantitative but not uniform all the way to a pure target: the ideal gain vanishes as the input becomes pure. This page gives sufficient error budgets, rather than a hardware threshold or an assertion that fixed noisy gates permit unlimited purification.

## A composable error convention

Use squared overlap with the pure target as fidelity, and half trace distance

```math
D(\rho,\sigma)=\tfrac12\lVert \rho-\sigma\rVert _1.
```

An instrument includes its classical outcome record. In particular, the ideal local map has two quantum-output branches, with Kraus operators $`C_+`$ and $`C_-`$, and a reject branch of weight $`\mathrm{Tr}[(I-C_+^\dagger C_+-C_-^\dagger C_-)\rho]`$. The reject branch has no retained quantum output. The direct sum of these branches is a completely positive trace-preserving channel, denoted $`\mathcal J`$.

Suppose the implemented local channels obey

```math
\tfrac12\lVert \widehat{\mathcal J}_A-\mathcal J_A\rVert _\diamond\le\eta_A,
\qquad
\tfrac12\lVert \widehat{\mathcal J}_B-\mathcal J_B\rVert _\diamond\le\eta_B.
```

These bounds include all local gates, measurements and outcome labels used in the attempt. They are assumptions or externally established control specifications, not something inferred from the unknown target. Reliable classical comparison is ideal in the base model; any imperfect comparison can instead be included as an additional channel error. Complete instruments, rather than only their normalized success branches, make the error accounting meaningful under postselection.

The sum of the two local bounds assumes an actual product of local channels, or such a bound uniformly conditional on an available classical history. If an unobserved shared environment correlates the laboratory errors, use a direct bound on the complete joint instrument instead. Bounds on its two reduced channels alone do not establish that joint bound.

If the actual three-pair source is at half trace distance at most $`r`$ from an allowed ideal input, contractivity and the channel hybrid inequality give a complete-attempt error budget

```math
e=r+\eta_A+\eta_B.
```

All bounds below can be capped at one when necessary. The useful regime has $`e`$ below the stated success probability.

## Conditioning lemma

Let an ideal complete experiment have an accepted subnormalized output $`\sigma=s\rho`$, with $`s>0`$. Let its implemented counterpart have accepted output $`\widehat\sigma=\widehat s\widehat\rho`$. Coarse-grain all other records into a single failure flag, discarding their quantum outputs. If the two complete outputs have half trace distance at most $`e`$, then

```math
|\widehat s-s|\le e,
\qquad
D(\widehat\rho,\rho)\le\frac{e}{s}
\quad\text{whenever }\widehat s>0.
```

To prove this, the orthogonal accept/failure blocks give

```math
\lVert \widehat\sigma-\sigma\rVert _1+|\widehat s-s|\le2e.
```

Each term is at least $`|\widehat s-s|`$, proving the success bound. For the conditional states, write

```math
\widehat\rho-\rho
=\frac{\widehat\sigma-\sigma}{s}
+\widehat\sigma\left(\frac1{\widehat s}-\frac1s\right).
```

The triangle inequality, $`\lVert \widehat\sigma\rVert _1=\widehat s`$, and the displayed block bound prove the conditional bound. No commutativity, isotropy or independence is required for this lemma. Its denominator is the ideal success probability. A sufficient condition for actual success is $`e\lt s`$.

## One purification attempt

For three identical ideal inputs of visibility $`p`$, define

```math
s(p)=\frac{(p+1)(2p^2-p+1)}8,
\qquad
f(p)=\frac{p(5p+1)}{3(2p^2-p+1)},
```

and the exact ideal fidelity gain

```math
\Delta_F(p)=\frac{p(1-p)(3p-1)}{2(2p^2-p+1)}.
```

The complete instrument bound implies

```math
\widehat s\ge s(p)-e,
\qquad
\widehat F\ge\frac{1+3f(p)}4-\frac{e}{s(p)}.
```

In particular, for $`1/3\lt p\lt 1`$, the following is a sufficient condition for fidelity strictly above the ideal input value $`(1+3p)/4`$:

```math
e\lt s(p)\Delta_F(p)
=\frac{p(1-p^2)(3p-1)}{16}.
```

This is a conservative certification inequality for arbitrary errors in the stated metric. It is not the largest tolerable physical error rate. For a desired fraction $`\alpha\in(0,1)`$ of the ideal gain, it suffices that

```math
e\le(1-\alpha)s(p)\Delta_F(p).
```

For example, $`p=3/5`$ gives ideal input fidelity $`7/10`$, output fidelity $`11/14`$, success $`28/125`$, and $`s\Delta_F=12/625`$. If the sum of the two local half-diamond instrument errors is at most $`1/500`$ and the source is exact, the guaranteed accepted fidelity is at least $`87/112\approx0.776786`$, with success at least $`111/500=0.222`$. The exact ideal value is approximately $`0.785714`$.

For unequal allowed ideal visibilities $`p_i\ge p_0>1/3`$, use the floor theorem with $`s_0=s(p_0)`$. The same reasoning gives

```math
\widehat s\ge s_0-e,
\qquad
\widehat F\ge\frac{1+3f(p_0)}4-\frac{e}{s_0}.
```

It certifies amplification above the prescribed ideal quality floor when $`e\lt s_0\Delta_F(p_0)`$. It does not promise improvement over the best member of an unequal-quality batch.

## Source perturbations and a fixed target

For a product of actual inputs $`\widetilde\rho_i`$ and chosen allowed reference inputs $`\rho_i`$,

```math
D\left(\bigotimes_{i=1}^3\widetilde\rho_i,
       \bigotimes_{i=1}^3\rho_i\right)
\le\sum_{i=1}^3D(\widetilde\rho_i,\rho_i).
```

Thus small nonisotropic source deviations have a direct one-attempt error budget. A correlated source needs an actual bound on the complete joint state; marginal bounds alone do not establish one.

As a limited example, let the $`i`$th pair have target $`\Phi_{U_i}`$ and visibility $`p_i`$, and compare it with the common-target ideal input using $`\Phi_U`$. Then

```math
D(\rho_{p_i}(U_i),\rho_{p_i}(U))
=p_i\sqrt{1-\frac{|\mathrm{Tr}(U^\dagger U_i)|^2}{4}}.
```

For a relative rotation through angle $`\theta_i`$, this is $`p_i|\sin(\theta_i/2)|`$. Summing these quantities supplies $`r`$ in the one-attempt theorem. This continuity bound does not establish indefinite purification with drifting targets. In particular, a fixed nonzero perturbation budget cannot preserve strict gain uniformly as $`p\to1`$.

## A finite complete protocol

The [resource construction](resources.md) implements ideal recursive purification with a deterministic native-pair cap $`N`$, failure probability at most $`\delta`$, and conditional infidelity at most $`\epsilon_{\rm id}`$. Every elementary attempt consumes three pair registers and produces at most one. Therefore, if at most $`N`$ native pairs enter the complete run, the number of elementary attempts is pathwise bounded by

```math
G\le\lfloor N/2\rfloor.
```

Indeed, each success reduces the live-pair count by two and each rejection by three; discards only decrease it further. This count includes attempted internal nodes of rejected and aborted trees.

For a complete finite adaptive experiment, the usual sequential channel hybrid argument also applies to outcome-dependent calls: include the transcript in the state, and pad unused calls with ideal identities up to the deterministic call cap. A uniform per-attempt half-diamond instrument error at most $`\eta`$ gives full-output half trace distance at most $`G\eta`$. The errors may be different and transcript-dependent, provided their conditional channel bounds hold uniformly and no unmodelled environment memory is being reused. More generally write

```math
E\le\sum_{a=1}^{G_{\max}}\eta_a
+E_{\rm source}+E_{\rm storage}+E_{\rm classical}.
```

Each summand is a composable bound on the corresponding complete channel or joint input. An arbitrary correlated noise process requires a bound on its complete strategy; bounds on memoryless reduced channels alone are insufficient. With uniform local instrument errors, $`\eta_a\le\eta_A+\eta_B`$. Independent native preparation errors of half trace distance at most $`r_{\rm native}`$ have $`E_{\rm source}\le Nr_{\rm native}`$; a nonproduct source must instead satisfy a complete joint-state bound.

The actual finite protocol then has

```math
\Pr(\text{failure})\le\delta+E,
\qquad
1-\widehat F_{\rm success}
\le\epsilon_{\rm id}+\frac{E}{1-\delta},
```

provided $`E\lt 1-\delta`$. The accepted output need not be isotropic. The proof compares the complete actual experiment with the complete ideal one before conditioning, so it does not feed a nonisotropic noisy output into an ideal isotropic recurrence.

For target conditional infidelity $`\epsilon`$ and failure probability $`\delta_{\rm tot}`$, one explicit allocation is

```math
\epsilon_{\rm id}=\epsilon/2,
\quad\delta=\delta_{\rm tot}/2,
\quad
E\le\min\!\left\{\delta_{\rm tot}/2,
             (1-\delta_{\rm tot}/2)\epsilon/2\right\}.
```

This gives a sufficient finite-precision construction. It can be conservative; it claims no optimal accumulation law or fault-tolerance threshold.

## Translating the budget to gate precision

Let $`W`$ be the exact fixed local three-qubit unitary in [the implementation](implementation.md), and let its implementation $`\widehat W`$ satisfy $`\lVert \widehat W-W\rVert \le\xi`$ in operator norm, with a consistent global phase. Unitary-channel distance and postprocessing contractivity give

```math
\tfrac12\lVert \widehat{\mathcal J}-\mathcal J\rVert _\diamond\le\xi.
```

If an exact circuit has $`L`$ unitary gates and each implemented gate has operator-norm error at most $`\xi/L`$, the telescoping product bound gives $`\lVert \widehat W-W\rVert \le\xi`$. Measurement and storage errors must be included separately. An angle-rounded gate $`\exp(-i\theta H)`$ with $`\lVert H\rVert \le1`$ has error at most the angle error, so a fixed continuous-control library needs angle precision $`O(\xi/L)`$, or $`O(\log(L/\xi))`$ bits per angle. A chosen fault-tolerant gate library must add its actual synthesis cost; the constant-size real-rotation model does not make arbitrary-angle gates free in that model.

The full-budget theorem permits, for example, equal local errors $`\eta_A=\eta_B\le E/(2G_{\max})`$ after reserving the other terms. This is an explicit sufficient requirement on local controls, not a certificate that a laboratory realizes it. Local gate calibration and a certified input-quality promise remain separate resources from learning the unknown entangled target.

## Why a fixed arbitrary error bound does not imply arbitrary purity

An allowed adverse implementation can depolarize one final output qubit with probability $`\lambda>0`$. Its additional local half-diamond error is at most $`\lambda`$. Even if its incoming pair were exactly the target, the final output is

```math
(1-\lambda)\Phi_U+\lambda I_4/4,
```

whose target infidelity is $`3\lambda/4`$. This explicit error within the allowed class precludes a uniform guarantee of arbitrarily small output infidelity at fixed positive control-error budget. It does not rule out better performance for a specified physical noise model, corrected local gates, or errors that decrease with the requested accuracy.
