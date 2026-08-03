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

---

## 13. Prime Ideals and Maximal Ideals

Throughout this section, $R$ denotes a **commutative ring with unity**. Both notions below are defined via the quotient ring $R/I$: a prime ideal is one whose quotient is an integral domain, a maximal ideal is one whose quotient is a field.

### 13.1 Prime Ideals

#### Definition

A proper ideal $P \trianglelefteq R$ (i.e., $P \neq R$) is called a **prime ideal** (素理想) if:
$$ab \in P \implies a \in P \text{ or } b \in P, \quad \text{for all } a, b \in R.$$

> **Why "prime"?** This mimics the defining property of a prime number $p$: $p \mid ab \implies p \mid a$ or $p \mid b$. Indeed, the ideals $p\mathbb{Z} \trianglelefteq \mathbb{Z}$ are exactly the prime ideals of $\mathbb{Z}$ (Example 32 below).

#### Theorem (Prime Ideal Criterion)

> **Theorem.** Let $R$ be a commutative ring with unity and $P$ a proper ideal of $R$. Then $P$ is prime if and only if $R/P$ is an integral domain.

**Proof.**

$(\Rightarrow)$ Suppose $P$ is prime. Since $P \neq R$, $R/P$ is a non-zero ring, and since $R$ has unity, so does $R/P$ (with unity $1 + P$, and $1 + P \neq 0 + P$ because $1 \notin P$). Suppose $(a+P)(b+P) = 0 + P$ in $R/P$, i.e., $ab + P = P$, i.e., $ab \in P$. Since $P$ is prime, $a \in P$ or $b \in P$, i.e., $a + P = 0+P$ or $b+P = 0+P$. Hence $R/P$ has no zero divisors, so it is an integral domain.

$(\Leftarrow)$ Suppose $R/P$ is an integral domain. Then $R/P$ is non-zero, so $P \neq R$. Suppose $ab \in P$. Then $(a+P)(b+P) = ab + P = 0 + P$ in $R/P$. Since $R/P$ has no zero divisors, $a + P = 0+P$ or $b+P = 0+P$, i.e., $a \in P$ or $b \in P$. Hence $P$ is prime. $\square$

#### Examples

**Example 32.** The prime ideals of $\mathbb{Z}$ are exactly $\{0\}$ and $p\mathbb{Z}$ for $p$ prime.

*Proof sketch.* By the theorem, $n\mathbb{Z}$ is prime iff $\mathbb{Z}/n\mathbb{Z} = \mathbb{Z}_n$ is an integral domain. By Example 22–25 and the non-example following Example 25, $\mathbb{Z}_n$ is an integral domain iff $n = 0$ or $n$ is prime. $\checkmark$

Note $2\mathbb{Z}$ is prime but not maximal is false here — we will see in Example 34 that $p\mathbb{Z}$ ($p$ prime) is in fact maximal, while $\{0\}$ is prime but **not** maximal (since $\{0\} \subsetneq 2\mathbb{Z} \subsetneq \mathbb{Z}$).

**Example 33.** $\langle x \rangle = x\mathbb{Z}[x] \trianglelefteq \mathbb{Z}[x]$ is prime, since $\mathbb{Z}[x]/\langle x\rangle \cong \mathbb{Z}$ (Example 21) is an integral domain.

**Non-example.** $\langle 4 \rangle = 4\mathbb{Z} \trianglelefteq \mathbb{Z}$ is not prime: $2 \cdot 2 = 4 \in 4\mathbb{Z}$, but $2 \notin 4\mathbb{Z}$.

### 13.2 Maximal Ideals

#### Definition

A proper ideal $M \trianglelefteq R$ is called a **maximal ideal** (极大理想) if there is no ideal $J$ with $M \subsetneq J \subsetneq R$. Equivalently, the only ideals containing $M$ are $M$ itself and $R$.

#### Theorem (Maximal Ideal Criterion)

> **Theorem.** Let $R$ be a commutative ring with unity and $M$ a proper ideal of $R$. Then $M$ is maximal if and only if $R/M$ is a field.

**Proof.**

$(\Rightarrow)$ Suppose $M$ is maximal. Since $R$ is commutative with unity, so is $R/M$, and it is non-zero since $M \neq R$. Let $a + M \neq 0 + M$ be a non-zero element of $R/M$, i.e., $a \notin M$. Consider the ideal $M + \langle a \rangle$ (the smallest ideal containing $M$ and $a$, using the ideal sum from Section 11). Since $a \notin M$, we have $M \subsetneq M + \langle a \rangle$. By maximality of $M$, this forces $M + \langle a \rangle = R$. In particular $1 \in M + \langle a \rangle$, so
$$1 = m + ra \quad \text{for some } m \in M,\ r \in R.$$
Reducing modulo $M$: $1 + M = ra + M = (r+M)(a+M)$. Hence $a + M$ is invertible in $R/M$, with inverse $r + M$. Since every non-zero element of $R/M$ is invertible, $R/M$ is a field.

$(\Leftarrow)$ Suppose $R/M$ is a field. Then $R/M$ is non-zero, so $M \neq R$. Let $J$ be an ideal with $M \subsetneq J \subseteq R$; we show $J = R$. Pick $a \in J \setminus M$. Then $a + M \neq 0+M$ in $R/M$, so since $R/M$ is a field, there exists $b \in R$ with $(a+M)(b+M) = 1+M$, i.e., $ab - 1 \in M \subseteq J$. Since $a \in J$ and $J$ is an ideal, $ab \in J$; combined with $ab - 1 \in J$, we get $1 = ab - (ab-1) \in J$. Then for any $r \in R$, $r = r\cdot 1 \in J$, so $J = R$. Hence $M$ is maximal. $\square$

#### Corollary: Every Maximal Ideal is Prime

> **Corollary.** In a commutative ring with unity, every maximal ideal is a prime ideal.

**Proof.** If $M$ is maximal, $R/M$ is a field (by the theorem above), hence an integral domain (fields have no zero divisors — Section 2 and the table in Section 2). By the Prime Ideal Criterion, $M$ is prime. $\square$

The converse is **false** in general: $\{0\} \trianglelefteq \mathbb{Z}$ is prime (since $\mathbb{Z}$ is an integral domain) but not maximal (since $\{0\} \subsetneq 2\mathbb{Z} \subsetneq \mathbb{Z}$). This gives the refined hierarchy of ideals:
$$\text{maximal} \implies \text{prime} \implies \text{proper},$$
mirroring the hierarchy of quotients:
$$\text{field} \implies \text{integral domain} \implies \text{non-zero ring}.$$

#### Examples

**Example 34.** For a prime $p$, $p\mathbb{Z} \trianglelefteq \mathbb{Z}$ is maximal, since $\mathbb{Z}/p\mathbb{Z} \cong \mathbb{Z}_p$ is a field (Corollary in Section 10). Conversely, every non-zero prime ideal of $\mathbb{Z}$ is of this form (Example 32), so **in $\mathbb{Z}$, every non-zero prime ideal is maximal.**

> **Remark.** This "prime = maximal" collapse (away from $\{0\}$) is special to rings like $\mathbb{Z}$ where every non-zero prime ideal is maximal — such rings, together with a few extra conditions, are called **principal ideal domains**, and this phenomenon (Krull dimension $1$) does not persist in higher-dimensional rings such as $\mathbb{Z}[x]$ or $k[x,y]$.

**Example 35.** $\langle x \rangle \trianglelefteq \mathbb{Z}[x]$ is prime but **not** maximal: $\mathbb{Z}[x]/\langle x\rangle \cong \mathbb{Z}$ (Example 21, 33) is an integral domain but not a field. Indeed, $\langle x\rangle \subsetneq \langle x, 2\rangle \subsetneq \mathbb{Z}[x]$, so $\langle x \rangle$ is not maximal. One checks $\langle x, 2\rangle$ *is* maximal, since $\mathbb{Z}[x]/\langle x,2\rangle \cong \mathbb{Z}_2$, a field.

**Example 36.** In $\mathbb{R}[x]$, the ideal $\langle x^2+1\rangle$ is maximal, since $\mathbb{R}[x]/\langle x^2+1\rangle \cong \mathbb{C}$ (Example 19) is a field.

**Example 37.** In $S = \mathbb{Z}_6$, the ideal $\{0,2,4\}$ (Example 8) is maximal: $\mathbb{Z}_6 / \{0,2,4\} \cong \mathbb{Z}_2$ (the map $\mathbb{Z}_6 \to \mathbb{Z}_2$, $n \mapsto n \bmod 2$, has this kernel), a field. Similarly $\{0,3\}$ is maximal with quotient $\mathbb{Z}_3$. Both correspond to the CRT decomposition $\mathbb{Z}_6 \cong \mathbb{Z}_2 \oplus \mathbb{Z}_3$ (Example 29).

### 13.3 Existence of Maximal Ideals

> **Theorem.** Every proper ideal $I$ of a ring $R$ with unity is contained in some maximal ideal.

*Idea of proof.* Consider the set $\Sigma$ of proper ideals containing $I$, partially ordered by inclusion. It is non-empty ($I \in \Sigma$), and every chain in $\Sigma$ has an upper bound (the union of the chain — one checks this union is still a proper ideal, since it cannot contain $1$). By **Zorn's Lemma**, $\Sigma$ has a maximal element, which is a maximal ideal of $R$ containing $I$. $\square$

In particular, taking $I = \{0\}$: **every non-zero ring with unity has a maximal ideal.**

### 13.4 Summary

| Ideal type | Condition on quotient | Implication |
|---|---|---|
| Proper ideal | $R/I \neq \{0\}$ | — |
| Prime ideal | $R/P$ is an integral domain | Maximal $\implies$ Prime |
| Maximal ideal | $R/M$ is a field | (converse false in general) |

This dictionary — turning ring-theoretic properties of $R/I$ into ideal-theoretic properties of $I$ — is the same technique used throughout Sections 8–10, and is the key bridge connecting ideal theory to the classification of rings by their quotients.

---

## 14. Constructing Extension Fields and Finite Fields

### 14.1 Motivation

We know $\mathbb{Z}_p$ is a field for every prime $p$ (Section 10), and more generally $R/M$ is a field exactly when $M$ is maximal (Section 13.2). Are there finite fields other than $\mathbb{Z}_p$? Yes — for every prime $p$ and every $n \geq 1$ there is a field with exactly $p^n$ elements. The construction runs entirely through the maximal-ideal machinery just developed, applied to the polynomial ring $k[x]$.

### 14.2 $k[x]$ is a Principal Ideal Domain

#### Definition

Let $R$ be a ring. An ideal $I \trianglelefteq R$ is called a **principal ideal** (主理想) if it is generated by a single element $a \in R$:
$$I = \langle a \rangle = \{ ra \mid r \in R \}.$$
An integral domain $R$ in which **every** ideal is principal is called a **principal ideal domain** (主理想整环, **PID**).

> **Remark.** The point is not that *some* ideals are principal — $\{0\} = \langle 0\rangle$ and $R = \langle 1\rangle$ always are — but that *all of them* are, with no exceptions. This section shows $k[x]$ has this property, alongside the already-familiar case of $\mathbb{Z}$ (Example 13).

#### Division Algorithm

> **Theorem.** Let $k$ be a field and $f, g \in k[x]$ with $g \neq 0$. There exist unique $q, r \in k[x]$ with
> $$f = qg + r, \qquad r = 0 \text{ or } \deg r < \deg g.$$

*Proof sketch.* *Existence*, by induction on $\deg f$: if $\deg f < \deg g$, take $q = 0, r = f$. Otherwise let $a, b$ be the leading coefficients of $f, g$ and $m = \deg f \geq n = \deg g$. Since $k$ is a field, $b^{-1}$ exists, and $f - (ab^{-1}x^{m-n})g$ has degree $< m$; apply the inductive hypothesis to it. *Uniqueness*: if $qg + r = q'g + r'$, then $(q-q')g = r' - r$; the right side has degree $< \deg g$ while the left side has degree $\geq \deg g$ unless $q = q'$, forcing $r = r'$ too. $\square$

> **Remark.** Invertibility of leading coefficients is where "$k$ is a field" is used essentially — the algorithm fails over $\mathbb{Z}$ (e.g. one cannot divide $x$ by $2x$ within $\mathbb{Z}[x]$).

#### Corollary: $k[x]$ is a PID

> **Corollary.** Every ideal of $k[x]$ is principal: $I = \langle f(x)\rangle$ for some $f \in k[x]$.

**Proof.** If $I = \{0\}$, take $f = 0$. Otherwise let $f \in I$ be nonzero of minimal degree. For any $g \in I$, divide $g = qf + r$ with $r = 0$ or $\deg r < \deg f$. Since $g, f \in I$, $r = g - qf \in I$; minimality of $\deg f$ forces $r = 0$, so $g = qf \in \langle f\rangle$. Hence $I = \langle f \rangle$. $\square$

(Compare Example 13: $\mathbb{Z}$ is likewise a PID, and the same division-algorithm argument is exactly how one proves it.)

### 14.3 Irreducible Polynomials Generate Maximal Ideals

#### Definition

Let $k$ be a field. A polynomial $f(x) \in k[x]$ with $\deg f \geq 1$ is **irreducible** (不可约) over $k$ if $f = gh$ with $g, h \in k[x]$ forces $\deg g = 0$ or $\deg h = 0$. Otherwise $f$ is **reducible**.

> Irreducibility is relative to $k$: $x^2+1$ is irreducible over $\mathbb{R}$ but factors as $(x-i)(x+i)$ over $\mathbb{C}$.

#### Theorem

> **Theorem.** Let $k$ be a field and $f \in k[x]$ non-constant. Then $\langle f(x)\rangle$ is a maximal ideal of $k[x]$ if and only if $f$ is irreducible over $k$.

**Proof.**

$(\Leftarrow)$ Since $\deg f \geq 1$, $1 \notin \langle f \rangle$, so $\langle f\rangle \neq k[x]$. Let $J$ be an ideal with $\langle f\rangle \subseteq J \subseteq k[x]$. By the Corollary, $J = \langle g\rangle$ for some $g$, and $f \in \langle g\rangle$ means $g \mid f$, say $f = gh$. Irreducibility of $f$ forces $\deg g = 0$ or $\deg h = 0$.
- If $\deg g = 0$: $g$ is a nonzero constant, hence a unit, so $\langle g \rangle = k[x]$, i.e. $J = k[x]$.
- If $\deg h = 0$: then $g = f h^{-1}$, so $g$ and $f$ differ by a unit and $\langle g \rangle = \langle f \rangle$, i.e. $J = \langle f\rangle$.

Either way $J \in \{\langle f\rangle, k[x]\}$, so $\langle f\rangle$ is maximal.

$(\Rightarrow)$ We prove the contrapositive: if $f$ is **reducible**, then $\langle f\rangle$ is **not** maximal. So suppose $f = gh$ with $\deg g \geq 1$ *and* $\deg h \geq 1$. We exhibit an ideal strictly between $\langle f\rangle$ and $k[x]$, namely $\langle g\rangle$, by checking both inclusions are strict:

$$\langle f\rangle \;\subsetneq\; \langle g\rangle \;\subsetneq\; k[x].$$

*Step 1: $\langle f\rangle \subseteq \langle g\rangle$.* Since $f = gh$, $f$ is a multiple of $g$, so $f \in \langle g\rangle$. An ideal containing $f$ contains every multiple of $f$, hence $\langle f\rangle \subseteq \langle g\rangle$.

*Step 2: the inclusion is strict, $\langle f\rangle \neq \langle g\rangle$ — this is where $\deg h \geq 1$ is used.* Suppose for contradiction $\langle f\rangle = \langle g\rangle$. Then $g \in \langle g\rangle = \langle f\rangle$, so $g$ is a multiple of $f$, i.e. $f \mid g$; hence $\deg f \leq \deg g$. But from $f = gh$ and the degree formula in $k[x]$ (valid since $k$ is a domain),
$$\deg g = \deg f - \deg h \;\leq\; \deg f - 1 \;<\; \deg f,$$
the middle inequality using $\deg h \geq 1$. This contradicts $\deg f \leq \deg g$. So $\langle f\rangle \subsetneq \langle g\rangle$.

*Step 3: $\langle g\rangle \neq k[x]$ — this is where $\deg g \geq 1$ is used.* In $k[x]$ the units are exactly the nonzero constants (degree $0$), and $\langle g\rangle = k[x]$ iff $g$ is a unit. Since $\deg g \geq 1$, $g$ is not a unit, so $\langle g\rangle \neq k[x]$. (This step depends on $g$, not $h$: even if $h$ were constant, a non-constant $g$ alone already makes $\langle g\rangle$ proper.)

Combining the three steps gives $\langle f\rangle \subsetneq \langle g\rangle \subsetneq k[x]$, an ideal properly between $\langle f\rangle$ and the whole ring. Therefore $\langle f\rangle$ is **not** maximal. $\square$

> The two hypotheses do distinct jobs: $\deg h \geq 1$ forces the *left* inclusion strict (Step 2), while $\deg g \geq 1$ forces the *right* inclusion strict (Step 3). Reducibility, supplying both at once, is exactly what the argument needs.

#### Corollary (the field-construction engine)

> **Corollary.** If $k$ is a field and $f(x) \in k[x]$ is irreducible, then $k[x]/\langle f(x)\rangle$ is a field.

**Proof.** Immediate from the theorem above and the Maximal Ideal Criterion (Section 13.2). $\square$

Every construction below is this one corollary applied to a specific $k$ and $f$.

### 14.4 Kronecker's Theorem: Adjoining a Root

> **Theorem (Kronecker).** Let $k$ be a field and $f(x) \in k[x]$ non-constant. There is a field $K \supseteq k$ in which $f$ has a root.

**Proof.** Let $p(x)$ be an irreducible factor of $f(x)$ (take $p = f$ if $f$ is already irreducible), and set $K = k[x]/\langle p(x)\rangle$, a field by the Corollary. The map $\iota : k \to K$, $\iota(a) = a + \langle p(x)\rangle$, is a ring homomorphism; since $k$ is a field (a simple ring, Example 16), $\ker \iota$ is $\{0\}$ or $k$, and it is not $k$ since $\iota(1) = 1 + \langle p(x)\rangle \neq 0$ (as $\deg p \geq 1$). So $\iota$ is injective, embedding $k$ into $K$; identify $k$ with its image. Let $\alpha = x + \langle p(x)\rangle$. Writing $p(x) = c_0 + c_1x + \cdots + c_nx^n$:
$$p(\alpha) = c_0 + c_1\alpha + \cdots + c_n\alpha^n = \big(c_0 + c_1x + \cdots + c_nx^n\big) + \langle p(x)\rangle = p(x) + \langle p(x)\rangle = 0.$$
So $\alpha \in K$ is a root of $p(x)$, hence of $f(x)$. $\square$

This is precisely what produced $\mathbb{C}$ from $\mathbb{R}$ in Example 19: $x^2+1$ is irreducible over $\mathbb{R}$, and $\mathbb{R}[x]/\langle x^2+1\rangle \cong \mathbb{C}$ adjoins the root $\alpha = x + \langle x^2+1\rangle$, playing the role of $i$.

**Example 38 (a degree-4 case, and why the base field matters).** Let $f(x) = x^4+1$. What field does Kronecker's theorem produce? The answer depends entirely on $k$.

*Over $k=\mathbb{Q}$:* $x^4+1$ is irreducible (it is the 8th cyclotomic polynomial $\Phi_8$). Substituting $x=y+1$ gives $y^4+4y^3+6y^2+4y+2$, which is irreducible by Eisenstein at $p=2$ ($2$ divides every non-leading coefficient, $4\nmid2$), so $x^4+1$ is irreducible too. So
$$K = \mathbb{Q}[x]/\langle x^4+1\rangle$$
is a genuine degree-$4$ field extension of $\mathbb{Q}$, with basis $\{1,\alpha,\alpha^2,\alpha^3\}$ where $\alpha^4=-1$. Since $\alpha^8=1$ but $\alpha^4\neq1$, $\alpha$ has multiplicative order exactly $8$ — it is a primitive 8th root of unity $\zeta_8 = \frac{1+i}{\sqrt2}$. One checks $\zeta_8^2=i$ and $\zeta_8+\zeta_8^{-1}=\sqrt2$, so
$$K \cong \mathbb{Q}(\zeta_8) = \mathbb{Q}(i,\sqrt2).$$

*Over $k=\mathbb{R}$:* $x^4+1$ **factors**: $x^4+1=(x^2-\sqrt2x+1)(x^2+\sqrt2x+1)$, so it is not irreducible, and Kronecker's construction must instead use one of these quadratic factors. Either one has no real root, so $\mathbb{R}[x]/\langle x^2-\sqrt2x+1\rangle \cong \mathbb{C}$ — the theorem just reproduces $\mathbb{C}$ again, via a different (but still degree-$2$) irreducible polynomial than $x^2+1$.

*Over $k=\mathbb{F}_2$:* characteristic $2$ gives $x^4+1=(x+1)^4$ (Freshman's dream: $(a+b)^{2^n}=a^{2^n}+b^{2^n}$ in characteristic $2$) — totally reducible, with the only irreducible factor $x+1$ of degree $1$. Kronecker's construction then just returns $\mathbb{F}_2[x]/\langle x+1\rangle \cong \mathbb{F}_2$ itself — no new field at all.

> **Moral.** "The field generated by $f(x)$" is not intrinsic to $f$ alone — it depends on which irreducible factor of $f$, over which base field $k$, is being adjoined. The same polynomial $x^4+1$ yields a degree-$4$ field over $\mathbb{Q}$, reproduces the familiar degree-$2$ field $\mathbb{C}$ over $\mathbb{R}$, and collapses to nothing new at all over $\mathbb{F}_2$.

### 14.5 Finite Fields

#### Characteristic

The **characteristic** $\operatorname{char}(R)$ of a ring with unity $R$ is the least $n > 0$ with $\underbrace{1 + \cdots + 1}_{n} = 0$, or $0$ if no such $n$ exists.

> **Proposition.** The characteristic of an integral domain is $0$ or a prime $p$.

*Proof.* If $\operatorname{char}(R) = n = ab$ with $1 < a,b < n$, then, writing $\overline{m}$ for $\underbrace{1+\cdots+1}_m$, distributivity gives $\overline{a}\cdot\overline{b} = \overline{n} = 0$. No zero divisors force $\overline a = 0$ or $\overline b = 0$, contradicting minimality of $n$. $\square$

A finite field $F$ cannot have characteristic $0$ (the elements $1, \overline 2, \overline 3, \ldots$ would then be infinitely many distinct elements of $F$), so $\operatorname{char}(F) = p$ for some prime $p$. The set $\{0, 1, \overline 2, \ldots, \overline{p-1}\}$ then forms a subring isomorphic to $\mathbb{Z}_p$, called the **prime subfield** of $F$.

#### Every Finite Field has Order $p^n$

> **Theorem.** A finite field $F$ has $|F| = p^n$ elements, where $p = \operatorname{char}(F)$ and $n = \dim_k F$ for $k \cong \mathbb{Z}_p$ the prime subfield.

*Proof.* View $F$ as a vector space over its prime subfield $k$ (vector addition = ring addition, scalar multiplication = ring multiplication restricted to $k \times F$; the field axioms of $F$ give exactly the vector space axioms). Since $F$ is finite, $\dim_k F = n$ is finite; fix a basis $e_1, \ldots, e_n$. Every element of $F$ is uniquely $c_1e_1 + \cdots + c_ne_n$ with $c_i \in k$, and $|k| = p$, so there are exactly $p^n$ such combinations. $\square$

#### Why the Field Axioms Give Exactly the Vector Space Axioms

The proof above leaned on a one-line claim worth verifying once in full. The general statement: **if $E \supseteq F$ are fields (with $F$ a subfield of $E$), then $E$ is a vector space over $F$** — with no extra work. The proposed cast:

| Vector space ingredient | What we use |
|---|---|
| Set of vectors $V$ | the set $E$ |
| Scalars | elements of $F$ |
| Vector addition $u + v$ | the field addition of $E$ |
| Scalar multiplication $a \cdot u$ ($a \in F$, $u \in E$) | the field multiplication of $E$, restricted to pairs whose left factor lies in $F$ |

The last row is the whole trick: since $F \subseteq E$, a scalar $a \in F$ is *also* an element of $E$, so the product $au$ already makes sense inside $E$ — no new operation is defined, we merely refuse to use the old one in full generality. Closure is immediate: $a, u \in E$ give $au \in E$. Now the eight vector space axioms, one by one.

**The four axioms about addition.** A vector space requires $(V, +)$ to be an abelian group. But the first block of the ring axioms (Section 1, axioms 1–5) says precisely: $(E, +)$ **is** an abelian group. This half is satisfied verbatim — not "follows from," but *is literally the same statement*. The zero vector is $0_E$; the additive inverse of $u$ is $-u$.

**The four axioms about scalar multiplication.** Take $a, b \in F$ and $u, v \in E$ throughout.

- **(V1)** $a(u+v) = au + av$ — exactly **left distributivity** in $E$ (axiom 8), applied to $a, u, v \in E$.
- **(V2)** $(a+b)u = au + bu$ — **right distributivity** in $E$ (axiom 9), but with a subtlety: on the left, $a+b$ is a *scalar* sum computed in $F$, while $E$'s distributive law speaks about sums computed in $E$. These agree only because $F$ is a **sub**field: its operations are by definition the *restrictions* of $E$'s, so adding $a, b$ "in $F$" and "in $E$" is the same computation. (If $F$ were an unrelated field merely injected into $E$ as a set, this axiom could fail.)
- **(V3)** $(ab)u = a(bu)$ — **associativity of multiplication** in $E$ (axiom 7); the same restriction subtlety as (V2), resolved the same way.
- **(V4)** $1 \cdot u = u$ — the **unity** axiom of $E$, *provided* the scalar $1_F$ is the same element as $1_E$. For fields this is automatic:

> **Claim.** If $F \subseteq E$ is a subring which is a field, its unity automatically equals $1_E$.
>
> *Proof.* Let $e = 1_F$. Then $e \cdot e = e$ (computed in $E$, since operations are restricted), so $e(e - 1_E) = 0$. A field has no zero divisors, and $e \neq 0$, hence $e = 1_E$. $\square$
>
> Contrast with general rings, where a subring's unity can genuinely differ from the ambient one (the summary table in Section 3 warns "may differ from $R$'s unity") — the zero-divisor argument is what fields add.

**The complete dictionary:**

| Vector space axiom | Field axiom of $E$ it comes from | Extra ingredient needed |
|---|---|---|
| $(V,+)$ abelian group (4 axioms) | $(E,+)$ abelian group (axioms 1–5) | — |
| $a(u+v) = au+av$ | left distributivity (axiom 8) | — |
| $(a+b)u = au+bu$ | right distributivity (axiom 9) | $F$'s $+$ is the restriction of $E$'s |
| $(ab)u = a(bu)$ | associativity of $\cdot$ (axiom 7) | $F$'s $\cdot$ is the restriction of $E$'s |
| $1u = u$ | unity of $E$ | $1_F = 1_E$ (automatic, by the Claim) |

Every axiom is accounted for, and no field axiom had to be *proved* — only *reread* with certain arguments restricted to $F$. That is the precise sense of "give exactly."

> **What the vector space structure forgets.** The field $E$ can multiply *any* two of its elements ($E \times E \to E$); the vector space structure retains only the slice $F \times E \to E$ (scalar times vector). Multiplying two *vectors* is extra structure that linear algebra does not see. The passage "field $\to$ vector space" is deliberately lossy — and that is its power: what survives is enough to define dimension (the counting $|F| = p^n$ above, and the **degree** $[E:F]$ of `Galois.md`), while what is forgotten is precisely what Galois theory later recovers.

Sanity check on the smallest example, $\mathbb{C}$ over $\mathbb{R}$: vectors are complex numbers, scalars are reals, and $a(x + yi) = ax + ayi$ is complex multiplication restricted to a real left factor — exactly the scalar multiplication of the plane $\mathbb{R}^2$. The familiar picture of $\mathbb{C}$ as a two-dimensional real plane *is* this construction.

We write $\mathbb{F}_q$ (or $GF(q)$, "Galois field") for a field with $q$ elements. One can show any two finite fields of the same order $q = p^n$ are isomorphic, and one exists for every prime power $q$ — this existence is exactly the construction below; uniqueness requires the theory of splitting fields and is not proved here.

#### Constructing $\mathbb{F}_{p^n}$

Combine Sections 14.2–14.3 directly: for any irreducible $f(x) \in \mathbb{Z}_p[x]$ of degree $n$,
$$\mathbb{F}_{p^n} := \mathbb{Z}_p[x]/\langle f(x)\rangle$$
is a field (Corollary, 14.3). By the division algorithm, every coset has a unique representative $c_0 + c_1x + \cdots + c_{n-1}x^{n-1}$ with $c_i \in \mathbb{Z}_p$ (reduce any polynomial modulo $f$), so this field has exactly $p^n$ elements, consistent with the theorem above.

#### Examples

**Example 39 ($\mathbb{F}_4$).** $f(x) = x^2+x+1$ has no root in $\mathbb{Z}_2$: $f(0) = 1$, $f(1) = 1+1+1 = 1$. A degree-2 polynomial with no root is irreducible (a nontrivial factorization would need a degree-1, i.e. root-producing, factor). So
$$\mathbb{F}_4 = \mathbb{Z}_2[x]/\langle x^2+x+1\rangle = \{0,\,1,\,\alpha,\,\alpha+1\}, \qquad \alpha^2 = \alpha + 1 \ \ (\text{since } \alpha^2+\alpha+1=0).$$
Note $\mathbb{F}_4 \not\cong \mathbb{Z}_4$: the latter is not even a field, since $2 \cdot 2 = 0$ in $\mathbb{Z}_4$ makes $2$ a zero divisor.

**Example 40 ($\mathbb{F}_8$).** $f(x) = x^3+x+1$ has no root in $\mathbb{Z}_2$ ($f(0)=1$, $f(1)=1$). Any nontrivial factorization of a cubic must include a linear (degree-1) factor, which would supply a root; since there is none, $f$ is irreducible. Hence
$$\mathbb{F}_8 = \mathbb{Z}_2[x]/\langle x^3+x+1\rangle, \qquad |\mathbb{F}_8| = 2^3 = 8.$$

**Example 41 ($\mathbb{F}_9$).** Over $\mathbb{Z}_3$: $0^2+1=1,\ 1^2+1=2,\ 2^2+1 \equiv 2$, so $x^2+1$ has no root and is irreducible over $\mathbb{Z}_3$ (compare Example 19, same polynomial over $\mathbb{R}$). Hence
$$\mathbb{F}_9 = \mathbb{Z}_3[x]/\langle x^2+1\rangle, \qquad |\mathbb{F}_9| = 3^2 = 9.$$
The same irreducible polynomial produces $\mathbb{C}$ over $\mathbb{R}$ and $\mathbb{F}_9$ over $\mathbb{Z}_3$ — the construction is identical, only the base field changes.

**Non-example.** Over $\mathbb{Z}_2$, $x^2+1 = (x+1)^2$ **factors**, so it is reducible, and $\mathbb{Z}_2[x]/\langle x^2+1\rangle$ is **not** a field: it has the zero divisor $x+1$ (nonzero, but $(x+1)^2 \equiv 0$).

### 14.6 Adjoining a Concrete Element: $F(\alpha)$

Sections 14.3–14.5 build a new field **abstractly**, as a quotient $k[x]/\langle f\rangle$, whose elements are cosets. There is a second, more concrete route: suppose $F$ already sits inside some larger ring $E$ (an **extension ring** of $F$), and pick a specific element $\alpha \in E$. Adjoining $\alpha$ to $F$ produces a field precisely when $\alpha$ satisfies a polynomial condition over $F$.

#### Definitions

Let $E$ be a ring containing $F$ as a subring, and $\alpha \in E$.

- $F[\alpha] = \{\, f(\alpha) \mid f(x) \in F[x] \,\}$, the smallest subring of $E$ containing $F$ and $\alpha$. This is exactly the image of the **evaluation homomorphism** $\operatorname{ev}_\alpha : F[x] \to E$, $f(x) \mapsto f(\alpha)$ — the same construction as Example 12's evaluation-at-$0$ map, now evaluated at $\alpha$ instead.
- If $E$ is a field, $F(\alpha) = \{\, f(\alpha)/g(\alpha) \mid f, g \in F[x],\ g(\alpha) \neq 0 \,\}$ denotes the smallest sub**field** of $E$ containing $F$ and $\alpha$. Clearly $F[\alpha] \subseteq F(\alpha)$, with equality exactly when $F[\alpha]$ is already a field.

> **Reading the notation: $f(x)$ vs. $f(\alpha)$.** In the definition of $F[\alpha]$, the two notations sit deliberately side by side and mean different things:
>
> - $f(x) \in F[x]$ is a **formal polynomial** (形式多项式) — here $x$ is not a number but a placeholder symbol (an *indeterminate*); the polynomial is really just its list of coefficients. Writing "$f(x) \in F[x]$" does *not* mean "$f$ evaluated at $x$" — the parenthesized letter merely names the variable.
> - $f(\alpha)$ is the **value** obtained by substituting the concrete element $\alpha \in E$ into that expression — an actual element of $E$.
>
> Example: $F = \mathbb{Q}$, $\alpha = \sqrt2$, $f(x) = x^2 + 3x + 1$. The formal polynomial $f(x)$ contributes the value $f(\sqrt2) = 2 + 3\sqrt2 + 1 = 3 + 3\sqrt2$ to the set $\mathbb{Q}[\sqrt2]$. Running through *all* polynomials and collecting all values yields the whole of $F[\alpha]$. Thus $F[\alpha]$ answers the question: *which elements of $E$ can be built from $F$ and $\alpha$ using only $+$, $-$, $\times$?* — any such expression, expanded out, is a polynomial evaluated at $\alpha$, which is exactly why $F[\alpha]$ is the smallest sub*ring* (rings have $+,-,\times$ but not division).

> **Reading the notation: the fraction $f(\alpha)/g(\alpha)$.** Two common misreadings to rule out:
>
> 1. **No polynomial divisibility is required.** The division is performed **in the field $E$, between the two values** $f(\alpha)$ and $g(\alpha)$ — it is *not* polynomial division, and $g$ need not divide $f$ in $F[x]$. Example: $f(x) = 1$, $g(x) = x$. The polynomial $x$ certainly does not divide $1$, yet $f(\sqrt2)/g(\sqrt2) = 1/\sqrt2$ is a perfectly legitimate element of $\mathbb{Q}(\sqrt2)$. Since $E$ is a field, *any* nonzero value may serve as a denominator.
> 2. **The condition is $g(\alpha) \neq 0$, not $g \neq 0$.** What must be nonzero is the *value after substitution*, not the polynomial itself. E.g. $g(x) = x^2 - 2$ is a nonzero polynomial, but $g(\sqrt2) = 0$, so it is a forbidden denominator for $\alpha = \sqrt2$. The excluded denominators are exactly the polynomials vanishing at $\alpha$ — i.e. the kernel $\ker(\operatorname{ev}_\alpha)$, which (for algebraic $\alpha$) consists of the multiples of the minimal polynomial.

> **Why the definition allows fractions at all — and why they turn out to be redundant.** A priori, permitting division should produce *more* elements than $F[\alpha]$, which is why the definition of the smallest sub*field* must be written with fractions. The punchline of Theorem (b) below is that for **algebraic** $\alpha$ the fractions are all unnecessary: every $f(\alpha)/g(\alpha)$ can be rewritten as a plain polynomial value $h(\alpha)$, so $F(\alpha) = F[\alpha]$. For instance $1/\sqrt2 = \tfrac{\sqrt2}{2} = \tfrac12\sqrt2$ — the fraction is "digested" into the polynomial $h(x) = \tfrac12 x$; this is the abstract theorem behind the familiar trick of *rationalizing the denominator* (分母有理化). The general mechanism is Bézout in $F[x]$: if $g(\alpha) \neq 0$ then $m \nmid g$, and since the minimal polynomial $m$ is irreducible, $\gcd(g, m) = 1$, so $ug + vm = 1$ for some $u, v \in F[x]$; substituting $\alpha$ kills the $vm$ term and leaves $u(\alpha)\,g(\alpha) = 1$, i.e. $1/g(\alpha) = u(\alpha)$ is itself a polynomial value. By contrast, for **transcendental** $\alpha$ (Theorem (a), e.g. $\alpha = \pi$) the fractions are genuinely needed: $1/\pi$ is not a rational-coefficient polynomial in $\pi$, so $\mathbb{Q}(\pi) \supsetneq \mathbb{Q}[\pi]$ — this is exactly where the two notations part ways.

$\alpha$ is called **algebraic** over $F$ if $f(\alpha) = 0$ for some nonzero $f \in F[x]$; otherwise $\alpha$ is **transcendental** over $F$.

#### Theorem: When is $F[\alpha]$ a Field?

> **Theorem.** Let $E \supseteq F$ be a field extension and $\alpha \in E$.
>
> (a) If $\alpha$ is **transcendental** over $F$, then $F[\alpha] \cong F[x]$, which is **not** a field, and $F(\alpha) \cong F(x)$ (the field of rational functions).
>
> (b) If $\alpha$ is **algebraic** over $F$, let $m(x) \in F[x]$ be the monic generator of $\ker(\operatorname{ev}_\alpha) = \{f \in F[x] \mid f(\alpha) = 0\}$ — the **minimal polynomial** of $\alpha$ over $F$. Then $m$ is irreducible over $F$, and
> $$F[\alpha] \;\cong\; F[x]/\langle m(x)\rangle$$
> is already a field. Consequently $F(\alpha) = F[\alpha]$.

**Proof.** $\operatorname{ev}_\alpha$ is a ring homomorphism (Example 12), so $\ker(\operatorname{ev}_\alpha) \trianglelefteq F[x]$, and since $F[x]$ is a PID (Section 14.2), $\ker(\operatorname{ev}_\alpha) = \langle m(x)\rangle$ for some $m$ — taking $m = 0$ covers the case $\ker(\operatorname{ev}_\alpha) = \{0\}$, and otherwise $m$ is the (unique) monic polynomial of minimal degree in the kernel.

**(a)** If $\alpha$ is transcendental, $\ker(\operatorname{ev}_\alpha) = \{0\}$, so $\operatorname{ev}_\alpha$ is injective. By the First Isomorphism Theorem (Section 9), $F[\alpha] = \operatorname{Im}(\operatorname{ev}_\alpha) \cong F[x]/\{0\} \cong F[x]$. This is not a field ($x$ has no inverse in $F[x]$), so $F(\alpha)$ is strictly larger, namely the field of fractions $F(x)$.

**(b)** If $\alpha$ is algebraic, $m \neq 0$. To see $m$ is irreducible: suppose $m = gh$ with $\deg g, \deg h \geq 1$. Then $g(\alpha)h(\alpha) = m(\alpha) = 0$ in $E$, and since $E$ is a field (hence has no zero divisors), $g(\alpha) = 0$ or $h(\alpha) = 0$. But $\deg g, \deg h < \deg m$, contradicting that $m$ has minimal degree among nonzero elements of $\ker(\operatorname{ev}_\alpha)$. So $m$ is irreducible.

By the First Isomorphism Theorem, $F[\alpha] = \operatorname{Im}(\operatorname{ev}_\alpha) \cong F[x]/\ker(\operatorname{ev}_\alpha) = F[x]/\langle m(x)\rangle$, which is a field by the Corollary in Section 14.3 (since $m$ is irreducible). Since $F[\alpha]$ is already a field and $F(\alpha)$ is by definition the *smallest* field containing $F[\alpha]$, we get $F(\alpha) = F[\alpha]$. $\square$

> **Remark.** The zero-divisor argument in (b) only used that $E$ has no zero divisors — so the conclusion "$m$ is irreducible" and "$F[\alpha] \cong F[x]/\langle m\rangle$ is a field" holds already when $E$ is merely an **integral domain** containing $F$, not necessarily a field.

> **Relation to Kronecker's Theorem (14.4).** This is the same construction as Kronecker's Theorem, run in the opposite direction. There, we started only with the abstract polynomial $f$ and *built* $K = k[x]/\langle f\rangle$, afterward noticing that $\alpha = x + \langle f\rangle$ is a root sitting inside $K$. Here, $\alpha$ is handed to us already, sitting concretely inside a pre-existing $E$, and we discover that the abstract quotient $F[x]/\langle m\rangle$ is an isomorphic copy of the concrete ring $F[\alpha]$ we get by literally plugging $\alpha$ into polynomials.

> **Degree and basis.** When $\alpha$ is algebraic with $\deg m = n$, the isomorphism $F(\alpha) \cong F[x]/\langle m(x)\rangle$ carries the basis $\{1, x, \ldots, x^{n-1}\}$ of the latter (Section 14.5) to $\{1, \alpha, \alpha^2, \ldots, \alpha^{n-1}\}$. So $F(\alpha)$ is an $n$-dimensional $F$-vector space, and every element of $F(\alpha)$ is uniquely $c_0 + c_1\alpha + \cdots + c_{n-1}\alpha^{n-1}$ with $c_i \in F$. This number $n = \deg m$ is called the **degree** of the extension, written $[F(\alpha):F]$.

#### Examples

**Example 42.** $F = \mathbb{R}$, $E = \mathbb{C}$, $\alpha = i$. The minimal polynomial of $i$ over $\mathbb{R}$ is $x^2+1$ (irreducible over $\mathbb{R}$, and $i \notin \mathbb{R}$ rules out any degree-$1$ polynomial vanishing at $i$). So $\mathbb{R}(i) = \mathbb{R}[i] \cong \mathbb{R}[x]/\langle x^2+1\rangle$, and indeed $\mathbb{R}[i] = \{a+bi \mid a,b\in\mathbb{R}\} = \mathbb{C}$ — recovering Example 19 from the concrete side.

**Example 43.** $F = \mathbb{Q}$, $E = \mathbb{R}$, $\alpha = \sqrt{2}$. The minimal polynomial is $x^2-2$ (irreducible over $\mathbb{Q}$, since $\sqrt 2 \notin \mathbb{Q}$). So
$$\mathbb{Q}(\sqrt2) = \mathbb{Q}[\sqrt2] = \{a+b\sqrt2 \mid a,b \in \mathbb{Q}\} \cong \mathbb{Q}[x]/\langle x^2-2\rangle,$$
a field with $[\mathbb{Q}(\sqrt2):\mathbb{Q}] = 2$.

**Example 44.** $F = \mathbb{Q}$, $E = \mathbb{R}$, $\alpha = \pi$. By the Lindemann–Weierstrass theorem, $\pi$ is **transcendental** over $\mathbb{Q}$ (no nonzero rational polynomial vanishes at $\pi$). So $\mathbb{Q}[\pi] \cong \mathbb{Q}[x]$ is *not* a field ($\pi$ itself has no multiplicative inverse expressible as a polynomial in $\pi$ with rational coefficients), and $\mathbb{Q}(\pi) \cong \mathbb{Q}(x)$, the field of rational functions in one variable.

**Non-example.** Take $E = \mathbb{Z}_6$ (not a field, and not a domain) and try to adjoin some $\alpha$: the irreducibility argument in part (b) breaks down precisely because $E$ has zero divisors, so nothing guarantees $F[\alpha]$ is a field — consistent with the Remark above requiring $E$ to be at least an integral domain.

### 14.7 Summary: Routes to a New Field

| Method | Input | Output | Reference |
|---|---|---|---|
| Quotient by a maximal ideal | ring $R$, maximal ideal $M$ | field $R/M$ | 13.2 |
| Adjoin a root of an irreducible polynomial (abstract) | field $k$, irreducible $f \in k[x]$ | field $k[x]/\langle f\rangle \supseteq k$ | 14.3–14.4 |
| Finite field of order $p^n$ | prime $p$, irreducible $f \in \mathbb{Z}_p[x]$, $\deg f = n$ | field $\mathbb{F}_{p^n}$ | 14.5 |
| Adjoin a concrete algebraic element | extension ring/domain $E \supseteq F$, $\alpha \in E$ algebraic over $F$ | field $F(\alpha) = F[\alpha] \cong F[x]/\langle m(x)\rangle$ | 14.6 |

All four are one idea at increasing specificity or from different directions: an irreducible polynomial generates a maximal ideal (14.3), whose quotient collapses the polynomial ring onto a field containing a root of that polynomial. Kronecker's theorem (14.4) builds this root abstractly from scratch; the $F(\alpha)$ construction (14.6) instead starts from a root already sitting in a known extension and recovers the same abstract quotient as its isomorphic description; finite fields (14.5) are the special case where the base field $\mathbb{Z}_p$ is itself finite.
