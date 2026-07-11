# Appendix: Ideals and Quotient Rings in Concrete Rings

This appendix is a companion to `ring_field.md`. Sections 6–14 there develop ideals, quotient rings, and their operations abstractly; here we work the same machinery through **four concrete families of rings** that keep reappearing as examples: the integers, congruence classes, direct-product ("vector") rings, and polynomial rings. Each section gives a full classification of the ideals, worked-out ideal operations with actual numbers/polynomials, the resulting quotient rings, and which ideals are prime or maximal. Cross-references like "(ring_field.md, §11)" point back to the main document.

---

## A.1 The Integers $\mathbb{Z}$

### A.1.1 All Ideals of $\mathbb{Z}$

Every ideal of $\mathbb{Z}$ is of the form $n\mathbb{Z}$ for a unique $n \geq 0$ (ring_field.md, Example 13 and §14.2 Corollary — this is exactly the statement "$\mathbb{Z}$ is a PID"). So the ideals of $\mathbb{Z}$, listed by $n = 0, 1, 2, 3, \ldots$, are
$$\{0\} = 0\mathbb{Z} \ \subsetneq\ \cdots \ \subsetneq\ 4\mathbb{Z} \subsetneq 2\mathbb{Z} \subsetneq \mathbb{Z} = 1\mathbb{Z}, \qquad \text{and similarly for every other } n.$$
There is one ideal per non-negative integer, ordered by divisibility: $m\mathbb{Z} \subseteq n\mathbb{Z} \iff n \mid m$.

### A.1.2 Ideal Operations, Worked

Using the formulas from ring_field.md §11 ($m\mathbb{Z}+n\mathbb{Z} = \gcd(m,n)\mathbb{Z}$, $m\mathbb{Z}\cap n\mathbb{Z} = \operatorname{lcm}(m,n)\mathbb{Z}$, $m\mathbb{Z}\cdot n\mathbb{Z} = mn\mathbb{Z}$):

**Example A1 (non-coprime case).** Take $m=4, n=6$.
$$4\mathbb{Z}+6\mathbb{Z} = \gcd(4,6)\mathbb{Z} = 2\mathbb{Z}, \qquad 4\mathbb{Z}\cap 6\mathbb{Z} = \operatorname{lcm}(4,6)\mathbb{Z} = 12\mathbb{Z}, \qquad 4\mathbb{Z}\cdot 6\mathbb{Z} = 24\mathbb{Z}.$$
Check the general containment $IJ \subseteq I\cap J \subseteq I,J \subseteq I+J$: indeed $24\mathbb{Z} \subseteq 12\mathbb{Z} \subseteq 4\mathbb{Z},6\mathbb{Z} \subseteq 2\mathbb{Z}$.

**Example A2 (coprime case).** Take $m=4,n=9$ ($\gcd=1$).
$$4\mathbb{Z}+9\mathbb{Z} = \mathbb{Z}, \qquad 4\mathbb{Z}\cap 9\mathbb{Z} = 36\mathbb{Z} = 4\mathbb{Z}\cdot 9\mathbb{Z}.$$
Coprimeness collapses intersection onto product, exactly as the Remark in §11.4 predicts.

### A.1.3 Quotient Rings $\mathbb{Z}/n\mathbb{Z}$

#### What the cosets actually look like

Fix $n$, say $n=4$. The ideal is $4\mathbb{Z} = \{\ldots,-8,-4,0,4,8,\ldots\}$. Recall (§8) the coset of an integer $a$ is $a+4\mathbb{Z} = \{a+4k \mid k\in\mathbb{Z}\}$ — the two-way-infinite arithmetic progression through $a$ with common difference $4$. Concretely:
$$0+4\mathbb{Z} = \{\ldots,-8,-4,0,4,8,\ldots\}, \quad 1+4\mathbb{Z} = \{\ldots,-7,-3,1,5,9,\ldots\}, \quad 2+4\mathbb{Z} = \{\ldots,-6,-2,2,6,10,\ldots\}, \quad 3+4\mathbb{Z} = \{\ldots,-5,-1,3,7,11,\ldots\}.$$
These four sets are pairwise disjoint and their union is all of $\mathbb{Z}$ — every integer lands in exactly one, according to its remainder on division by $4$. This is exactly the general fact "$a+I=b+I \iff a-b\in I$" (§8) specialized to $I = 4\mathbb{Z}$: two integers give the *same* coset iff they differ by a multiple of $4$, i.e. iff they have the same remainder mod $4$. So although each coset is an infinite set of integers, there are only **finitely many distinct cosets** — exactly $n=4$ of them, one per possible remainder $0,1,2,3$. In general, $a+n\mathbb{Z} = b + n\mathbb{Z} \iff n \mid (a-b)$, giving exactly $n$ distinct cosets for $n\mathbb{Z}$, represented by $0,1,\ldots,n-1$.

So as a *set*,
$$\mathbb{Z}/4\mathbb{Z} = \big\{\, 0+4\mathbb{Z},\ 1+4\mathbb{Z},\ 2+4\mathbb{Z},\ 3+4\mathbb{Z} \,\big\},$$
a set with exactly $4$ elements — even though each "element" is itself an infinite subset of $\mathbb{Z}$.

#### Operations on cosets

By the general quotient-ring formulas (§8), $(a+4\mathbb{Z})+(b+4\mathbb{Z}) = (a+b)+4\mathbb{Z}$ and $(a+4\mathbb{Z})(b+4\mathbb{Z}) = ab+4\mathbb{Z}$ — add/multiply representatives, then take the coset of the result. E.g.
$$(2+4\mathbb{Z}) + (3+4\mathbb{Z}) = 5 + 4\mathbb{Z} = 1+4\mathbb{Z} \qquad(\text{since } 5 \text{ and } 1 \text{ differ by } 4),$$
$$(2+4\mathbb{Z}) \cdot (3+4\mathbb{Z}) = 6 + 4\mathbb{Z} = 2+4\mathbb{Z} \qquad(\text{since } 6 \text{ and } 2 \text{ differ by } 4).$$
Writing $\bar a := a+4\mathbb{Z}$ for brevity, the full addition and multiplication tables on $\mathbb{Z}/4\mathbb{Z} = \{\bar0,\bar1,\bar2,\bar3\}$ are:

| $+$ | $\bar0$ | $\bar1$ | $\bar2$ | $\bar3$ | | $\cdot$ | $\bar0$ | $\bar1$ | $\bar2$ | $\bar3$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $\bar0$ | $\bar0$ | $\bar1$ | $\bar2$ | $\bar3$ | | $\bar0$ | $\bar0$ | $\bar0$ | $\bar0$ | $\bar0$ |
| $\bar1$ | $\bar1$ | $\bar2$ | $\bar3$ | $\bar0$ | | $\bar1$ | $\bar0$ | $\bar1$ | $\bar2$ | $\bar3$ |
| $\bar2$ | $\bar2$ | $\bar3$ | $\bar0$ | $\bar1$ | | $\bar2$ | $\bar0$ | $\bar2$ | $\bar0$ | $\bar2$ |
| $\bar3$ | $\bar3$ | $\bar0$ | $\bar1$ | $\bar2$ | | $\bar3$ | $\bar0$ | $\bar3$ | $\bar2$ | $\bar1$ |

These are *exactly* the familiar addition/multiplication-mod-$4$ tables — which is the entire content of the isomorphism below.

#### The isomorphism $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$

The map $\bar\varphi : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}_n$, $\bar\varphi(a+n\mathbb{Z}) = a \bmod n$, sends each infinite coset to the single integer $0,\ldots,n-1$ that names it. It is exactly the map produced by the First Isomorphism Theorem (§9) applied to the reduction homomorphism $\varphi:\mathbb{Z}\to\mathbb{Z}_n$, $\varphi(k)=k\bmod n$, whose kernel is $n\mathbb{Z}$ (§5 Example) — so $\bar\varphi$ is automatically a well-defined bijective ring homomorphism, i.e. an isomorphism (this *re-derives* Example 18, rather than assuming it). Under $\bar\varphi$, the abstract "infinite coset" picture above and the everyday "arithmetic mod $n$" picture become identical: $\bar\varphi$ just relabels each coset $a+n\mathbb{Z}$ by its canonical representative $a \bmod n \in \{0,\ldots,n-1\}$, and the coset-addition/multiplication tables become the usual mod-$n$ tables.

#### Special and small cases

- $\mathbb{Z}/0\mathbb{Z} = \mathbb{Z}/\{0\}$: since $0\mathbb{Z} = \{0\}$, each coset $a+\{0\}=\{a\}$ is a single integer, so the quotient is (isomorphic to) $\mathbb{Z}$ itself — the "finest possible" quotient, collapsing nothing.
- $\mathbb{Z}/1\mathbb{Z} = \mathbb{Z}/\mathbb{Z}$: the only coset is $0+\mathbb{Z}=\mathbb{Z}$ itself, so the quotient is the one-element zero ring $\{0\}$ — the "coarsest possible" quotient, collapsing everything.
- $\mathbb{Z}/2\mathbb{Z} = \{\bar0,\bar1\} = \{\text{evens},\ \text{odds}\}$, with $\bar1+\bar1=\bar0$ — the familiar parity arithmetic.

So $n\mathbb{Z}$ acts as a "coarseness dial" with two extremes: $n=0$ collapses nothing ($\mathbb{Z}/0\mathbb{Z}\cong\mathbb{Z}$, every coset a singleton), and $n=1$ collapses everything ($\mathbb{Z}/1\mathbb{Z}=\{0\}$, one coset). For any $n\geq 1$, every coset is still an infinite set (some information about the original integer is always lost), but $|\mathbb{Z}/n\mathbb{Z}|=n$ — so larger $n$ means *more* surviving residue classes, i.e. a finer partition of $\mathbb{Z}$, closer to (but never reaching) the no-collapse extreme at $n=0$.

### A.1.4 Prime and Maximal Ideals

| $n$ | $n\mathbb{Z}$ | $\mathbb{Z}/n\mathbb{Z}$ | Prime? | Maximal? |
|---|---|---|---|---|
| $0$ | $\{0\}$ | $\mathbb{Z}$ (domain, not field) | Yes | No |
| $1$ | $\mathbb{Z}$ | $\{0\}$ | — (not proper) | — |
| $4$ | $4\mathbb{Z}$ | $\mathbb{Z}_4$ (has zero divisor $2$) | No | No |
| $6$ | $6\mathbb{Z}$ | $\mathbb{Z}_6$ (has zero divisors $2,3$) | No | No |
| $p$ prime | $p\mathbb{Z}$ | $\mathbb{Z}_p$ (field) | Yes | Yes |

This recovers Example 32 and Example 34 side by side: $\{0\}$ is the one prime ideal that is not maximal in $\mathbb{Z}$; every other prime ideal $p\mathbb{Z}$ is automatically maximal.

---

## A.2 Congruence Classes $\mathbb{Z}_n$

> **Notation warning: $n\mathbb{Z}$ vs. $\mathbb{Z}_n$.** These look similar but are different objects, easy to confuse. $n\mathbb{Z} = \{\ldots,-2n,-n,0,n,2n,\ldots\}$ (§A.1) is the *ideal of multiples of $n$* — an infinite subset of $\mathbb{Z}$. By contrast $\mathbb{Z}_n = \{0,1,\ldots,n-1\}$ (ring_field.md, Example 4) is the *ring of residues mod $n$* — a finite ring with exactly $n$ elements, none of which are "multiples of $n$" in the usual integer sense (they are the possible remainders on division by $n$). This section is entirely about ideals **inside** the finite ring $\mathbb{Z}_n$, e.g. $\langle 2\rangle = \{0,2,4,\ldots\} \subseteq \mathbb{Z}_{12}$ below consists of ordinary elements of $\mathbb{Z}_{12}$ (all less than $12$), not of multiples of $12$.

### A.2.1 The Ideal Correspondence

> **Fact.** The ideals of $\mathbb{Z}_n$ correspond bijectively to the (positive) divisors $d$ of $n$: for each $d \mid n$, the ideal generated by $d$ in $\mathbb{Z}_n$ is
> $$\langle d \rangle = \{0, d, 2d, \ldots\} \pmod n, \qquad |\langle d\rangle| = n/d.$$

This is the image, under the natural projection $\mathbb{Z} \to \mathbb{Z}_n$, of the ideal $d\mathbb{Z} \subseteq \mathbb{Z}$ — every ideal of $\mathbb{Z}_n$ arises this way because every ideal of $\mathbb{Z}$ containing $n\mathbb{Z}$ is $d\mathbb{Z}$ for some $d \mid n$ (§A.1.1), and ideals of a quotient ring $R/I$ correspond exactly to ideals of $R$ containing $I$.

**Example A3 ($\mathbb{Z}_{12}$).** The divisors of $12$ are $1,2,3,4,6,12$, giving exactly $6$ ideals:

| $d$ | $\langle d\rangle$ | size |
|---|---|---|
| $1$ | $\mathbb{Z}_{12}$ | $12$ |
| $2$ | $\{0,2,4,6,8,10\}$ | $6$ |
| $3$ | $\{0,3,6,9\}$ | $4$ |
| $4$ | $\{0,4,8\}$ | $3$ |
| $6$ | $\{0,6\}$ | $2$ |
| $12$ | $\{0\}$ | $1$ |

### A.2.2 Quotient Rings of $\mathbb{Z}_n$

> **Fact.** For $d \mid n$, $\mathbb{Z}_n / \langle d \rangle \cong \mathbb{Z}_d$, via $x + \langle d\rangle \mapsto x \bmod d$.

*Why it's well-defined:* reduction mod $d$ is well-defined on $\mathbb{Z}_n$ precisely because $d \mid n$, and its kernel is $\{x \in \mathbb{Z}_n : d \mid x\} = \langle d\rangle$.

#### What the cosets of $\mathbb{Z}_n/\langle d\rangle$ actually look like

Take $n=12$, $d=4$, so $\langle4\rangle = \{0,4,8\} \subseteq \mathbb{Z}_{12}$ (§A.2.1, Example A3). A coset of $\langle4\rangle$ in $\mathbb{Z}_{12}$ is $a + \langle4\rangle = \{a+0,\ a+4,\ a+8\} \pmod{12}$ for $a \in \mathbb{Z}_{12}$ — this time each coset is a **finite** set of size $3 = |\langle4\rangle|$ (unlike the infinite cosets of $n\mathbb{Z}$ in §A.1.3, because here we're already inside the finite ring $\mathbb{Z}_{12}$, not inside $\mathbb{Z}$). Listing all of them:
$$0+\langle4\rangle=\{0,4,8\}, \quad 1+\langle4\rangle=\{1,5,9\}, \quad 2+\langle4\rangle=\{2,6,10\}, \quad 3+\langle4\rangle=\{3,7,11\}.$$
These four sets are pairwise disjoint and their union is all $12$ elements of $\mathbb{Z}_{12}$ — exactly a partition of $\{0,1,\ldots,11\}$ into $4$ blocks of $3$, grouped by remainder mod $4$. (Compare: two elements $a,b\in\mathbb{Z}_{12}$ give the same coset of $\langle4\rangle$ iff $a-b\in\langle4\rangle$, i.e. iff $4\mid(a-b)$ in the usual integer sense — iff $a,b$ have the same remainder mod $4$.) So
$$\mathbb{Z}_{12}/\langle4\rangle = \big\{\, 0+\langle4\rangle,\ 1+\langle4\rangle,\ 2+\langle4\rangle,\ 3+\langle4\rangle \,\big\},$$
a set with exactly $4$ elements, matching $|\mathbb{Z}_{12}|/|\langle4\rangle| = 12/3 = 4$.

#### Operations, and the isomorphism to $\mathbb{Z}_4$

Cosets add/multiply via representatives, exactly as in §8 and §A.1.3:
$$(2+\langle4\rangle) + (3+\langle4\rangle) = 5+\langle4\rangle = 1+\langle4\rangle \quad (\text{since } 5 \text{ and } 1 \text{ differ by } 4),$$
$$(2+\langle4\rangle) \cdot (3+\langle4\rangle) = 6+\langle4\rangle = 2+\langle4\rangle \quad (\text{since } 6 \text{ and } 2 \text{ differ by } 4).$$
The map $\bar\varphi: \mathbb{Z}_{12}/\langle4\rangle \to \mathbb{Z}_4$ sending each coset to its remainder mod $4$,
$$0+\langle4\rangle \mapsto 0, \qquad 1+\langle4\rangle\mapsto1, \qquad 2+\langle4\rangle\mapsto2, \qquad 3+\langle4\rangle\mapsto3,$$
is exactly the reduction-mod-$4$ map descending to the quotient (First Isomorphism Theorem, §9, applied to $\mathbb{Z}_{12}\to\mathbb{Z}_4$, $x\mapsto x\bmod4$, whose kernel is $\langle4\rangle$) — the two coset computations above literally *become* $2+3=1$ and $2\cdot3=2$ in $\mathbb{Z}_4$ once you relabel by $\bar\varphi$. So, just as in §A.1.3, the "coset of $3$ finite subsets" picture and the everyday "arithmetic mod $4$" picture are the same object, viewed two ways.

**Example A4 (the other divisors of $12$).**
$$\mathbb{Z}_{12}/\langle 3\rangle \cong \mathbb{Z}_3 \ (\text{size } 12/4=3), \qquad \mathbb{Z}_{12}/\langle 6\rangle \cong \mathbb{Z}_6 \ (\text{size } 12/2=6).$$
For instance $\mathbb{Z}_{12}/\langle3\rangle$, with $\langle3\rangle=\{0,3,6,9\}$, has the $3$ cosets $0+\langle3\rangle=\{0,3,6,9\}$, $1+\langle3\rangle=\{1,4,7,10\}$, $2+\langle3\rangle=\{2,5,8,11\}$ — each of size $4$, partitioning $\mathbb{Z}_{12}$ by remainder mod $3$.

### A.2.3 Prime and Maximal Ideals, Zero Divisors

**Example A5 ($\mathbb{Z}_8$).** Divisors of $8$: $1,2,4,8$, giving ideals $\mathbb{Z}_8 \supsetneq \langle 2\rangle = \{0,2,4,6\} \supsetneq \langle 4\rangle=\{0,4\} \supsetneq \langle 8\rangle=\{0\}$.

- $\mathbb{Z}_8/\langle 2\rangle \cong \mathbb{Z}_2$, a **field** $\implies \langle 2\rangle$ is prime and maximal.
- $\mathbb{Z}_8/\langle 4\rangle \cong \mathbb{Z}_4$, which has the zero divisor $2$ ($2\cdot 2 = 0$) $\implies \langle 4\rangle$ is **neither** prime nor maximal.
- $\mathbb{Z}_8/\{0\} = \mathbb{Z}_8$ itself has zero divisors ($2 \cdot 4 = 8 \equiv 0$) $\implies \{0\}$ is **not prime** in $\mathbb{Z}_8$.

So $\langle 2\rangle$ is the *only* nonzero proper ideal of $\mathbb{Z}_8$ that is prime — and it is automatically maximal. This is not a coincidence:

> **Remark.** In $\mathbb{Z}_n$ (or any finite commutative ring with unity), every prime ideal is automatically maximal. Reason: if $P$ is prime, $\mathbb{Z}_n/P$ is a finite integral domain, hence a field by the theorem "every finite integral domain is a field" (ring_field.md, §10) — so $P$ is maximal by the Maximal Ideal Criterion (§13.2). Contrast with $\mathbb{Z}$ itself (infinite), where $\{0\}$ is prime but not maximal.

### A.2.4 A Chinese Remainder Theorem Example

**Example A6.** In $\mathbb{Z}_{12}$, take $I=\langle 3\rangle=\{0,3,6,9\}$ and $J=\langle 4\rangle=\{0,4,8\}$. Since $9 \in I$ and $4 \in J$ with $9+4=13\equiv 1 \pmod{12}$, we get $1 \in I+J$, i.e. $I+J=\mathbb{Z}_{12}$ (coprime). Also $I \cap J = \{0\}$ (the only common multiple of $3$ and $4$ below $12$ is $0$). CRT (§12) gives
$$\mathbb{Z}_{12}/\{0\} = \mathbb{Z}_{12} \ \cong\ \mathbb{Z}_{12}/\langle 3\rangle \oplus \mathbb{Z}_{12}/\langle 4\rangle \ \cong\ \mathbb{Z}_3 \oplus \mathbb{Z}_4,$$
matching Example 29/31 with $m=3,n=4$.

---

## A.3 Direct-Product ("Vector") Rings

Here the ring is a **finite Cartesian product** $R_1 \oplus \cdots \oplus R_n$ with componentwise operations (ring_field.md §12) — e.g. $\mathbb{Z}\oplus\mathbb{Z}$, or $F^n$ for a field $F$, thought of as "vectors" of ring elements added and multiplied entrywise.

### A.3.1 Classification of Ideals in $R_1 \oplus R_2$

> **Theorem.** Let $R_1, R_2$ be rings with unity. Every ideal of $R_1 \oplus R_2$ is of the form $I_1 \oplus I_2$ for (unique) ideals $I_1 \trianglelefteq R_1$, $I_2 \trianglelefteq R_2$.

**Proof.** Let $J \trianglelefteq R_1\oplus R_2$. Define $I_1 = \{a \in R_1 \mid (a,0) \in J\}$ and $I_2 = \{b\in R_2 \mid (0,b)\in J\}$; these are ideals of $R_1,R_2$ respectively (routine check, using that $J$ absorbs multiplication by any ring element, in particular by $(1,0)$ and $(0,1)$).

If $(a,b) \in J$, multiplying by $(1,0) \in R_1\oplus R_2$ gives $(a,0) = (a,b)\cdot(1,0) \in J$, so $a \in I_1$; similarly $b \in I_2$. Hence $J \subseteq I_1\oplus I_2$.

Conversely if $a\in I_1, b\in I_2$, then $(a,0),(0,b)\in J$, so $(a,b)=(a,0)+(0,b)\in J$. Hence $I_1\oplus I_2 \subseteq J$. So $J = I_1\oplus I_2$. $\square$

> **Lemma (quotient of a product).** $(R_1\oplus R_2)/(I_1\oplus I_2) \cong (R_1/I_1)\oplus(R_2/I_2)$.

*Proof.* The map $(a,b)\mapsto(a+I_1,\,b+I_2)$ is a surjective ring homomorphism $R_1\oplus R_2 \to (R_1/I_1)\oplus(R_2/I_2)$ with kernel exactly $I_1\oplus I_2$; apply the First Isomorphism Theorem (§9). $\square$

### A.3.2 Worked Examples

**Example A7.** In $\mathbb{Z}\oplus\mathbb{Z}$, take $I = 2\mathbb{Z}\oplus 3\mathbb{Z}$. Then
$$(\mathbb{Z}\oplus\mathbb{Z})/(2\mathbb{Z}\oplus 3\mathbb{Z}) \cong \mathbb{Z}_2 \oplus \mathbb{Z}_3.$$
Note this ideal $I$ is *different* from a "diagonal" ideal like $\{(2k,2k)\mid k\in\mathbb{Z}\}$ — the latter is **not** an ideal of $\mathbb{Z}\oplus\mathbb{Z}$ at all (it fails absorption: $(1,0)\cdot(2,2) = (2,0) \notin$ the diagonal set), which is a useful check that the classification theorem's ideals really are the *only* ones.

### A.3.3 Prime and Maximal Ideals

A product of two nonzero rings always has zero divisors: $(1,0)\cdot(0,1) = (0,0)$ (Example 30). So $(R_1/I_1)\oplus(R_2/I_2)$ can be a field or an integral domain only if **one factor collapses entirely** (equals the zero ring) and the other becomes a field/domain.

> **Consequence.** The maximal ideals of $R_1\oplus R_2$ are exactly
> $$M_1 \oplus R_2 \ \ (M_1 \text{ maximal in } R_1), \qquad \text{and} \qquad R_1 \oplus M_2 \ \ (M_2 \text{ maximal in } R_2).$$
> Likewise the prime ideals are exactly $P_1\oplus R_2$ ($P_1$ prime in $R_1$) and $R_1\oplus P_2$ ($P_2$ prime in $R_2$).

**Example A8.** In $\mathbb{Z}\oplus\mathbb{Z}$: $2\mathbb{Z}\oplus\mathbb{Z}$ is maximal, with quotient $(\mathbb{Z}\oplus\mathbb{Z})/(2\mathbb{Z}\oplus\mathbb{Z}) \cong \mathbb{Z}_2\oplus\{0\} \cong \mathbb{Z}_2$, a field. Meanwhile $\{0\}\oplus\mathbb{Z}$ is **prime but not maximal**: its quotient is $\mathbb{Z}\oplus\{0\} \cong \mathbb{Z}$, an integral domain but not a field — mirroring the fact that $\{0\}$ is prime-not-maximal in $\mathbb{Z}$ itself (§A.1.4).

### A.3.4 $F^n$: the Coordinate-Subset Ideals

For a field $F$, apply the classification theorem repeatedly to $F^n = F\oplus\cdots\oplus F$. Since $F$ is simple (Example 16 — its only ideals are $\{0\}$ and $F$), every ideal of $F^n$ is a choice, independently in each coordinate, of "$\{0\}$" or "$F$":
$$I_S = \{(a_1,\ldots,a_n) \mid a_i = 0 \text{ for } i \notin S\}, \qquad S \subseteq \{1,\ldots,n\}.$$
This gives exactly $2^n$ ideals of $F^n$.

**Example A9.** $F^3$ has $2^3=8$ ideals; e.g. $S=\{1,3\}$ gives $I_S = F\times\{0\}\times F$.

The **maximal** ideals are those with $|S|=n-1$ (a single coordinate zeroed out), i.e. $S = \{1,\ldots,n\}\setminus\{i\}$ — these are exactly $\ker \pi_i$ for the projection maps of §12, with quotient $F^n/I_S \cong F$. There are exactly $n$ maximal ideals of $F^n$, one per coordinate.

---

## A.4 Polynomial Rings

### A.4.1 $k[x]$ (Field Coefficients) is a PID

For a field $k$, every ideal of $k[x]$ is $\langle f(x)\rangle$ for a polynomial $f$, unique up to a nonzero constant multiple — equivalently, unique if we insist $f$ is **monic** (ring_field.md §14.2). We now give a concrete Chinese Remainder Theorem computation with such ideals, and then contrast with $\mathbb{Z}[x]$, which is *not* a PID.

### A.4.2 A Concrete CRT Example in $\mathbb{R}[x]$

**Example A10.** Let $f_1 = x-1$ and $f_2 = x+1$ in $\mathbb{R}[x]$.

*Coprimeness:* $\tfrac12(x+1) - \tfrac12(x-1) = 1$, so $1 \in \langle x-1\rangle + \langle x+1\rangle$, giving $\langle x-1\rangle+\langle x+1\rangle = \mathbb{R}[x]$.

*Intersection = product:* by coprimeness (§11.4), $\langle x-1\rangle\cap\langle x+1\rangle = \langle x-1\rangle\langle x+1\rangle = \langle (x-1)(x+1)\rangle = \langle x^2-1\rangle$.

*Quotients:* the evaluation map $f \mapsto f(1)$ has kernel exactly $\langle x-1\rangle$ (the minimal polynomial of the "point" $1$, ring_field.md §14.6), so $\mathbb{R}[x]/\langle x-1\rangle \cong \mathbb{R}$; likewise $\mathbb{R}[x]/\langle x+1\rangle \cong \mathbb{R}$ via evaluation at $-1$.

*CRT conclusion:*
$$\mathbb{R}[x]/\langle x^2-1\rangle \ \cong\ \mathbb{R}[x]/\langle x-1\rangle \ \oplus\ \mathbb{R}[x]/\langle x+1\rangle \ \cong\ \mathbb{R}\oplus\mathbb{R}, \qquad f + \langle x^2-1\rangle \ \longmapsto\ (f(1),\,f(-1)).$$
This is the exact polynomial analogue of $\mathbb{Z}_{mn}\cong\mathbb{Z}_m\oplus\mathbb{Z}_n$ (Example 31) — same theorem, same proof, different ring.

*The CRT "selector" made explicit:* given target $(r_1,r_2) \in \mathbb{R}\oplus\mathbb{R}$, the preimage is the (Lagrange-interpolating) linear polynomial
$$f(x) = r_1\cdot\frac{x+1}{2} + r_2\cdot\frac{1-x}{2},$$
which satisfies $f(1)=r_1, f(-1)=r_2$ — precisely the elements $e_1 = \tfrac{x+1}{2}$ ($\equiv 1$ mod $x-1$, $\equiv 0$ mod $x+1$) and $e_2 = \tfrac{1-x}{2}$ from the general CRT construction (ring_field.md §12, Step 4).

### A.4.3 $\mathbb{Z}[x]$ is NOT a PID

**Example A11.** Consider $I = \langle 2, x\rangle = \{2g(x) + xh(x) \mid g,h \in \mathbb{Z}[x]\} \trianglelefteq \mathbb{Z}[x]$.

*Concrete description:* $I = \{f \in \mathbb{Z}[x] \mid f(0) \text{ is even}\}$. Indeed, any $2g+xh$ has constant term $2g(0)$, even; conversely if $f = c_0+c_1x+\cdots$ has $c_0=2c_0'$ even, then $f = 2c_0' + x(c_1+c_2x+\cdots) \in I$.

*Quotient:* the map $\mathbb{Z}[x] \to \mathbb{Z}_2$, $f \mapsto f(0) \bmod 2$, is a surjective ring homomorphism with kernel exactly $I$, so $\mathbb{Z}[x]/I \cong \mathbb{Z}_2$, a **field** — hence $I$ is maximal (and prime).

*$I$ is not principal.* Suppose $I = \langle g(x)\rangle$ for some $g$. Since $2 \in I$, $g \mid 2$, so $2 = g\cdot h$ for some $h \in \mathbb{Z}[x]$; as $\mathbb{Z}[x]$ is an integral domain, $\deg g + \deg h = \deg 2 = 0$, forcing $\deg g = 0$, i.e. $g$ is an integer constant with $g \mid 2$, so $g \in \{\pm1,\pm2\}$. Since $x \in I = \langle g\rangle$, also $g \mid x$; but a nonzero integer constant $g$ divides the polynomial $x$ (i.e. $x = g\cdot k(x)$) only if $g \mid 1$ (compare coefficients of $x^1$), forcing $g = \pm1$. But then $\langle g\rangle = \mathbb{Z}[x]$, contradicting that $I$ is a proper ideal (e.g. $1 \notin I$, since $1$ has odd constant term). No single $g$ works, so $I$ is **not principal**.

> **Conclusion.** $\mathbb{Z}[x]$ is an integral domain in which not every ideal is principal — so $\mathbb{Z}[x]$ is **not a PID**, even though both $\mathbb{Z}$ and $k[x]$ (for $k$ a field) individually are. Principality of $k[x]$'s ideals relied on the division algorithm (§14.2), which in turn relied on $k$ being a field (invertible leading coefficients) — exactly the ingredient missing in $\mathbb{Z}[x]$.

### A.4.4 A Finite-Field Polynomial CRT Check

**Example A12.** In $\mathbb{F}_2[x] = \mathbb{Z}_2[x]$, take $f_1 = x$, $f_2 = x+1$.

*Coprime:* $(x+1) - x = 1 \in \langle x\rangle+\langle x+1\rangle$, so the sum is all of $\mathbb{F}_2[x]$.

*Intersection = product:* $\langle x\rangle \cap \langle x+1\rangle = \langle x(x+1)\rangle = \langle x^2+x\rangle$ (recall $x^2 - x = x^2+x$ in characteristic $2$).

*CRT:* $\mathbb{F}_2[x]/\langle x^2+x\rangle \cong \mathbb{F}_2[x]/\langle x\rangle \oplus \mathbb{F}_2[x]/\langle x+1\rangle \cong \mathbb{F}_2 \oplus \mathbb{F}_2$ (evaluation at $0$ and at $1$ respectively). Both sides have exactly $4$ elements: the left side because $\deg(x^2+x)=2$ gives $2^2=4$ coset representatives (§14.5), the right side because $|\mathbb{F}_2\oplus\mathbb{F}_2| = 2\cdot2=4$. A useful sanity check that the abstract isomorphism is size-consistent.

---

## A.5 Summary Table

| Ring | All ideals | Quotient by ideal | Prime $\iff$ | Maximal $\iff$ |
|---|---|---|---|---|
| $\mathbb{Z}$ | $n\mathbb{Z}$, $n \geq 0$ | $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$ | $n=0$ or $n$ prime | $n$ prime |
| $\mathbb{Z}_n$ | $\langle d\rangle$, $d \mid n$ | $\mathbb{Z}_n/\langle d\rangle \cong \mathbb{Z}_d$ | $d$ prime (automatically maximal — §A.2.3) | $d$ prime |
| $R_1\oplus R_2$ | $I_1\oplus I_2$ | $(R_1/I_1)\oplus(R_2/I_2)$ | $P_1\oplus R_2$ or $R_1\oplus P_2$ | $M_1\oplus R_2$ or $R_1\oplus M_2$ |
| $k[x]$, $k$ a field | $\langle f\rangle$, $f$ monic | $k[x]/\langle f\rangle$ | $f=0$ or $f$ irreducible | $f$ irreducible |
| $\mathbb{Z}[x]$ | *not all principal* (e.g. $\langle 2,x\rangle$) | e.g. $\mathbb{Z}[x]/\langle 2,x\rangle \cong \mathbb{Z}_2$ | — | — |

The recurring theme: whenever the base ring is a field (so its polynomial ring or its finite quotients admit a division algorithm), ideal theory reduces to a clean divisor/factorization combinatorics — sizes, gcd/lcm, irreducibility — and quotients are computed by evaluation or reduction maps. $\mathbb{Z}[x]$'s failure to be a PID is the appendix's one cautionary example showing this combinatorics can break down once *both* "dimensions" (integer coefficients *and* a polynomial variable) are present at once.
