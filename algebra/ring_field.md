# Rings and Fields

## 1. Rings

### Definition

A **ring** is a set $R$ equipped with two binary operations, addition $(+)$ and multiplication $(\cdot)$, satisfying the following axioms:

**Under addition, $(R, +)$ is an abelian group:**

1. **(Closure)** For all $a, b \in R$, $a + b \in R$.
2. **(Associativity)** For all $a, b, c \in R$, $(a + b) + c = a + (b + c)$.
3. **(Identity)** There exists $0 \in R$ such that $a + 0 = 0 + a = a$ for all $a \in R$.
4. **(Inverses)** For each $a \in R$, there exists $-a \in R$ such that $a + (-a) = 0$.
5. **(Commutativity)** For all $a, b \in R$, $a + b = b + a$.

**Under multiplication, $(R, \cdot)$ is a semigroup:**

6. **(Closure)** For all $a, b \in R$, $a \cdot b \in R$.
7. **(Associativity)** For all $a, b, c \in R$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.

**Multiplication distributes over addition:**

8. **(Left distributivity)** $a \cdot (b + c) = a \cdot b + a \cdot c$.
9. **(Right distributivity)** $(a + b) \cdot c = a \cdot c + b \cdot c$.

> **Note:** We do not require multiplication to be commutative, nor do we require a multiplicative identity $1$. If multiplication is commutative, $R$ is called a **commutative ring**. If $R$ has a multiplicative identity, it is called a **ring with unity** (or **unital ring**).

### Examples

**Example 1.** The integers $\mathbb{Z}$ with the usual addition and multiplication form a commutative ring with unity.

**Example 2.** The set of $n \times n$ matrices over $\mathbb{R}$, denoted $M_n(\mathbb{R})$, is a ring under matrix addition and multiplication. It is **not** commutative for $n \geq 2$.

**Example 3.** The set $2\mathbb{Z} = \{\ldots, -4, -2, 0, 2, 4, \ldots\}$ of even integers is a commutative ring **without** unity.

**Example 4.** $\mathbb{Z}_n = \{0, 1, \ldots, n-1\}$ with addition and multiplication modulo $n$ is a commutative ring with unity.

---

## 2. Fields

### Definition

A **field** (域) is a set $F$ equipped with two binary operations $+$ and $\cdot$ such that:

1. $(F, +, \cdot)$ is a commutative ring with unity ($1 \neq 0$).
2. Every non-zero element has a multiplicative inverse: for all $a \in F$ with $a \neq 0$, there exists $a^{-1} \in F$ such that $a \cdot a^{-1} = 1$.

Equivalently, $(F \setminus \{0\}, \cdot)$ is an abelian group.

### Examples

- $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are fields under the usual operations.
- $\mathbb{Z}_p$ for any prime $p$ is a field (finite field with $p$ elements).
- $\mathbb{Z}$ is **not** a field: $2$ has no multiplicative inverse in $\mathbb{Z}$.

### Fields vs. Rings

A field is a ring with one extra requirement — every non-zero element is invertible. Dropping that requirement opens up a much richer world of examples ($\mathbb{Z}$, matrix rings, polynomial rings). The hierarchy from most general to most structured:

| Structure | Commutative $+$ | Assoc. $\cdot$ | Unity | No zero divisors | Every non-zero invertible |
|---|:---:|:---:|:---:|:---:|:---:|
| Ring | Yes | Yes | Not required | No | No |
| Commutative ring with unity | Yes | Yes | Yes | No | No |
| Integral domain | Yes | Yes | Yes | **Yes** | No |
| Field | Yes | Yes | Yes | Yes | **Yes** |

---

## 3. Subrings

### Definition

Let $(R, +, \cdot)$ be a ring. A non-empty subset $R_1 \subseteq R$ is called a **subring** of $R$ if $R_1$ itself forms a ring under the same operations inherited from $R$.

### Theorem (Subring Criterion)

> **Theorem.** Let $R$ be a ring and $R_1$ a non-empty subset of $R$. Then $R_1$ is a subring of $R$ if and only if:
>
> 1. For all $a, b \in R_1$, $a - b \in R_1$.
> 2. For all $a, b \in R_1$, $a \cdot b \in R_1$.

**Proof.**

$(\Rightarrow)$ Suppose $R_1$ is a subring of $R$. Then $(R_1, +)$ is a subgroup of $(R, +)$, so by the subgroup criterion, $a, b \in R_1$ implies $a - b \in R_1$. Closure under multiplication holds by definition, so $a \cdot b \in R_1$.

$(\Leftarrow)$ Suppose conditions (1) and (2) hold. We verify the ring axioms for $R_1$:

- **Additive identity:** Since $R_1 \neq \emptyset$, pick any $a \in R_1$. By (1), $a - a = 0 \in R_1$.
- **Additive inverses:** For any $a \in R_1$, we have $0, a \in R_1$, so $0 - a = -a \in R_1$.
- **Closure under addition:** For $a, b \in R_1$, we have $-b \in R_1$, so $a - (-b) = a + b \in R_1$.
- **Associativity, commutativity of addition, distributivity:** These are inherited from $R$ and hold for all elements in $R$, hence for all elements in $R_1 \subseteq R$.
- **Closure under multiplication:** Given by condition (2). $\square$

> **Remark.** Conditions (1) and (2) are independent — neither implies the other. For example, $\mathbb{Z}$ satisfies (1) trivially but we still need (2) to ensure products stay in the ring.

### Why $a - b$, not $a + b$?

One might ask: why does condition (1) use subtraction rather than the more natural-looking $a + b \in R_1$?

The reason is efficiency. Requiring only $a + b \in R_1$ gives closure under addition, but says nothing about whether $0$ or $-a$ are in $R_1$ — you would need those as separate conditions. The subtraction condition encodes all three at once:

- **Identity:** Pick any $a \in R_1$ (possible since $R_1 \neq \emptyset$). Then $a - a = 0 \in R_1$.
- **Inverses:** Now $0 \in R_1$, so for any $b \in R_1$: $0 - b = -b \in R_1$.
- **Closure under $+$:** For any $a, b \in R_1$, we have $-b \in R_1$, so $a - (-b) = a + b \in R_1$.

Thus $a - b \in R_1$ is a single condition from which the entire subgroup structure of $(R_1, +)$ follows by a short chain of deductions. This is the same idea as the **subgroup criterion** in group theory.

### Examples

**Example 5.** $\mathbb{Z}$ is a subring of $\mathbb{Q}$, which is a subring of $\mathbb{R}$, which is a subring of $\mathbb{C}$.

*Verification:* For any $a, b \in \mathbb{Z}$, we have $a - b \in \mathbb{Z}$ and $a \cdot b \in \mathbb{Z}$. Both subring conditions hold. $\checkmark$

**Example 6.** The set $n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}$ of multiples of a fixed integer $n$ is a subring of $\mathbb{Z}$.

*Verification:* If $a = nj$ and $b = nk$, then $a - b = n(j-k) \in n\mathbb{Z}$ and $a \cdot b = n(njk) \in n\mathbb{Z}$. $\checkmark$

**Example 7.** $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$, the **Gaussian integers**, is a subring of $\mathbb{C}$.

*Verification:* For $\alpha = a + bi$ and $\beta = c + di$ in $\mathbb{Z}[i]$:
$$\alpha - \beta = (a-c) + (b-d)i \in \mathbb{Z}[i], \qquad \alpha \cdot \beta = (ac - bd) + (ad + bc)i \in \mathbb{Z}[i]. \checkmark$$

**Example 8 (subring).** $S = \{0, 2, 4\} \subset \mathbb{Z}_6$ is a subring of $\mathbb{Z}_6$.

*Verification:* Differences mod 6: $2 - 4 \equiv 4$, $4 - 2 = 2$, $0 - 2 \equiv 4$, etc. — all land in $S$. Products: $2 \cdot 2 = 4$, $2 \cdot 4 \equiv 2$, $4 \cdot 4 \equiv 4$, and anything times $0$ is $0$. Both conditions hold. $\checkmark$

**Non-example.** $T = \{1, 2\} \subset \mathbb{Z}_3$ is **not** a subring.

*Verification:* Condition (1) fails immediately: $2 - 2 = 0 \notin T$. Since $T$ does not contain the additive identity, it cannot be a subring. $\times$

---

### Summary

| Property | Ring $R$ | Subring $R_1 \subseteq R$ |
|---|---|---|
| Closed under $+$ | Yes | Yes (follows from criterion 1) |
| Closed under $-$ | Yes | Yes (criterion 1) |
| Has $0$ | Yes | Yes (follows from criterion 1) |
| Closed under $\cdot$ | Yes | Yes (criterion 2) |
| Commutative $+$ | Yes | Yes (inherited) |
| Associative $\cdot$ | Yes | Yes (inherited) |
| Has $1$ | Not required | Not required (may differ from $R$'s unity) |

---

## 4. Ring Homomorphisms

### Definition

Let $(R, +, \cdot)$ and $(S, \oplus, \odot)$ be rings. A map $\varphi : R \to S$ is called a **ring homomorphism** if it preserves both operations:

1. $\varphi(a + b) = \varphi(a) \oplus \varphi(b)$ for all $a, b \in R$,
2. $\varphi(a \cdot b) = \varphi(a) \odot \varphi(b)$ for all $a, b \in R$.

In words: $\varphi$ carries sums to sums and products to products. It is a structure-preserving map between rings.

> **Immediate consequences.** If $\varphi : R \to S$ is a ring homomorphism, then:
> - $\varphi(0_R) = 0_S$ (homomorphisms send the zero of $R$ to the zero of $S$).
> - $\varphi(-a) = -\varphi(a)$ for all $a \in R$.
>
> Both follow from condition (1) alone, by the same argument as for group homomorphisms.

### Terminology

| Name | Chinese | Condition |
|---|---|---|
| **Homomorphism** | 同态 | Structure-preserving map (as above) |
| **Monomorphism** | 单同态 | Injective homomorphism |
| **Epimorphism** | 满同态 | Surjective homomorphism |
| **Isomorphism** | 同构 | Bijective homomorphism; we write $R \cong S$ |
| **Endomorphism** | 自同态 | Homomorphism from $R$ to itself |
| **Automorphism** | 自同构 | Bijective endomorphism |

### Examples

**Example 9.** The map $\varphi : \mathbb{Z} \to \mathbb{Z}_n$ defined by $\varphi(k) = k \bmod n$ is a ring homomorphism (the **reduction mod $n$** map).

*Verification:* $\varphi(a + b) = (a+b) \bmod n = (a \bmod n) + (b \bmod n) = \varphi(a) + \varphi(b)$, and similarly for products. $\checkmark$

**Example 10.** The **inclusion map** $\iota : \mathbb{Z} \hookrightarrow \mathbb{Q}$ defined by $\iota(n) = n$ is a ring monomorphism.

**Example 11.** Complex conjugation $\varphi : \mathbb{C} \to \mathbb{C}$, $\varphi(a + bi) = a - bi$, is a ring automorphism.

*Verification:* $\overline{z + w} = \bar{z} + \bar{w}$ and $\overline{zw} = \bar{z}\bar{w}$. It is its own inverse, so it is bijective. $\checkmark$

**Example 12 (epimorphism).** The **evaluation map** $\varphi : \mathbb{Z}[x] \to \mathbb{Z}$ defined by $\varphi(f) = f(0)$ is an epimorphism.

**What is $\mathbb{Z}[x]$?** The notation $\mathbb{Z}[x]$ denotes the ring of all polynomials in one variable $x$ with integer coefficients:
$$\mathbb{Z}[x] = \{ a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n \mid n \geq 0,\ a_i \in \mathbb{Z} \}.$$
For example, $3 - 2x + 5x^3 \in \mathbb{Z}[x]$. Addition and multiplication are the usual polynomial operations; the coefficients are computed in $\mathbb{Z}$.

**What does $\varphi$ do?** Given a polynomial $f(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n$, the map $\varphi$ substitutes $x = 0$ and returns the result:
$$\varphi(f) = f(0) = a_0 + a_1 \cdot 0 + a_2 \cdot 0^2 + \cdots + a_n \cdot 0^n = a_0.$$
So $\varphi$ simply **reads off the constant term** of the polynomial. For example:
$$\varphi(3 - 2x + 5x^3) = 3, \qquad \varphi(7) = 7, \qquad \varphi(x^2 + x) = 0.$$

It is called an "evaluation map" because it evaluates the polynomial at the specific point $x = 0$. More generally, for any fixed $c \in \mathbb{Z}$, the map $f \mapsto f(c)$ is a ring homomorphism $\mathbb{Z}[x] \to \mathbb{Z}$; our example is the special case $c = 0$.

*Verification of homomorphism:* For $f, g \in \mathbb{Z}[x]$, $(f+g)(0) = f(0) + g(0)$ and $(fg)(0) = f(0)g(0)$. $\checkmark$

*Surjective:* Every $n \in \mathbb{Z}$ is the image of the constant polynomial $n \in \mathbb{Z}[x]$. $\checkmark$

*Not injective:* $\varphi(x) = 0 = \varphi(0)$ but $x \neq 0$, so $\varphi$ is not injective. The kernel is $\ker\varphi = \{f \in \mathbb{Z}[x] \mid f(0) = 0\} = x\mathbb{Z}[x]$, the set of polynomials with zero constant term.

**Non-example.** The map $\varphi : \mathbb{Z} \to \mathbb{Z}$ defined by $\varphi(n) = 2n$ is **not** a ring homomorphism: $\varphi(1 \cdot 1) = 2$ but $\varphi(1) \cdot \varphi(1) = 4$.

---

## 5. The Kernel of a Homomorphism

### Definition

Let $\varphi : R \to S$ be a ring homomorphism. The **kernel** of $\varphi$ is the set of elements in $R$ that map to the zero of $S$:

$$\ker \varphi = \{ a \in R \mid \varphi(a) = 0_S \}.$$

### Properties

**Proposition.** Let $\varphi : R \to S$ be a ring homomorphism. Then:

1. $\ker \varphi$ is a subring of $R$.
2. $\ker \varphi$ is **closed under multiplication by arbitrary elements of $R$**: for any $r \in R$ and $a \in \ker \varphi$, both $r \cdot a \in \ker \varphi$ and $a \cdot r \in \ker \varphi$.
3. $\varphi$ is injective if and only if $\ker \varphi = \{0_R\}$.

**Proof of (1).** We apply the subring criterion. Since $\varphi(0_R) = 0_S$, we have $0_R \in \ker\varphi$, so it is non-empty. For $a, b \in \ker\varphi$:
$$\varphi(a - b) = \varphi(a) - \varphi(b) = 0_S - 0_S = 0_S \implies a - b \in \ker\varphi.$$
$$\varphi(a \cdot b) = \varphi(a) \cdot \varphi(b) = 0_S \cdot 0_S = 0_S \implies a \cdot b \in \ker\varphi.$$
Both subring conditions hold. $\square$

**Proof of (2).** For $r \in R$ and $a \in \ker\varphi$:
$$\varphi(r \cdot a) = \varphi(r) \cdot \varphi(a) = \varphi(r) \cdot 0_S = 0_S.$$
Hence $r \cdot a \in \ker\varphi$, and similarly $a \cdot r \in \ker\varphi$. $\square$

**Proof of (3).** $(\Rightarrow)$ If $\varphi$ is injective and $\varphi(a) = 0_S = \varphi(0_R)$, then $a = 0_R$. $(\Leftarrow)$ If $\ker\varphi = \{0_R\}$ and $\varphi(a) = \varphi(b)$, then $\varphi(a - b) = 0_S$, so $a - b \in \ker\varphi = \{0_R\}$, giving $a = b$. $\square$

> **Remark.** Property (2) says the kernel is more than a subring — it absorbs multiplication from outside. A subring with this property is called an **ideal**. Every kernel is an ideal, and conversely every ideal is the kernel of some homomorphism. This is the starting point of ideal theory, which we develop in the next section.

### Example

For $\varphi : \mathbb{Z} \to \mathbb{Z}_n$ (reduction mod $n$):
$$\ker\varphi = \{ k \in \mathbb{Z} \mid k \equiv 0 \pmod{n} \} = n\mathbb{Z}.$$
This is consistent with Example 6: $n\mathbb{Z}$ is indeed a subring of $\mathbb{Z}$, and it absorbs multiplication — if $n \mid a$ and $r \in \mathbb{Z}$, then $n \mid ra$.

---

## 6. Ideals

### Motivation

The kernel of any ring homomorphism (Section 5) is not just a subring — it also absorbs multiplication from outside. This extra property is what defines an ideal.

### Definition

Let $R$ be a ring and $I$ a non-empty subset of $R$.

- $I$ is a **left ideal** of $R$ if:
  1. For all $a, b \in I$, $a - b \in I$.
  2. For all $r \in R$ and $a \in I$, $r \cdot a \in I$.

- $I$ is a **right ideal** of $R$ if:
  1. For all $a, b \in I$, $a - b \in I$.
  2. For all $r \in R$ and $a \in I$, $a \cdot r \in I$.

- $I$ is a **(two-sided) ideal** of $R$ if it is both a left ideal and a right ideal.

We write $I \trianglelefteq R$ to indicate that $I$ is a two-sided ideal of $R$.

> **Comparison with subrings.** A subring requires closure under multiplication within $I$ (i.e., $a, b \in I \Rightarrow ab \in I$). An ideal requires the stronger condition that $I$ absorbs multiplication by any element of $R$ from outside. Every ideal is a subring, but not every subring is an ideal.

> **Left vs. right.** The distinction between left and right ideals only matters in non-commutative rings. If $R$ is commutative, every left ideal is automatically a right ideal, so "left", "right", and "two-sided" all coincide.

### Examples

**Example 13.** For any integer $n$, the set $n\mathbb{Z} = \{nk \mid k \in \mathbb{Z}\}$ is an ideal of $\mathbb{Z}$.

*Verification:* We already know $n\mathbb{Z}$ is a subring. For absorption: if $a = nk \in n\mathbb{Z}$ and $r \in \mathbb{Z}$, then $r \cdot a = n(rk) \in n\mathbb{Z}$. Since $\mathbb{Z}$ is commutative, this is simultaneously a left and right ideal. $\checkmark$

In fact, **every ideal of $\mathbb{Z}$ is of this form** — $\mathbb{Z}$ is a principal ideal domain, a fact we will revisit later.

**Example 14.** In the matrix ring $M_2(\mathbb{R})$, consider the set
$$I = \left\{ \begin{pmatrix} a & 0 \\ b & 0 \end{pmatrix} \mid a, b \in \mathbb{R} \right\}.$$
This is a **left ideal** but **not** a right ideal of $M_2(\mathbb{R})$.

*Left absorption:* For any $M \in M_2(\mathbb{R})$ and $A \in I$, one checks that $MA \in I$ (the second column of $MA$ is zero). $\checkmark$

*Not a right ideal:* Take $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \in I$ and $M = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Then $AM = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \notin I$. $\times$

**Example 15.** The kernel of any ring homomorphism $\varphi : R \to S$ is a two-sided ideal of $R$.

This was proved in Section 5 (Property 2 of kernels). Conversely, every two-sided ideal arises as a kernel — the quotient ring construction $R/I$ makes this precise.

### Trivial Ideals

Every ring $R$ has two ideals that are always present:

- $\{0\}$, the **zero ideal**.
- $R$ itself.

These are called the **trivial ideals** of $R$. A non-zero ring in which these are the only two-sided ideals is called a **simple ring** (defined below).

---

## 7. Simple Rings

### Definition

A non-zero ring $R$ is called **simple** if its only two-sided ideals are $\{0\}$ and $R$ itself.

Intuitively, a simple ring has no non-trivial "internal structure" that can be detected by ideals — it cannot be "collapsed" by a non-trivial homomorphism while preserving ring structure.

> **Connection to homomorphisms.** Since every kernel is a two-sided ideal, the only homomorphisms out of a simple ring $R$ are:
> - The **zero map** $\varphi(r) = 0$ for all $r$ (kernel $= R$), and
> - **Injective maps** (kernel $= \{0\}$).
>
> A simple ring cannot have a "partial collapse" — any homomorphism is either trivial or injective.

### Examples

**Example 16.** Every field $F$ is a simple ring (viewed as a commutative ring).

*Proof.* Let $I \trianglelefteq F$ with $I \neq \{0\}$. Pick any non-zero $a \in I$. Since $F$ is a field, $a^{-1} \in F$, and by the absorption property of the ideal: $a^{-1} \cdot a = 1 \in I$. Then for any $r \in F$: $r = r \cdot 1 \in I$. Hence $I = F$. $\square$

**Example 17.** The matrix ring $M_n(F)$ over a field $F$ is simple for any $n \geq 1$.

This is a classical result (Artin–Wedderburn theory). The key idea is that any non-zero ideal must contain an invertible matrix, from which one can generate all of $M_n(F)$ using the absorption property.

**Non-example.** $\mathbb{Z}$ is **not** simple: $2\mathbb{Z}$ is a non-trivial ideal.

**Non-example.** $\mathbb{Z}_6$ is **not** simple: $\{0, 2, 4\}$ is a non-trivial ideal (recall Example 8).

---

## 8. Quotient Rings

### Motivation

Given a two-sided ideal $I \trianglelefteq R$, we want to build a new ring by "collapsing $I$ to zero." The construction mirrors quotient groups: we partition $R$ into cosets of $I$ and define ring operations on those cosets.

### Cosets

For $a \in R$, the **coset** of $a$ modulo $I$ is:
$$a + I = \{ a + x \mid x \in I \} \subseteq R.$$

Two cosets are either identical or disjoint: $a + I = b + I$ if and only if $a - b \in I$.

The set of all cosets is denoted:
$$R/I = \{ a + I \mid a \in R \}.$$

### Definition

Let $I \trianglelefteq R$ be a two-sided ideal. The **quotient ring** (商环) $R/I$ is the set of cosets $\{a + I \mid a \in R\}$ equipped with the operations:

$$\boxed{(a + I) + (b + I) = (a + b) + I, \qquad (a + I)(b + I) = (ab) + I.}$$

**These operations are well-defined.** If $a + I = a' + I$ and $b + I = b' + I$, then $a - a' \in I$ and $b - b' \in I$. We must check that $(a+b)+I = (a'+b')+I$ and $ab + I = a'b' + I$:

- *Addition:* $(a+b) - (a'+b') = (a-a') + (b-b') \in I$ since $I$ is closed under addition. $\checkmark$
- *Multiplication:* $ab - a'b' = ab - a'b + a'b - a'b' = (a-a')b + a'(b-b')$. Since $I$ is a two-sided ideal, $(a-a')b \in I$ (right absorption) and $a'(b-b') \in I$ (left absorption), so their sum is in $I$. $\checkmark$

> **Why two-sided?** The well-definedness of multiplication uses both left and right absorption. This is exactly why we need $I$ to be a two-sided ideal — a one-sided ideal does not suffice.

**Proposition.** $(R/I, +, \cdot)$ is a ring. The zero element is $0 + I = I$, and the additive inverse of $a + I$ is $(-a) + I$.

### The Projection Map

The map $\pi : R \to R/I$ defined by $\pi(a) = a + I$ is a surjective ring homomorphism, called the **natural projection** (自然同态). Its kernel is:
$$\ker \pi = \{ a \in R \mid a + I = I \} = I.$$

This confirms the earlier claim: every two-sided ideal is the kernel of some homomorphism.

### Examples

**Example 18.** $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$.

The cosets of $n\mathbb{Z}$ in $\mathbb{Z}$ are $\{0 + n\mathbb{Z},\ 1 + n\mathbb{Z},\ \ldots,\ (n-1) + n\mathbb{Z}\}$, and the ring operations on cosets are exactly addition and multiplication modulo $n$. This is the integers modulo $n$, familiar from Example 4.

**Example 19.** $\mathbb{R}[x]/\langle x^2 + 1 \rangle \cong \mathbb{C}$.

Here $\mathbb{R}[x]$ is the ring of polynomials with real coefficients and $\langle x^2+1 \rangle$ is the ideal of all multiples of $x^2+1$. Every coset has a unique representative of the form $a + bx$ (with $a, b \in \mathbb{R}$), since we can reduce any polynomial modulo $x^2 + 1$ using the relation $x^2 \equiv -1$. The coset $x + \langle x^2+1 \rangle$ plays the role of $i$, and the ring operations reproduce exactly those of $\mathbb{C}$.

---

## 9. The Fundamental Theorem of Ring Homomorphisms

### Statement

> **Theorem (First Isomorphism Theorem).** Let $\varphi : R \to S$ be a ring homomorphism. Then:
>
> $$R / \ker\varphi \cong \operatorname{Im}\varphi$$
>
> where $\operatorname{Im}\varphi = \varphi(R) = \{\varphi(r) \mid r \in R\}$ is the image of $\varphi$.

More explicitly, the map $\bar{\varphi} : R/\ker\varphi \to \operatorname{Im}\varphi$ defined by

$$\bar{\varphi}(a + \ker\varphi) = \varphi(a)$$

is a well-defined ring isomorphism.

### Proof

Let $K = \ker\varphi$. We verify that $\bar\varphi$ is a well-defined ring isomorphism.

**Well-defined.** If $a + K = b + K$, then $a - b \in K$, so $\varphi(a-b) = 0$, giving $\varphi(a) = \varphi(b)$. Hence $\bar\varphi$ does not depend on the choice of coset representative. $\checkmark$

**Homomorphism.**
$$\bar\varphi((a+K)+(b+K)) = \bar\varphi((a+b)+K) = \varphi(a+b) = \varphi(a)+\varphi(b) = \bar\varphi(a+K)+\bar\varphi(b+K).$$
The case for multiplication is analogous. $\checkmark$

**Injective.** If $\bar\varphi(a+K) = 0$, then $\varphi(a) = 0$, so $a \in K$, meaning $a + K = K = 0_{R/K}$. Hence $\ker\bar\varphi = \{0_{R/K}\}$, so $\bar\varphi$ is injective (Section 5, Property 3). $\checkmark$

**Surjective.** Every element of $\operatorname{Im}\varphi$ is of the form $\varphi(a) = \bar\varphi(a+K)$ for some $a \in R$. $\checkmark$

Thus $\bar\varphi$ is a bijective ring homomorphism, i.e., an isomorphism. $\square$

### Diagram

The theorem says every homomorphism $\varphi$ factors through the quotient:

$$\begin{array}{ccc} R & \xrightarrow{\ \varphi\ } & S \\ {\scriptstyle \pi}\downarrow & \nearrow_{\bar\varphi} & \\ R/K & & \end{array}$$

where $\pi$ is the natural projection ($\pi(a) = a + K$) and $\varphi = \bar\varphi \circ \pi$. The map $\bar\varphi$ is the unique injective homomorphism making this diagram commute.

### Examples

**Example 20.** Apply the theorem to $\varphi : \mathbb{Z} \to \mathbb{Z}_n$ (reduction mod $n$).

- $\ker\varphi = n\mathbb{Z}$.
- $\operatorname{Im}\varphi = \mathbb{Z}_n$ (surjective).
- The theorem gives $\mathbb{Z}/n\mathbb{Z} \cong \mathbb{Z}_n$, confirming Example 18.

**Example 21.** Apply the theorem to $\varphi : \mathbb{Z}[x] \to \mathbb{Z}$, $f \mapsto f(0)$ (evaluation at 0, Example 12).

- $\ker\varphi = x\mathbb{Z}[x]$ (polynomials with zero constant term).
- $\operatorname{Im}\varphi = \mathbb{Z}$ (surjective).
- The theorem gives $\mathbb{Z}[x]/x\mathbb{Z}[x] \cong \mathbb{Z}$.

  This has a concrete interpretation: in the quotient ring, $x$ is set to $0$, so every polynomial collapses to its constant term, and what remains is a copy of $\mathbb{Z}$.

---

## 10. Integral Domains

### Motivation

In $\mathbb{Z}$, if $ab = 0$ then $a = 0$ or $b = 0$. This familiar cancellation property fails in some rings: in $\mathbb{Z}_6$, for instance, $2 \cdot 3 = 0$ even though neither $2$ nor $3$ is zero. Elements like $2$ and $3$ in $\mathbb{Z}_6$ are called **zero divisors**, and rings without them behave much more like the integers.

### Definition

Let $R$ be a commutative ring with unity ($1 \neq 0$). A non-zero element $a \in R$ is called a **zero divisor** (零因子) if there exists a non-zero $b \in R$ such that $ab = 0$.

An **integral domain** (整环) is a commutative ring with unity ($1 \neq 0$) that has no zero divisors. Equivalently, $R$ is an integral domain if:
$$ab = 0 \implies a = 0 \text{ or } b = 0, \quad \text{for all } a, b \in R.$$

> **Cancellation law.** $R$ is an integral domain if and only if the cancellation law holds: for all $a, b, c \in R$ with $a \neq 0$,
> $$ab = ac \implies b = c.$$
> *Proof.* $ab = ac \iff a(b-c) = 0$. Since $a \neq 0$ and $R$ has no zero divisors, $b - c = 0$, i.e., $b = c$. $\square$

### Examples

**Example 22.** $\mathbb{Z}$ is an integral domain.

If $ab = 0$ in $\mathbb{Z}$, then $a = 0$ or $b = 0$ by the usual properties of integers. $\checkmark$

**Example 23.** $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ are integral domains (in fact, they are fields — see Section 2).

**Example 24.** $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$, the Gaussian integers, is an integral domain.

*Proof.* Suppose $(a+bi)(c+di) = 0$. Taking modulus: $|a+bi|^2 |c+di|^2 = (a^2+b^2)(c^2+d^2) = 0$. Since $a^2+b^2 \geq 0$ and $c^2+d^2 \geq 0$, one of them must be zero, forcing $a+bi = 0$ or $c+di = 0$. $\square$

**Example 25.** $\mathbb{Z}[x]$, polynomials with integer coefficients, is an integral domain.

If $f, g \in \mathbb{Z}[x]$ are both non-zero, then the leading coefficient of $fg$ is the product of the leading coefficients of $f$ and $g$, which is non-zero in $\mathbb{Z}$. Hence $fg \neq 0$.

**Non-example.** $\mathbb{Z}_6$ is **not** an integral domain: $2 \cdot 3 = 6 \equiv 0$ but $2 \neq 0$ and $3 \neq 0$.

**Non-example.** $\mathbb{Z}_n$ is an integral domain if and only if $n$ is prime. When $n$ is composite, say $n = ab$ with $1 < a, b < n$, then $a \cdot b \equiv 0 \pmod{n}$ with both $a, b \neq 0$.

### Finite Integral Domains are Fields

**Theorem.** Every finite integral domain is a field.

*Proof.* Let $R$ be a finite integral domain and $a \in R$ non-zero. Consider the map $\mu_a : R \to R$ defined by $\mu_a(r) = ar$. Since $R$ has no zero divisors, $\mu_a$ is injective (if $ar = as$ then $r = s$ by cancellation). An injective map from a finite set to itself is surjective, so $\mu_a$ is bijective. In particular, $1 \in \operatorname{Im}(\mu_a)$, meaning there exists $b \in R$ with $ab = 1$. Hence every non-zero element is invertible, so $R$ is a field. $\square$

**Corollary.** $\mathbb{Z}_p$ is a field for every prime $p$.

---

## 11. Operations on Ideals

Let $R$ be a ring and $I, J \trianglelefteq R$ two-sided ideals. We can combine them in several natural ways, each producing a new ideal.

### 11.1 Sum

The **sum** of $I$ and $J$ is:
$$I + J = \{ a + b \mid a \in I,\ b \in J \}.$$

**Proposition.** $I + J$ is a two-sided ideal of $R$, and it is the smallest ideal containing both $I$ and $J$.

*Proof.* For closure under subtraction: $(a+b) - (a'+b') = (a-a') + (b-b') \in I+J$. For absorption: $r(a+b) = ra + rb \in I+J$ since $ra \in I$ and $rb \in J$. Hence $I+J \trianglelefteq R$.

If $K \trianglelefteq R$ contains $I$ and $J$, then for any $a \in I \subseteq K$ and $b \in J \subseteq K$, we have $a+b \in K$. So $I+J \subseteq K$. $\square$

**Example 26.** In $\mathbb{Z}$, every ideal is of the form $n\mathbb{Z}$. Then:
$$m\mathbb{Z} + n\mathbb{Z} = \gcd(m,n)\mathbb{Z}.$$
For instance, $6\mathbb{Z} + 10\mathbb{Z} = 2\mathbb{Z}$, since $\gcd(6,10) = 2$. Any element of $m\mathbb{Z} + n\mathbb{Z}$ is an integer linear combination of $m$ and $n$, and by Bézout's identity, the set of all such combinations is exactly $\gcd(m,n)\mathbb{Z}$.

### 11.2 Intersection

The **intersection** $I \cap J$ is the usual set intersection.

**Proposition.** $I \cap J$ is a two-sided ideal of $R$, and it is the largest ideal contained in both $I$ and $J$.

*Proof.* If $a, b \in I \cap J$, then $a - b \in I$ and $a - b \in J$, so $a - b \in I \cap J$. Absorption: for $r \in R$, $ra \in I$ and $ra \in J$, so $ra \in I \cap J$. $\square$

**Example 27.** In $\mathbb{Z}$:
$$m\mathbb{Z} \cap n\mathbb{Z} = \operatorname{lcm}(m,n)\mathbb{Z}.$$
For instance, $6\mathbb{Z} \cap 10\mathbb{Z} = 30\mathbb{Z}$, since $\operatorname{lcm}(6,10) = 30$. An integer belongs to both $6\mathbb{Z}$ and $10\mathbb{Z}$ if and only if it is divisible by both $6$ and $10$, i.e., by $\text{lcm}(6,10)$.

### 11.3 Product

The **product** of $I$ and $J$ is the ideal generated by all pairwise products:
$$IJ = \left\{ \sum_{k=1}^n a_k b_k \;\middle|\; n \geq 1,\ a_k \in I,\ b_k \in J \right\}.$$

That is, $IJ$ consists of all **finite sums** of products $ab$ with $a \in I$, $b \in J$. (A single product $ab$ need not be in an ideal; we need sums to ensure closure under addition.)

**Proposition.** $IJ$ is a two-sided ideal of $R$, and $IJ \subseteq I \cap J$.

*Proof.* Ideal: sums of elements in $IJ$ stay in $IJ$; for absorption, $r(\sum a_k b_k) = \sum (ra_k)b_k \in IJ$ since $ra_k \in I$. Inclusion: each $a_k b_k \in I$ (since $I$ absorbs $b_k$ from the right) and $a_k b_k \in J$ (since $J$ absorbs $a_k$ from the left), so every generator lies in $I \cap J$, hence $IJ \subseteq I \cap J$. $\square$

**Example 28.** In $\mathbb{Z}$:
$$m\mathbb{Z} \cdot n\mathbb{Z} = mn\mathbb{Z}.$$
Each generator is of the form $(mk)(nl) = mn(kl)$, a multiple of $mn$. Note $mn\mathbb{Z} \subseteq \operatorname{lcm}(m,n)\mathbb{Z}$, consistent with $IJ \subseteq I \cap J$. When $\gcd(m,n) = 1$, we have $\operatorname{lcm}(m,n) = mn$, so $IJ = I \cap J$.

### 11.4 Summary of Containments

$$IJ \subseteq I \cap J \subseteq I,\ J \subseteq I + J.$$

In $\mathbb{Z}$ with $I = 6\mathbb{Z}$, $J = 10\mathbb{Z}$:
$$60\mathbb{Z} \subseteq 30\mathbb{Z} \subseteq 6\mathbb{Z},\ 10\mathbb{Z} \subseteq 2\mathbb{Z}.$$

> **Coprime ideals.** $I$ and $J$ are called **coprime** (互素) if $I + J = R$. In this case $I \cap J = IJ$ — the intersection collapses to the product. This is the ideal-theoretic generalization of the Chinese Remainder Theorem.

---

## 12. Direct Sum of Rings

### Definition

Let $R_1, R_2, \ldots, R_n$ be rings. Their **direct sum** (直和, also called **direct product**) is the Cartesian product:

$$R_1 \oplus R_2 \oplus \cdots \oplus R_n = \{ (a_1, a_2, \ldots, a_n) \mid a_i \in R_i \}$$

equipped with **componentwise** operations:
$$(a_1, \ldots, a_n) + (b_1, \ldots, b_n) = (a_1+b_1, \ldots, a_n+b_n),$$
$$(a_1, \ldots, a_n) \cdot (b_1, \ldots, b_n) = (a_1 b_1, \ldots, a_n b_n).$$

**Proposition.** $R_1 \oplus \cdots \oplus R_n$ is a ring. Its zero is $(0_{R_1}, \ldots, 0_{R_n})$, and if each $R_i$ has unity $1_i$, then $(1_{R_1}, \ldots, 1_{R_n})$ is the unity of the direct sum.

### Examples

**Example 29.** $\mathbb{Z}_2 \oplus \mathbb{Z}_3$.

Elements are pairs $(a, b)$ with $a \in \mathbb{Z}_2$, $b \in \mathbb{Z}_3$, giving $2 \times 3 = 6$ elements. Addition and multiplication are done in each component independently. By the Chinese Remainder Theorem, $\mathbb{Z}_2 \oplus \mathbb{Z}_3 \cong \mathbb{Z}_6$.

**Example 30.** $\mathbb{R} \oplus \mathbb{R}$.

This is a commutative ring with unity $(1, 1)$. It is **not** an integral domain: $(1, 0) \cdot (0, 1) = (0, 0)$, so $(1,0)$ and $(0,1)$ are zero divisors. Compare this with $\mathbb{R}$ itself, which is a field.

### Projection Maps

For each $i$, the **projection** $\pi_i : R_1 \oplus \cdots \oplus R_n \to R_i$ defined by $\pi_i(a_1, \ldots, a_n) = a_i$ is a surjective ring homomorphism with kernel:
$$\ker \pi_i = \{ (a_1, \ldots, a_n) \mid a_i = 0 \} \cong R_1 \oplus \cdots \oplus \widehat{R_i} \oplus \cdots \oplus R_n,$$
where $\widehat{R_i}$ denotes that $R_i$ is omitted.

### Chinese Remainder Theorem for Rings

> **Theorem (CRT).** Let $R$ be a commutative ring with unity and $I_1, \ldots, I_n \trianglelefteq R$ pairwise coprime ideals (i.e., $I_j + I_k = R$ for all $j \neq k$). Then the map
> $$\varphi : R \to R/I_1 \oplus R/I_2 \oplus \cdots \oplus R/I_n, \qquad \varphi(a) = (a + I_1,\ a + I_2,\ \ldots,\ a + I_n)$$
> is a surjective ring homomorphism with $\ker\varphi = I_1 \cap I_2 \cap \cdots \cap I_n = I_1 I_2 \cdots I_n$. In particular:
> $$R \,/\, (I_1 \cap \cdots \cap I_n) \;\cong\; R/I_1 \oplus \cdots \oplus R/I_n.$$

### Proof

The proof has four steps: (1) $\varphi$ is a homomorphism, (2) compute $\ker\varphi$, (3) show $I_1 \cap \cdots \cap I_n = I_1 \cdots I_n$, (4) show $\varphi$ is surjective. The isomorphism then follows from the Fundamental Theorem (Section 9).

---

**Step 1: $\varphi$ is a ring homomorphism.**

For all $a, b \in R$:
$$\varphi(a+b) = (a+b+I_1, \ldots, a+b+I_n) = (a+I_1,\ldots,a+I_n) + (b+I_1,\ldots,b+I_n) = \varphi(a)+\varphi(b).$$
$$\varphi(ab) = (ab+I_1, \ldots, ab+I_n) = (a+I_1,\ldots,a+I_n)\cdot(b+I_1,\ldots,b+I_n) = \varphi(a)\cdot\varphi(b).$$
Both follow directly from the componentwise operations on the direct sum. $\checkmark$

---

**Step 2: $\ker\varphi = I_1 \cap \cdots \cap I_n$.**

$$a \in \ker\varphi \iff \varphi(a) = (I_1, \ldots, I_n) \iff a + I_k = I_k \text{ for all } k \iff a \in I_k \text{ for all } k \iff a \in I_1 \cap \cdots \cap I_n. \quad \checkmark$$

---

**Step 3: $I_1 \cap \cdots \cap I_n = I_1 \cdots I_n$ (under pairwise coprimeness).**

We always have $I_1 \cdots I_n \subseteq I_1 \cap \cdots \cap I_n$ (Section 11). We prove the reverse inclusion by induction on $n$.

*Base case $n = 2$.* Suppose $I_1 + I_2 = R$. Pick $u \in I_1$, $v \in I_2$ with $u + v = 1$. For any $x \in I_1 \cap I_2$:
$$x = x \cdot 1 = x(u + v) = \underbrace{xu}_{\in I_2 \cdot I_1 = I_1 I_2} + \underbrace{xv}_{\in I_1 \cdot I_2 = I_1 I_2}.$$
Hence $x \in I_1 I_2$, giving $I_1 \cap I_2 \subseteq I_1 I_2$. $\square$

*Inductive step.* Assume the result holds for $n-1$ ideals. Let $J = I_2 \cdots I_{n} = I_2 \cap \cdots \cap I_n$ (by the induction hypothesis applied to $I_2, \ldots, I_n$).

We claim $I_1 + J = R$. For each $k \geq 2$, since $I_1 + I_k = R$, pick $u_k \in I_1$, $v_k \in I_k$ with $u_k + v_k = 1$. Then:
$$1 = \prod_{k=2}^{n}(u_k + v_k).$$
Expanding this product, every term contains at least one factor $v_k \in I_k$ unless the term is $\prod_k u_k$. More precisely:
$$1 = \underbrace{\prod_{k=2}^n u_k}_{\in I_1} + \underbrace{\text{(remaining terms, each containing some } v_k \in I_k \subseteq J\text{)}}_{\in J}.$$
Hence $1 \in I_1 + J$, so $I_1 + J = R$.

Applying the base case to $I_1$ and $J$:
$$I_1 \cap \cdots \cap I_n = I_1 \cap J = I_1 J = I_1 (I_2 \cap \cdots \cap I_n) = I_1 I_2 \cdots I_n. \quad \square$$

---

**Step 4: $\varphi$ is surjective.**

*Key construction.* For each index $i$, define $J_i = \prod_{j \neq i} I_j$. By the same argument as in Step 3, $I_i + J_i = R$ (since $I_i$ is coprime to each $I_j$ with $j \neq i$, so it is coprime to their product). Pick $u_i \in I_i$ and $e_i \in J_i$ such that:
$$u_i + e_i = 1, \quad \text{so} \quad e_i \equiv 1 \pmod{I_i}.$$

Note the crucial property of $e_i$: since $J_i = \prod_{j\neq i} I_j \subseteq I_k$ for every $k \neq i$, we have:
$$e_i \equiv 0 \pmod{I_k} \quad \text{for all } k \neq i.$$

So the elements $e_1, \ldots, e_n$ act as "selectors": $e_i$ is $1$ modulo $I_i$ and $0$ modulo all other $I_k$.

*Constructing the preimage.* Given any target $(r_1 + I_1, \ldots, r_n + I_n)$, set:
$$a = r_1 e_1 + r_2 e_2 + \cdots + r_n e_n.$$

For each fixed $k$, reduce $a$ modulo $I_k$:
$$a = r_k e_k + \sum_{i \neq k} r_i e_i \equiv r_k \cdot 1 + \sum_{i \neq k} r_i \cdot 0 = r_k \pmod{I_k}.$$

Hence $\varphi(a) = (r_1 + I_1, \ldots, r_n + I_n)$, and $\varphi$ is surjective. $\checkmark$

---

**Conclusion.** By the Fundamental Theorem of Ring Homomorphisms (Section 9):
$$R \,/\, \ker\varphi \;\cong\; \operatorname{Im}\varphi = R/I_1 \oplus \cdots \oplus R/I_n,$$
and from Steps 2–3, $\ker\varphi = I_1 \cap \cdots \cap I_n = I_1 \cdots I_n$. $\square$

### Connection to the Classical Number-Theoretic CRT

The ring proof and the classical integer CRT are the same argument in different languages. The correspondence is exact:

| Number-theoretic language | Ring-theoretic language |
|---|---|
| Modulus $m_k$ | Ideal $I_k$ |
| $\mathbb{Z}/m_k\mathbb{Z}$ | Quotient ring $R/I_k$ |
| $\gcd(m_j, m_k) = 1$ | $I_j + I_k = R$ |
| $M_i = \prod_{j \neq i} m_j$ | $J_i = \prod_{j \neq i} I_j$ |
| Bézout: $u_i m_i + y_i M_i = 1$ | Coprimeness: $u_i + e_i = 1$, $u_i \in I_i$, $e_i \in J_i$ |
| $e_i = y_i M_i \equiv 1 \pmod{m_i}$, $\equiv 0 \pmod{m_j}$ for $j \neq i$ | $e_i \equiv 1 \pmod{I_i}$, $\equiv 0 \pmod{I_k}$ for $k \neq i$ |
| Solution $x = \sum r_i e_i$ | Preimage $a = \sum r_i e_i$ |

The "selector" construction in Step 4 — build $e_i$ that is $1$ on the $i$-th component and $0$ on all others, then take $a = \sum r_i e_i$ — is verbatim the classical proof. The only difference is that $\gcd = 1$ (proved by the Euclidean algorithm) is replaced by $I + J = R$ (an algebraic condition that requires no computation). This abstraction makes the same theorem true over $\mathbb{Z}[i]$, $k[x]$, and any commutative ring, without changing a single step of the proof.

### The Isomorphism as a Solution Machine

The isomorphism conclusion corresponds directly to solving congruence equations. Taking $n = 2$ for clarity, CRT gives a bijection:

$$\bar\varphi : \mathbb{Z}/mn\mathbb{Z} \xrightarrow{\ \sim\ } \mathbb{Z}/m\mathbb{Z} \oplus \mathbb{Z}/n\mathbb{Z}, \qquad x \bmod mn \;\mapsto\; (x \bmod m,\ x \bmod n).$$

The left side has $mn$ residues; the right side has $mn$ pairs $(r_1, r_2)$. The isomorphism says these two sets are in perfect one-to-one correspondence.

The system of congruences $x \equiv r_1 \pmod{m}$, $x \equiv r_2 \pmod{n}$ is asking: what is the unique preimage $\bar\varphi^{-1}(r_1, r_2)$ in $\mathbb{Z}/mn\mathbb{Z}$?

| Congruence language | Isomorphism language |
|---|---|
| System $x \equiv r_k \pmod{m_k}$ | Find $\bar\varphi^{-1}(r_1, \ldots, r_n)$ |
| A solution exists | $\bar\varphi$ is surjective |
| Solution is unique mod $m_1 \cdots m_n$ | $\bar\varphi$ is injective |
| Explicit formula $x = \sum r_i e_i$ | Explicit construction of $\bar\varphi^{-1}$ |

The isomorphism — being simultaneously surjective and injective — packages both **existence** and **uniqueness** of the solution into a single algebraic statement. Finding the solution is exactly traversing $\bar\varphi$ in reverse.

**Example 31.** In $\mathbb{Z}$, take $I_1 = m\mathbb{Z}$ and $I_2 = n\mathbb{Z}$ with $\gcd(m,n)=1$. Then $I_1 + I_2 = \mathbb{Z}$ (coprime), $I_1 \cap I_2 = mn\mathbb{Z}$, and CRT gives:
$$\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \oplus \mathbb{Z}/n\mathbb{Z}, \quad \text{i.e., } \mathbb{Z}_{mn} \cong \mathbb{Z}_m \oplus \mathbb{Z}_n.$$
This is the classical Chinese Remainder Theorem: a system of congruences modulo pairwise coprime moduli has a unique solution modulo their product.
