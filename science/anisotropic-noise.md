# Three-pair purification with different noise axes

A source can distribute pairs with different storage histories. The three-pair chiral filter [already defined here](protocol.md) can improve a common guaranteed fidelity even when the losses of fidelity and the axes of the errors differ across pairs.

## The common-floor theorem

Let three independent two-qubit pairs have maximally mixed marginals. Each has the same unknown maximally entangled eigenvector $`\Phi_U`$ and squared overlap at least $`w`$, where $`1/2\lt w\lt1`$. Let $`r=1-w`$. Alice and Bob run the fixed chiral filter, and combine both opposite-sign outcomes into a single success record.

The accepted output has maximally mixed marginals and has $`\Phi_U`$ as its unique dominant eigenvector. For this filter the exact worst conditional fidelity over the entire promised class is

```math
W(w)=\frac{3w^3+r^3}{3w^3+r^3+w^2r+3wr^2}\gt w.
```

Three rank-two states of fidelity $`w`$ with mutually orthogonal Pauli error axes attain equality. The success probability of every promised batch is at least $`w^3/2`$. This lower bound follows from the all-target term. In the worst-fidelity example the success probability is $`(3w^3+r^3+w^2r+3wr^2)/6`$. For $`w=7/10`$, the worst accepted fidelity is $`22/29\simeq 0.75862`$, attained at success probability $`29/125`$. The isotropic equal-fidelity example gives $`11/14`$ at success probability $`28/125`$.

There is no need to identify the target or any noise axis. The result also holds for a classical mixture of product batches with the same target and a pointwise floor in every component. The guarantee concerns the common floor. If one input is better than the floor, its fidelity can exceed the accepted fidelity. The inherited two-copy impossibility for isotropic sources still rules out a uniform two-pair guarantee on the larger class.

## A real Pauli description of the source

Covariance lets the proof work at $`U=I`$. Use the orthonormal Bell-vector basis $`\Phi,\Phi_X,\Phi_Y,\Phi_Z`$, with $`\Phi_M=(I\otimes M)\Phi`$. An input that has $`\Phi`$ as an eigenvector is block diagonal in the target and its orthogonal complement. Write its complementary block as $`H`$ in the three Pauli directions. The Bob marginal of that block is $`\frac12\sum_{a,b}H_{ab}\sigma_a\sigma_b`$ in the convention $`H_{ab}=\langle\Phi_{\sigma_a}|\rho|\Phi_{\sigma_b}\rangle`$. The Pauli product identity shows that the three Bloch components are proportional to the three independent entries of the imaginary antisymmetric part of $`H`$. They vanish because the marginal is maximally mixed. Hence $`H`$ is real, symmetric and positive semidefinite.

Diagonalize $`H`$ in real unit directions. A pair with target weight $`F\ge w`$ is a convex combination of the perfect target and states of the form $`wP+rP_a`$, where $`P=|\Phi\rangle\langle\Phi|`$ and $`P_a=|\Phi_{\sigma_a}\rangle\langle\Phi_{\sigma_a}|`$ for $`\sigma_a=a\cdot\boldsymbol\sigma`$. The weight on the perfect vertex can be chosen to be $`(F-w)/r`$. The remaining weight is distributed over the eigenvectors of $`H`$. The proof can therefore optimize over products of these extreme states. For a fixed candidate fidelity, the homogeneous lower bound on accepted overlap is linear in each of the three inputs, so it passes to their mixtures.

## The chiral compression

In a product of Bell rays let $`M`$ be the tensor product of the one-sided Pauli error operators and identities. On the two accepted records, the unnormalized output vectors are represented by the $`2\times2`$ matrices $`C_\pm M C_\pm^\dagger`$, each with vectorization prefactor $`1/\sqrt8`$. For a compressed matrix $`\alpha I+\sigma_v`$, with real $`\alpha`$ and $`v`$, the resulting branch has target overlap numerator $`\alpha^2/4`$ and orthogonal weight $`\lVert v\rVert^2/4`$.

Spin time reversal $`\Theta=iYK`$, with $`K`$ complex conjugation in the computational basis, changes the sign of each Pauli matrix. The real Schur intertwiners in the [protocol](protocol.md) commute with this time reversal on the input and output representations. The factor of $`i`$ in the chiral intertwiners changes sign, giving, for $`k`$ active Pauli factors,

```math
\Theta(C_+MC_+^\dagger)\Theta^{-1}=(-1)^k C_-MC_-^\dagger.
```

As a consequence, the two branch density matrices cancel the cross terms between their scalar and Pauli-vector components. Each remaining pure Pauli-direction projector has maximally mixed marginals. This proves closure of the pooled output class. An individual sign record can leave cross terms. The recurrence uses the pooled flag and does not select batches using the two finer records.

To get the overlap and error weights, the spin intertwining identity makes the compression covariant under simultaneous rotations of the Pauli directions. In addition, the chiral cycle eigenvalue cancels between $`C_+`$ and $`C_+^\dagger`$. Hence the one-active-factor map is proportional to $`\sigma_a`$, the two-factor scalar and vector are proportional to $`a\cdot b`$ and $`a\times b`$, and the three-factor scalar and vector are proportional to the determinant and the cyclic sum $`a(b\cdot c)+b(c\cdot a)+c(a\cdot b)`$. These are the rotation-invariant scalar and equivariant vector tensors in three dimensions. Substitution into the explicit two-row Schur maps determines their magnitudes. The one-factor vector coefficient is $`1/3`$. Testing equal and orthogonal axes gives magnitudes $`1/3`$ and $`1/\sqrt3`$ for the two-factor coefficients. Three equal axes and three ordered coordinate axes give magnitudes $`1/3`$ and $`1/\sqrt3`$ for the three-factor vector and scalar, respectively. [Exact Pauli-basis checks](../verification/check_anisotropy.py) also verify those coefficients in every slot.

Put $`x=a\cdot b`$, $`S=(a\cdot b)^2+(b\cdot c)^2+(c\cdot a)^2`$ and $`T=(a\cdot b)(b\cdot c)(c\cdot a)`$. Squaring the compressed components, and adding both signs, gives the following table for pure Bell-ray products.

| Active errors | Unnormalized target weight | Unnormalized orthogonal weight |
| --- | ---: | ---: |
| Zero | $`1/2`$ | $`0`$ |
| One | $`0`$ | $`1/18`$ |
| Two, directions $`a,b`$ | $`x^2/18`$ | $`(1-x^2)/6`$ |
| Three, directions $`a,b,c`$ | $`(1-S+2T)/6`$ | $`(S+6T)/18`$ |

The last row uses the Gram determinant for the scalar term. The squared norm of the cyclic vector sum is $`S+6T`$.

## Optimizing over different axes

For three noisy vertices $`wP+rP_a`$, expand the product over the eight pure choices. With $`N`$ the target weight and $`E`$ the orthogonal weight, the table gives

```math
\begin{aligned}
N&=\frac{w^3}{2}+\frac{wr^2S}{18}+\frac{r^3(1-S+2T)}6,\\
E&=\frac{w^2r}{6}+\frac{wr^2(3-S)}6+\frac{r^3(S+6T)}{18}.
\end{aligned}
```

Subtracting $`w`$ from the normalized fidelity gives $`(rN-wE)/(N+E)`$. The numerator factors as

```math
rN-wE=\frac{r(1-2r)}6\left[(1-2r)(2-r)+rS-2r^2T\right].
```

Since $`S\ge3|T|`$ and $`r\lt1/2`$, this positive numerator is minimized by orthogonal directions. The denominator differs from its orthogonal value by $`r^2(-S+6rT)/9\le0`$. Orthogonal directions thus minimize the entire normalized fidelity.

The remaining product vertices have one or more perfect inputs. With two noisy vertices the minimum is at perpendicular error axes: the target weight increases and the error weight decreases with the squared dot product. With $`u=r/w\in(0,1)`$, the worst ratios of error weight to target weight for zero, one, two and three noisy vertices are, in order,

```math
0,\qquad \frac u9,\qquad \frac{2u}{9}+\frac{u^2}{3},\qquad
\frac{u+3u^2}{3+u^3}.
```

The order is increasing. For the last comparison, the positive numerator after multiplication by $`9(3+u^3)`$ is $`3u+18u^2-2u^4-3u^5`$. Taking $`1/(1+E/N)`$ now gives the stated $`W(w)`$. Its reported sharpness is for this fixed instrument over its allowed input class.

## Repetition and the independence boundary

Each pooled successful output can serve as a new input with floor $`W(w)`$. Disjoint preparations remain conditionally independent within each latent product component. Conditioning on scalar heralds and cap decisions only reweights allowed components if there is a hidden product mixture. This supplies a [finite counted recurrence](resources.md#different-noise-axes).

Without the pointwise product premise, marginal fidelities alone do not suffice. A source can choose once between three perfect copies and three copies of the same orthogonal Bell ray, with respective probabilities $`w`$ and $`1-w`$. Each marginal has the claimed overlap. Both clean Bell-orbit branches have the same success probability, so the accepted overlap remains $`w`$.

[Scientific reading route](README.md) · [Exact isotropic algebra](algebra.md) · [Fixed-block optimum near purity](near-pure-limit.md)
