# The near-pure limit at fixed block size

How much can a blind protocol suppress an already small infidelity in one accepted block? For a fixed number of pairs, there is an exact answer. Three or more pairs allow the two laboratories to attain the leading error reduction available to a joint quantum operation.

## Statement and accuracy convention

The target is the unknown physical two-qubit maximally entangled state $`\lvert\Phi_U\rangle=(I\otimes U)\lvert\Phi\rangle`$. Write $`P_U=\lvert\Phi_U\rangle\langle\Phi_U\rvert`$. The input consists of $`n`$ independent copies of

```math
\rho_{U,\epsilon}=(1-\epsilon)P_U+\epsilon\tau_U,
\qquad \mathrm{Tr}\tau_U=1,\quad \tau_U\ge0,\quad P_U\tau_U=0.
```

Here $`\epsilon`$ is the input infidelity. The noise can put different weights on the three orthogonal Bell directions, and the result below allows any density operator on their span. The block size $`n`$ is fixed as $`\epsilon\downarrow0`$. Fidelity is the squared overlap with the *same* physical target.

A fixed successful operation $`\mathcal E`$ is completely positive and trace nonincreasing. It maps pure inputs to the exact target on success throughout the unknown target orbit:

```math
\mathcal E(P_U^{\otimes n})=s_U P_U.
```

The guarantees concern $`s_U\gt 0`$. Positive success for all pure orientations is part of the uniform block claim. Let $`p_U(\epsilon)`$ be the acceptance probability and $`\epsilon'_U`$ the accepted output infidelity. Then

```math
\epsilon'_U\ge
\frac{\epsilon(1-\epsilon)^{n-1}}{n}\frac{s_U}{p_U(\epsilon)},
\qquad
\liminf_{\epsilon\downarrow0}\frac{\epsilon'_U}{\epsilon}\ge\frac1n .
```

For every $`n\ge3`$, a fixed local instrument with classical comparison attains the coefficient $`1/n`$ at every $`U`$ and for every orthogonal noise state. The $`n=3`$ instrument is the chiral filter already used in the [finite-noise protocol](protocol.md). For two pairs, the optimal *worst-target* coefficient under isotropic noise is $`1`$, by the inherited bound of Zhao et al. The single-pair retention operation has coefficient $`1`$.

## Converse from physical target preservation

Choose Kraus operators $`K_\ell`$ for the successful map. Rank one of the successful pure output implies

```math
K_\ell\lvert\Phi_U\rangle^{\otimes n}
=\alpha_\ell(U)\lvert\Phi_U\rangle,
\qquad \sum_\ell |\alpha_\ell(U)|^2=s_U.
```

For a Pauli matrix $`\sigma_a`$, vary the target along $`U(t)=U e^{it\sigma_a}`$. Apart from the common factor $`i`$, its derivative is the unit vector $`\lvert e_a\rangle=(I\otimes U\sigma_a)\lvert\Phi\rangle`$, orthogonal to $`\lvert\Phi_U\rangle`$. Let $`\lvert e_{a,j}\rangle`$ be the $`n`$-pair vector with $`\lvert e_a\rangle`$ at position $`j`$ and the target elsewhere. Differentiate the Kraus identity and project with $`Q_U=I-P_U`$ on the output. The projection eliminates the derivative of $`\alpha_\ell`$ and gives the following identity.

```math
\sum_{j=1}^n Q_U K_\ell\lvert e_{a,j}\rangle
=\alpha_\ell\lvert e_a\rangle.
```

The three Pauli directions span the full complex orthogonal complement, so the identity holds for an arbitrary unit vector $`\lvert e\rangle\perp\lvert\Phi_U\rangle`$ by complex linearity. Cauchy–Schwarz then gives

```math
\sum_{\ell,j}\bigl\|Q_UK_\ell\lvert e_j\rangle\bigr\|^2
\ge \frac{1}{n}\sum_\ell |\alpha_\ell|^2=\frac{s_U}{n}.
```

This is the sum of the accepted bad weights for single errors at the $`n`$ possible specimen positions. Average over a spectral resolution of $`\tau_U`$. Each position has prefactor $`\epsilon(1-\epsilon)^{n-1}`$. Higher-error terms have nonnegative bad weight. Dividing by $`p_U(\epsilon)`$ gives the finite inequality, and continuity gives the leading coefficient. The argument uses no locality restriction on $`\mathcal E`$.

The global symmetrization construction is established prior work. Its output in Zhao et al., [Supplemental Material A, Eq. (A.5)](https://arxiv.org/html/2509.08691v2#A1), also has first-order infidelity $`\epsilon/n`$. The local construction below shows that, with at least three specimens, the distributed laboratories reach the same leading coefficient.

For the two-pair case use Zhao et al., [Theorem 2 and Supplemental Eq. (G.100)](https://arxiv.org/html/2509.08691v2#A7). At every positive isotropic error their optimal acceptance-weighted average fidelity over four orthogonal Bell targets equals the input fidelity, even under their PPT relaxation. Taylor expansion at zero error gives an average leading error coefficient of at least one with weights proportional to the four pure acceptance probabilities. Some target therefore has coefficient at least one. Discarding one specimen attains one uniformly. This uses the weighted-average theorem and requires positive pure acceptance on those targets. It imposes a worst-target bound on the original operation.

## Local construction from cyclic specimen permutations

At one laboratory let $`R`$ cyclically shift its $`n`$ physical qubits. It commutes with the collective rotation $`U^{\otimes n}`$. Choose a rotation-invariant subspace $`\mathcal B`$ contained in one eigenspace of $`R`$, with an intertwining identification

```math
\mathcal B\simeq V_{1/2}\otimes V_J.
```

Here $`V_j`$ is the spin-$`j`$ representation. The first factor is a physical qubit output after local decoding, and the second is discarded locally. Choose any collection of mutually orthogonal blocks of this form. Both parties measure the block label. Alice uses the selected basis and Bob its conjugate in the computational basis. They keep a block when their labels agree on one of the chosen blocks, decode, and each discard the spin-$`J`$ register.

To see the pure acceptance and the error response, group the input into laboratory registers. Use $`\mathrm{vec}(M)=\sum_{ij}M_{ij}\lvert i\rangle_A\lvert j\rangle_B`$. Write $`V=U^{\mathsf T}`$ so the grouped pure input is $`2^{-n/2}\mathrm{vec}(V^{\otimes n})`$. In a matched block of dimension $`d_{\mathcal B}=2(2J+1)`$, its projected amplitude is $`2^{-n/2}\mathrm{vec}(V\otimes D_J(V))`$, where $`D_J(V)`$ is the spectator rotation. This factors into the target Bell vector on the decoded qubits and a normalized maximally entangled spectator state up to the overall amplitude. The matched block has probability $`s_{\mathcal B}=d_{\mathcal B}/2^n`$.

All one-specimen compressions of a Pauli matrix into $`\mathcal B`$ coincide. Rotating one position to another by $`R`$ changes only a cancelling scalar phase on this eigenspace. The sum over positions is the generator of the collective rotation. Thus, writing $`C`$ for the local identification of the subspace with its decoded factors,

```math
C\,\sigma_a^{(j)} C^\dagger
=\frac{1}{n}\bigl(\sigma_a\otimes I+I\otimes2J_a^{(J)}\bigr)
\qquad (j=1,\ldots,n).
```

In the one-error matched amplitude the second term errors only the spectator. It leaves the decoded target pair in the range of $`P_U`$ and vanishes after projecting with $`Q_U`$. The first term contributes accepted bad weight $`s_{\mathcal B}/n^2`$ at each position. This holds for the Pauli basis and extends to every normalized orthogonal error vector. Summing the positions and accepted blocks yields $`s_U/n`$. This gives equality in the leading bound, with $`s_U=\sum_{\mathcal B}s_{\mathcal B}`$ independent of $`U`$.

### A block exists for every allowed size

For odd $`n`$, at least one spin-half copy occurs in $`(\mathbb C^2)^{\otimes n}`$. Diagonalizing $`R`$ on its multiplicity space gives a block with $`J=0`$. At $`n=3`$ the two chiral multiplicity filters are exactly the two cyclic eigenvectors in the spin-half sector. Both are accepted under conjugate matching.

For even $`n=2m\ge4`$, it suffices to find spin zero and spin one in the same cyclic eigenspace. These representations satisfy $`V_0\oplus V_1\simeq V_{1/2}\otimes V_{1/2}`$. Pair the odd site $`O_j`$ with the following even site $`E_j`$ and let $`\lvert D\rangle`$ be the product of oriented singlets $`\lvert s\rangle_{O_j E_j}`$. Then $`R^2\lvert D\rangle=\lvert D\rangle`$. The nonzero vector $`\lvert D\rangle-R\lvert D\rangle`$ is spin zero with cyclic eigenvalue $`-1`$.

Define $`S_O^+`$ as the sum of the individual raising operators on the odd sites. The vector $`\lvert T\rangle=S_O^+(\lvert D\rangle+R\lvert D\rangle)`$ has magnetic weight $`1`$ and is annihilated by the collective raising operator, since the singlet is annihilated and the two raising operators commute. It has cyclic eigenvalue $`-1`$ because shifting replaces $`S_O^+`$ with $`S_E^+`$, and their sum annihilates the singlet $`\lvert D\rangle+R\lvert D\rangle`$.

For completeness, grouped by the odd and even registers, $`\lvert D\rangle`$ is a maximally entangled vector with a fixed singlet basis change on the even register. In the same convention $`R\lvert D\rangle`$ is obtained by a cyclic permutation $`\Pi`$ on the odd register and a sign $`(-1)^m`$ from reversing the singlets. Since $`\Pi`$ is nonscalar for $`m\ge2`$, the spin-zero vector above is nonzero. The spin-one vector is nonzero if $`S_O^+(I+(-1)^m\Pi)`$ is nonzero. For even $`m`$ apply this operator to the all-down vector. For odd $`m\ge3`$ apply it to a one-up vector at site $`1`$ with the direction of $`\Pi`$ chosen to shift it to site $`2`$. After raising $`\lvert1\rangle-\lvert2\rangle`$, the common two-up string cancels and the strings with a second up spin at sites $`3,\ldots,m`$ remain. This produces a full spin-one copy in the same $`-1`$ eigenspace. A single such matched block gives pure acceptance $`4/2^n`$.

### Matching many blocks raises acceptance

The low success of a single block at large $`n`$ is avoidable. One can choose blocks so that

```math
s_U\ge 1-O\!\left(n^3 2^{-n/2}\right).
```

Here is a counting construction. Let $`d_j(n)`$ be the multiplicity of $`V_j`$ on $`n`$ qubits. Tensoring with a spin half gives $`d_j(n)=d_{j-1/2}(n-1)+d_{j+1/2}(n-1)`$, with unavailable spin values treated as zero. Let $`m_j(\omega)`$ count spin-$`j`$ copies of cyclic eigenvalue $`\omega`$. Extracting the multiplicity character by subtracting the traces on the two adjacent magnetic-weight spaces gives, uniformly over $`j`$ and $`\omega`$,

```math
\left|m_j(\omega)-\frac{d_j(n)}{n}\right|\le D_n,
\qquad D_n=\left\lceil2\,2^{n/2}\right\rceil.
```

Indeed, the identity permutation gives $`d_j(n)`$. Each other shift by $`k`$ fixes at most $`2^{\gcd(n,k)}\le2^{n/2}`$ binary strings, a bound that applies to each magnetic-weight space. Fourier averaging gives the stated error.

In each cyclic eigenspace allocate $`r_J=\max\{0,\lfloor d_J(n-1)/n\rfloor-D_n\}`$ blocks with spectator spin $`J`$. These use $`r_{j-1/2}+r_{j+1/2}`$ copies of spin $`j`$. If the sum is positive, at least one positive summand brings a full subtraction of $`D_n`$, so the requested multiplicity is at most $`d_j(n)/n-D_n\le m_j(\omega)`$. The zero request is automatically feasible. Conversely, at most $`3D_n+2`$ copies of each spin remain unused at each momentum. Multiplying by $`2j+1`$ and summing over spins and the $`n`$ cyclic eigenvalues bounds the unused dimension by $`O(n^3 2^{n/2})`$. Dividing by $`2^n`$ yields the acceptance bound. The explicit odd and even constructions supply positive acceptance at the smaller sizes where this estimate can be vacuous.

## Finite error and charged resources

Let $`s=\sum_{\mathcal B} d_{\mathcal B}/2^n`$ denote the chosen blocks' pure acceptance. All-good inputs have that acceptance, so $`p_U(\epsilon)\ge s(1-\epsilon)^n`$. Exactly one bad input contributes $`s\epsilon(1-\epsilon)^{n-1}/n`$ to accepted bad weight. The probability of at least two bad inputs is at most $`\binom{n}{2}\epsilon^2`$. Consequently the local scheme obeys

```math
\epsilon'_U
\le \frac{\epsilon}{n(1-\epsilon)}
   +\frac{\binom{n}{2}\epsilon^2}{s(1-\epsilon)^n}.
```

Together with the converse this gives $`\epsilon'_U=\epsilon/n+O_n(\epsilon^2)`$ for fixed blocks, uniformly over $`U`$ and orthogonal noise. The displayed finite bound also makes explicit how the error remainder depends on $`n`$ and $`s`$. The block expansion does not set an optimal finite-error fidelity or a joint limit of $`n`$ and $`\epsilon`$.

Every attempt consumes $`n`$ source pairs, including rejected attempts. Each laboratory coherently processes its $`n`$ local input qubits, performs a fixed local block measurement and decoding, and announces a local label. At most $`n`$ label bits per party suffice for $`n\ge2`$, since each matched block has dimension at least two. There is no quantum communication, preshared entanglement beyond the supplied pairs, target estimation, or target-labelled operation. Ideal local basis changes and instruments are assumed. The resource count here does not optimize their gate counts or implementation time. With independent repeated blocks, the expected pair consumption for one accepted output is $`n/p_U(\epsilon)`$.

## Expected specimen cost at fixed isotropic input quality

For independent identical isotropic source pairs of fixed initial target fidelity above one half, the protocol uses $`O(1/\epsilon_{\mathrm f})`$ native pairs in expectation to produce one accepted pair with infidelity at most $`\epsilon_{\mathrm f}`$. The three-pair chiral recurrence reaches any fixed positive entry error with finite expected cost. Both protocols preserve isotropy by covariance under the two local rotations. Each subsequent attempt prepares independent copies of the preceding level and restarts on failure.

For each block size $`m\ge3`$, choose the finite successful cyclic construction at small $`m`$ and the high-acceptance construction at large $`m`$. The pure acceptances satisfy $`s_*=\inf_{m\ge3}s_m\gt 0`$ because every chosen $`s_m`$ is positive and $`s_m\to1`$. For input infidelity $`e`$ with $`me\le1/2`$, the finite-error estimates give

```math
p_m(e)\ge s_m(1-me),
\qquad
e'\le\frac{e}{m}\left(1+C m^3e\right)
```

with a constant $`C\ge 2+1/s_*`$ independent of $`m`$. Indeed, $`(1-e)^m\ge1-me\ge1/2`$, $`1/(1-e)\le1+2e`$, and $`2\binom m2\le m^2`$.

Choose a fixed $`n_0\ge5`$, set $`n_k=n_0+k`$, and use the following deterministic error bounds for the successive levels after entry:

```math
E_{k+1}=\frac{E_k}{n_k}\left(1+C n_k^3 E_k\right),
\qquad
r=\frac{2}{n_0}.
```

Choose the entry bound $`E_0\gt 0`$ small enough that $`C E_0\sup_{k\ge0}(2n_k+1)^3r^k\le1`$. The supremum is finite. Inductively $`E_k\le E_0r^k`$ and each level accepts with output error at most $`E_{k+1}`$. In particular, for every $`3\le m\le2n_k+1`$, one has $`mE_k\le1/2`$ and $`C m^3E_k\le1`$.

Let $`B_k=\prod_{j\lt k}n_j`$. The multiplicative error factor is bounded since

```math
B_k E_k
=E_0\prod_{j\lt k}(1+C n_j^3E_j)
\le E_0\exp\!\left(C\sum_{j\ge0}n_j^3E_j\right)
<\infty .
```

The product of the acceptance lower bounds $`b_j=s_{n_j}(1-n_jE_j)`$ is bounded away from zero. Each factor is positive and $`\sum_j(1-b_j)\le\sum_j[(1-s_{n_j})+n_jE_j]\lt \infty`$ by the exponential pure-acceptance estimate and the geometric error bound. Counting every failed attempt, the expected native-pair cost to finish level $`k`$ is at most the fixed entry cost times $`B_k/\prod_{j\lt k}b_j`$, which is $`O(B_k)`$.

For an arbitrary target $`0\lt \epsilon_{\mathrm f}\lt E_0`$, take the crossing $`E_{k+1}\le\epsilon_{\mathrm f}\lt E_k`$ and finish with one block of size $`m=\max\{3,\lceil2E_k/\epsilon_{\mathrm f}\rceil\}`$. The crossing gives $`E_k/\epsilon_{\mathrm f}\le n_k`$, so $`m\le2n_k+1`$ and the same finite-error estimate gives $`e'\le2E_k/m\le\epsilon_{\mathrm f}`$. Its success probability is at least $`s_*/2`$. Its expected native cost is therefore $`O(B_k\,m)=O(B_k E_k/\epsilon_{\mathrm f})=O(1/\epsilon_{\mathrm f})`$.

The constant depends on the fixed source quality and the selected entry and block procedures. The bound counts specimens with ideal local controls. The block size can grow with the requested accuracy, and this estimate does not bound coherent storage, gate count, or elapsed time as functions of that accuracy. For a comparison with global access, Childs et al. obtain the same specimen exponent using joint swap tests on noisy qudits. [Streaming quantum state purification](https://quantum-journal.org/papers/q-2025-01-21-1603/).

The [three-pair finite-noise theorem](anisotropic-noise.md) supplies a separate uniform fidelity-floor update for nonidentical inputs with locally maximally mixed marginals. The tangent statement here requires only the exact target orbit and the orthogonality of the noise, with the input error taken to zero at fixed $`n`$.
