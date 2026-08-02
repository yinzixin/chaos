# Field Extensions and Galois Theory

*This chapter continues from `ring_field.md`. There we learned to **build** extension fields — as quotients $k[x]/\langle f\rangle$ (Section 14.3–14.4) or by adjoining a concrete element $F(\alpha)$ (Section 14.6). Here we study the **properties** of field extensions themselves: degree, towers, algebraicity, splitting fields, normality, separability — and finally the symmetries of extensions, which is Galois theory.*

## 1. Field Extensions and Degree

### Definition

Let $F$ and $E$ be fields with $F \subseteq E$ (as a subfield, i.e., $F$ is a subring of $E$ that is itself a field, sharing the same $1$). We call $E$ a **field extension** (域扩张) of $F$, written $E/F$ (read "$E$ over $F$" — this is *not* a quotient!).

> **Key observation.** If $E/F$ is a field extension, then $E$ is a **vector space over $F$**: vector addition is the field addition of $E$, and scalar multiplication is the field multiplication of $E$ restricted to $F \times E$. The field axioms of $E$ give exactly the vector space axioms. This single observation imports all of linear algebra into field theory.

### Definition (Degree)

The **degree** (扩张次数) of $E/F$ is the dimension of $E$ as an $F$-vector space:
$$[E : F] = \dim_F E.$$

- If $[E:F] < \infty$, we say $E/F$ is a **finite extension** (有限扩张).
- $[E:F] = 1$ if and only if $E = F$ (the basis $\{1\}$ already spans).

### Examples

**Example 1.** $[\mathbb{C} : \mathbb{R}] = 2$, with basis $\{1, i\}$: every complex number is uniquely $a + bi$ with $a, b \in \mathbb{R}$.

**Example 2.** $[\mathbb{Q}(\sqrt2) : \mathbb{Q}] = 2$, with basis $\{1, \sqrt2\}$ (Example 43 of `ring_field.md`).

**Example 3.** $[\mathbb{F}_{p^n} : \mathbb{F}_p] = n$: the finite field $\mathbb{F}_{p^n} = \mathbb{Z}_p[x]/\langle f\rangle$ has basis $\{1, x, \ldots, x^{n-1}\}$ over $\mathbb{Z}_p$ (Section 14.5 of `ring_field.md`).

> **Notation: what is $\mathbb{F}_p$?** For $p$ prime, $\mathbb{F}_p$ is just a different name for a familiar object:
> $$\mathbb{F}_p = \mathbb{Z}_p = \mathbb{Z}/p\mathbb{Z} = \{0, 1, \ldots, p-1\}, \qquad \text{arithmetic mod } p.$$
> The "$\mathbb{F}$" stands for **field** (the notation $GF(p)$, "Galois field," is also common). All three notations denote the same object; texts switch to $\mathbb{F}_p$ precisely when they want to emphasize its *field* structure rather than its quotient-ring origin.
>
> Concretely, in $\mathbb{F}_5 = \{0,1,2,3,4\}$: $3+4 \equiv 2$, $3\cdot4 \equiv 2$, and $3^{-1} = 2$ (since $3 \cdot 2 = 6 \equiv 1$) — that last computation is the point: every nonzero element is invertible, which is what makes it a field and not merely a ring. Primality of $p$ is essential (`ring_field.md`, Section 10): $\mathbb{Z}_p$ is a field iff $p$ is prime; in $\mathbb{Z}_6$, $2 \cdot 3 = 0$, so there is no field "$\mathbb{F}_6$."
>
> The general convention is $\mathbb{F}_q$ = the field with exactly $q$ elements, which exists iff $q = p^n$ is a prime power. **One trap:** for $n \ge 2$,
> $$\mathbb{F}_{p^n} \neq \mathbb{Z}_{p^n}.$$
> E.g. $\mathbb{F}_4$ is *not* $\mathbb{Z}_4$ (which has the zero divisor $2$); rather $\mathbb{F}_4 = \mathbb{Z}_2[x]/\langle x^2+x+1\rangle$ (Example 39 of `ring_field.md`). In general $\mathbb{F}_{p^n} = \mathbb{F}_p[x]/\langle f\rangle$ for an irreducible $f$ of degree $n$, and $\mathbb{F}_p$ sits inside it as the **prime subfield** (素域) — the base field of this very example.

**Example 4.** $[\mathbb{R} : \mathbb{Q}] = \infty$. Indeed any finite extension of $\mathbb{Q}$ is countable, but $\mathbb{R}$ is uncountable. (Also $[\mathbb{Q}(\pi):\mathbb{Q}] = \infty$, since $\pi$ is transcendental — see Section 3.)

**Example 5 (degree of a simple algebraic extension).** If $\alpha$ is algebraic over $F$ with minimal polynomial $m(x)$ of degree $n$, then
$$[F(\alpha) : F] = n = \deg m,$$
with basis $\{1, \alpha, \alpha^2, \ldots, \alpha^{n-1}\}$. This was proved in Section 14.6 of `ring_field.md` ("Degree and basis" remark).

---

## 2. The Tower Law

The single most-used computational tool in the subject.

### Theorem (Tower Law / 望远镜公式)

> **Theorem.** Let $F \subseteq K \subseteq E$ be a tower of field extensions. Then
> $$[E : F] = [E : K] \cdot [K : F].$$
> In particular, $E/F$ is finite if and only if both $E/K$ and $K/F$ are finite.

**Proof.** Suppose $[K:F] = m$ with $F$-basis $\{u_1, \ldots, u_m\}$ of $K$, and $[E:K] = n$ with $K$-basis $\{v_1, \ldots, v_n\}$ of $E$. We claim the $mn$ products
$$\{\, u_i v_j \mid 1 \le i \le m,\ 1 \le j \le n \,\}$$
form an $F$-basis of $E$.

*Spanning.* Let $e \in E$. Since $\{v_j\}$ spans $E$ over $K$, write $e = \sum_{j=1}^n c_j v_j$ with $c_j \in K$. Since $\{u_i\}$ spans $K$ over $F$, write each $c_j = \sum_{i=1}^m a_{ij} u_i$ with $a_{ij} \in F$. Substituting:
$$e = \sum_{j=1}^n \Big( \sum_{i=1}^m a_{ij} u_i \Big) v_j = \sum_{i,j} a_{ij}\, u_i v_j,$$
an $F$-linear combination of the $u_i v_j$. $\checkmark$

*Linear independence.* Suppose $\sum_{i,j} a_{ij} u_i v_j = 0$ with $a_{ij} \in F$. Group by $v_j$:
$$\sum_{j=1}^n \underbrace{\Big( \sum_{i=1}^m a_{ij} u_i \Big)}_{\in\, K} v_j = 0.$$
Since $\{v_j\}$ is linearly independent over $K$, each inner sum vanishes: $\sum_i a_{ij} u_i = 0$ for every $j$. Since $\{u_i\}$ is linearly independent over $F$, every $a_{ij} = 0$. $\checkmark$

Hence $[E:F] = mn = [E:K][K:F]$. (The infinite cases are checked similarly: if either step is infinite, an infinite independent set survives into $E/F$.) $\square$

### Consequences

> **Corollary (divisibility constraint).** If $F \subseteq K \subseteq E$ with $[E:F]$ finite, then $[K:F]$ **divides** $[E:F]$.

This turns degree computations into arithmetic. Two standard uses:

**Example 6.** $\sqrt[3]{2} \notin \mathbb{Q}(\sqrt2)$.

*Proof.* $[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}] = 3$ (minimal polynomial $x^3 - 2$, irreducible by Eisenstein at $p=2$). If $\sqrt[3]2 \in \mathbb{Q}(\sqrt2)$, then $\mathbb{Q} \subseteq \mathbb{Q}(\sqrt[3]2) \subseteq \mathbb{Q}(\sqrt2)$, so by the corollary $3 \mid [\mathbb{Q}(\sqrt2):\mathbb{Q}] = 2$ — impossible. $\times$

**Example 7 ($\mathbb{Q}(\sqrt2, \sqrt3)$, a degree-4 tower).** Build the tower $\mathbb{Q} \subseteq \mathbb{Q}(\sqrt2) \subseteq \mathbb{Q}(\sqrt2, \sqrt3)$.

- $[\mathbb{Q}(\sqrt2):\mathbb{Q}] = 2$.
- $[\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}(\sqrt2)] = 2$: we must check $\sqrt3 \notin \mathbb{Q}(\sqrt2)$, so that $x^2 - 3$ stays irreducible over $\mathbb{Q}(\sqrt2)$. Suppose $\sqrt3 = a + b\sqrt2$ with $a,b \in \mathbb{Q}$. Squaring: $3 = a^2 + 2b^2 + 2ab\sqrt2$. Since $\sqrt2 \notin \mathbb{Q}$, we need $ab = 0$. If $b = 0$: $\sqrt3 = a \in \mathbb{Q}$, false. If $a = 0$: $\sqrt3 = b\sqrt2$, so $\sqrt{3/2} = b \in \mathbb{Q}$, i.e. $3/2$ is a rational square, false. $\times$

By the Tower Law:
$$[\mathbb{Q}(\sqrt2,\sqrt3) : \mathbb{Q}] = 2 \cdot 2 = 4, \qquad \text{basis } \{1, \sqrt2, \sqrt3, \sqrt6\}$$
(the pairwise products $u_i v_j$ from the proof: $\{1,\sqrt2\} \times \{1,\sqrt3\}$).

---

## 3. Algebraic Extensions

Recall (Section 14.6 of `ring_field.md`): $\alpha \in E$ is **algebraic** (代数的) over $F$ if $f(\alpha) = 0$ for some nonzero $f \in F[x]$, and **transcendental** (超越的) otherwise.

### Definition

An extension $E/F$ is an **algebraic extension** (代数扩张) if *every* element of $E$ is algebraic over $F$.

### Theorem (Finite $\Rightarrow$ Algebraic)

> **Theorem.** Every finite extension is algebraic. More precisely, if $[E:F] = n < \infty$, then every $\alpha \in E$ is algebraic over $F$ with $\deg m_\alpha \le n$.

**Proof.** Let $\alpha \in E$. The $n+1$ elements
$$1,\ \alpha,\ \alpha^2,\ \ldots,\ \alpha^n$$
live in an $n$-dimensional $F$-vector space, so they are linearly **dependent** over $F$: there exist $c_0, \ldots, c_n \in F$, not all zero, with
$$c_0 + c_1\alpha + \cdots + c_n\alpha^n = 0.$$
Then $f(x) = c_0 + c_1 x + \cdots + c_n x^n$ is a nonzero polynomial in $F[x]$ with $f(\alpha) = 0$, so $\alpha$ is algebraic of degree $\le n$. $\square$

> **The converse is false.** Algebraic does not imply finite. The field $\overline{\mathbb{Q}}$ of *all* algebraic numbers (see Example 9) is an algebraic extension of $\mathbb{Q}$ of infinite degree: it contains $\sqrt[n]{2}$ of degree $n$ for every $n$, so no finite bound on $[\overline{\mathbb{Q}}:\mathbb{Q}]$ is possible.

### Theorem (Algebraic Elements Form a Field)

> **Theorem.** Let $E/F$ be a field extension. If $\alpha, \beta \in E$ are algebraic over $F$ (with $\beta \neq 0$ where needed), then
> $$\alpha + \beta,\quad \alpha - \beta,\quad \alpha\beta,\quad \alpha/\beta$$
> are all algebraic over $F$. Hence the set of elements of $E$ algebraic over $F$ is a subfield of $E$.

**Proof.** The trick is to avoid writing down any explicit polynomial for $\alpha + \beta$ (which is painful) and instead count dimensions.

Let $\alpha$ have degree $m$ and $\beta$ degree $n$ over $F$. Build the tower
$$F \subseteq F(\alpha) \subseteq F(\alpha, \beta) := F(\alpha)(\beta).$$
- $[F(\alpha):F] = m$ (Example 5).
- $\beta$ satisfies its minimal polynomial over $F$, which is *also* a polynomial over the larger field $F(\alpha)$ — perhaps no longer minimal, but still a witness of algebraicity. Hence $[F(\alpha)(\beta) : F(\alpha)] \le n$.

By the Tower Law:
$$[F(\alpha,\beta) : F] = [F(\alpha,\beta):F(\alpha)]\cdot[F(\alpha):F] \le nm < \infty.$$
So $F(\alpha,\beta)$ is a **finite** extension of $F$, hence **algebraic** (previous theorem). But $\alpha+\beta$, $\alpha-\beta$, $\alpha\beta$, $\alpha/\beta$ all live inside $F(\alpha,\beta)$ — so each is algebraic over $F$. $\square$

> **Remark.** Note how indirect this is: we never exhibit the minimal polynomial of $\alpha + \beta$; we only trap it inside a finite-dimensional vector space. Linear algebra does the work that explicit computation cannot.

### Theorem (Transitivity of Algebraicity)

> **Theorem.** If $E/K$ is algebraic and $K/F$ is algebraic, then $E/F$ is algebraic.

**Proof.** Let $\alpha \in E$. It satisfies some $f(x) = c_0 + c_1x + \cdots + c_rx^r \in K[x]$, $f \neq 0$. Only the finitely many coefficients $c_0, \ldots, c_r$ are involved, and each is algebraic over $F$. Build the tower
$$F \subseteq F(c_0, \ldots, c_r) \subseteq F(c_0, \ldots, c_r, \alpha).$$
The first step is finite (adjoin finitely many algebraic elements, applying the previous theorem's tower argument $r+1$ times). The second step is finite because $\alpha$ is algebraic over $F(c_0,\ldots,c_r)$ — the polynomial $f$ has its coefficients there. By the Tower Law the whole tower is finite over $F$, hence algebraic, so $\alpha$ is algebraic over $F$. $\square$

### Examples

**Example 8.** $\sqrt2 + \sqrt3$ is algebraic over $\mathbb{Q}$ — guaranteed by the theorem with no computation. (For the curious: squaring twice gives its minimal polynomial $x^4 - 10x^2 + 1$, and its degree is indeed $4 = [\mathbb{Q}(\sqrt2,\sqrt3):\mathbb{Q}]$; in fact $\mathbb{Q}(\sqrt2+\sqrt3) = \mathbb{Q}(\sqrt2,\sqrt3)$.)

**Example 9 (the field of algebraic numbers).** $\overline{\mathbb{Q}} = \{\alpha \in \mathbb{C} \mid \alpha \text{ algebraic over } \mathbb{Q}\}$ is a field, by the theorem above. It is countable (there are countably many rational polynomials, each with finitely many roots), so "most" complex numbers are transcendental — even though proving any *specific* number transcendental (e.g. $\pi$, Example 44 of `ring_field.md`) is hard.

### How large can the degree of an algebraic element be? It depends on the base field

Over $\mathbb{Q}$, algebraic elements of arbitrarily large degree exist: $x^n - 2$ is irreducible for every $n$ (Eisenstein at 2), so $\sqrt[n]2$ has degree exactly $n$. Over $\mathbb{R}$, the situation collapses dramatically:

> **Theorem.** Every irreducible polynomial in $\mathbb{R}[x]$ has degree $1$ or $2$. Consequently, if $\alpha$ is algebraic over $\mathbb{R}$, then $\deg m_\alpha \le 2$ — and the only algebraic extensions of $\mathbb{R}$ are $\mathbb{R}$ itself and (up to isomorphism) $\mathbb{C}$.

**Proof.** Let $f \in \mathbb{R}[x]$, $\deg f \ge 1$. By the **Fundamental Theorem of Algebra** (代数基本定理), $f$ splits completely over $\mathbb{C}$:
$$f(x) = c\,(x - z_1)(x - z_2)\cdots(x - z_n), \qquad z_i \in \mathbb{C}.$$
Since $f$ has *real* coefficients, conjugating $f(z) = 0$ gives $f(\bar z) = \overline{f(z)} = 0$ — so **non-real roots come in conjugate pairs** $z, \bar z$. Each such pair merges into a single factor with *real* coefficients:
$$(x - z)(x - \bar z) = x^2 - 2\operatorname{Re}(z)\,x + |z|^2 \;\in\; \mathbb{R}[x].$$
Hence every real polynomial factors over $\mathbb{R}$ into linear factors (real roots) and quadratics with negative discriminant (conjugate pairs). A polynomial of degree $\ge 3$ always factors, so it is never irreducible over $\mathbb{R}$. Since the minimal polynomial is irreducible, $\deg m_\alpha \le 2$. $\square$

(Example 38 of `ring_field.md` showed this concretely: $x^4+1$ is irreducible over $\mathbb{Q}$ but breaks over $\mathbb{R}$ into $(x^2-\sqrt2\,x+1)(x^2+\sqrt2\,x+1)$.)

The two possible cases for $\alpha$ algebraic over $\mathbb{R}$:

| $\deg m_\alpha$ | Meaning | Resulting field |
|:---:|---|---|
| 1 | $m_\alpha = x - \alpha$, i.e. $\alpha \in \mathbb{R}$ already | $\mathbb{R}(\alpha) = \mathbb{R}$ |
| 2 | $\alpha \notin \mathbb{R}$, e.g. $\alpha = i$ with $m = x^2+1$ | $\mathbb{R}(\alpha) \cong \mathbb{R}[x]/\langle m\rangle \cong \mathbb{C}$ |

Every degree-2 quotient $\mathbb{R}[x]/\langle x^2+bx+c\rangle$ (discriminant $<0$) is just $\mathbb{C}$ wearing a different irreducible polynomial.

> **The spectrum across base fields.** A field $K$ is **algebraically closed** (代数闭域) if every non-constant polynomial in $K[x]$ has a root in $K$ — equivalently, the only irreducible polynomials are linear, so the only element algebraic over $K$ is one already in $K$.
>
> | Base field | Max degree of an irreducible polynomial | Why |
> |---|:---:|---|
> | $\mathbb{C}$ | $1$ | algebraically closed (Fundamental Theorem of Algebra) |
> | $\mathbb{R}$ | $2$ | sits one step below its algebraic closure: $[\mathbb{C}:\mathbb{R}] = 2$ |
> | $\mathbb{Q}$, $\mathbb{F}_p$ | unbounded | $x^n - 2$ (Eisenstein); irreducibles of every degree $n$ exist over $\mathbb{F}_p$ (they construct $\mathbb{F}_{p^n}$, Section 14.5 of `ring_field.md`) |
>
> The bound $2$ for $\mathbb{R}$ is really the statement $[\mathbb{C}:\mathbb{R}] = 2$ in disguise: any $\alpha$ algebraic over $\mathbb{R}$ generates $\mathbb{R}(\alpha) \subseteq \mathbb{C}$ (up to isomorphism), and by the Tower Law its degree must divide $2$.

---

## 4. Splitting Fields

Kronecker's theorem (Section 14.4 of `ring_field.md`) adjoins **one** root of $f$. We now adjoin **all** of them.

### Definition

Let $F$ be a field and $f \in F[x]$ non-constant. We say $f$ **splits** (分裂) in an extension $E \supseteq F$ if it factors into linear factors there:
$$f(x) = c\,(x - \alpha_1)(x - \alpha_2)\cdots(x - \alpha_n), \qquad c \in F,\ \alpha_i \in E.$$

$E$ is a **splitting field** (分裂域) of $f$ over $F$ if
1. $f$ splits in $E$, and
2. $E$ is generated by the roots: $E = F(\alpha_1, \ldots, \alpha_n)$ — no proper subfield of $E$ containing $F$ splits $f$.

Condition 2 makes the splitting field *minimal*: it contains exactly what is needed and nothing more.

### Theorem (Existence)

> **Theorem.** Every non-constant $f \in F[x]$ has a splitting field $E$ over $F$, with $[E : F] \le (\deg f)!$.

**Proof.** Induction on $n = \deg f$. If $n = 1$, $f$ is already linear; take $E = F$.

For $n > 1$: by Kronecker's theorem, there is an extension $F_1 = F(\alpha_1) \supseteq F$ containing a root $\alpha_1$ of $f$, with $[F_1 : F] \le n$ (the minimal polynomial of $\alpha_1$ divides $f$, so has degree $\le n$). Over $F_1$, factor $f(x) = (x - \alpha_1)\,g(x)$ with $\deg g = n - 1$ (division algorithm: divide $f$ by $x - \alpha_1$; the remainder is the constant $f(\alpha_1) = 0$). By the inductive hypothesis, $g$ has a splitting field $E$ over $F_1$ with $[E : F_1] \le (n-1)!$. Then $f$ splits in $E$, $E$ is generated over $F$ by the roots of $f$, and by the Tower Law
$$[E:F] = [E:F_1][F_1:F] \le (n-1)! \cdot n = n!. \qquad \square$$

### Theorem (Uniqueness)

> **Theorem.** Any two splitting fields of $f$ over $F$ are isomorphic via an isomorphism fixing $F$ pointwise.

*Idea of proof.* One proves the stronger statement: any isomorphism $\sigma : F \to F'$ extends to an isomorphism of splitting fields $E \to E'$ (of $f$ and $\sigma f$ respectively), by induction on $[E:F]$. The key step: a root $\alpha$ of an irreducible factor $p$ of $f$ satisfies $F(\alpha) \cong F[x]/\langle p\rangle \cong F'[x]/\langle \sigma p\rangle \cong F'(\alpha')$ for any root $\alpha'$ of $\sigma p$ — the abstract quotient description (Section 14.6 of `ring_field.md`) doesn't care which root is chosen. This freedom of choice is exactly where the *symmetries* of Section 7 will come from. $\square$

Because of uniqueness we may speak of **the** splitting field of $f$ over $F$.

### Examples

**Example 10.** The splitting field of $x^2 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt2, -\sqrt2) = \mathbb{Q}(\sqrt2)$, of degree $2$. Adjoining one root was already enough — the other root came for free ($-\sqrt2 = -1\cdot\sqrt2$).

**Example 11 (one root is not always enough).** The splitting field of $f(x) = x^3 - 2$ over $\mathbb{Q}$.

The roots in $\mathbb{C}$ are $\sqrt[3]2,\ \omega\sqrt[3]2,\ \omega^2\sqrt[3]2$, where $\omega = e^{2\pi i/3} = \frac{-1+\sqrt{-3}}{2}$ is a primitive cube root of unity.

- $\mathbb{Q}(\sqrt[3]2)$ is **not** a splitting field: it lies inside $\mathbb{R}$, but the other two roots are non-real. Adjoining one root of a cubic can fail to catch the others.
- The splitting field is $E = \mathbb{Q}(\sqrt[3]2, \omega)$. Tower: $[\mathbb{Q}(\sqrt[3]2):\mathbb{Q}] = 3$, and $\omega$ has minimal polynomial $x^2 + x + 1$ over $\mathbb{Q}(\sqrt[3]2)$ (still irreducible there, since $\mathbb{Q}(\sqrt[3]2) \subseteq \mathbb{R}$ contains no non-real roots), so
$$[E : \mathbb{Q}] = 3 \cdot 2 = 6 = 3!.$$
The upper bound $(\deg f)!$ from the existence theorem is attained.

**Example 12.** The splitting field of $x^4 + 1$ over $\mathbb{Q}$ is $\mathbb{Q}(\zeta_8) = \mathbb{Q}(i, \sqrt2)$, of degree $4$ — Example 38 of `ring_field.md` already showed $\mathbb{Q}[x]/\langle x^4{+}1\rangle \cong \mathbb{Q}(\zeta_8)$, and all four roots $\zeta_8, \zeta_8^3, \zeta_8^5, \zeta_8^7$ are powers of $\zeta_8$, so adjoining one root splits the whole polynomial. Here $[E:\mathbb{Q}] = 4 < 4! = 24$: how much of the bound is used depends on how entangled the roots are.

**Example 13 (finite fields as splitting fields).** $\mathbb{F}_{p^n}$ is the splitting field of $x^{p^n} - x$ over $\mathbb{F}_p$. Every element $\alpha \in \mathbb{F}_{p^n}$ satisfies $\alpha^{p^n} = \alpha$ (for $\alpha \neq 0$ this is Lagrange's theorem in the multiplicative group $\mathbb{F}_{p^n}^\times$ of order $p^n - 1$), so the $p^n$ elements of the field are exactly the $p^n$ roots of $x^{p^n} - x$. This is the cleanest proof that **the finite field of order $p^n$ is unique up to isomorphism**: it is *the* splitting field of one specific polynomial.

---

## 5. Normal Extensions

### Definition

An algebraic extension $E/F$ is **normal** (正规扩张) if every irreducible polynomial in $F[x]$ that has *at least one* root in $E$ splits *completely* in $E$.

Informally: $E$ makes no half-hearted promises. If it contains one root of an irreducible polynomial, it contains the whole family.

### Theorem (Normal $=$ Splitting Field)

> **Theorem.** A finite extension $E/F$ is normal if and only if $E$ is the splitting field of some polynomial in $F[x]$.

*Proof sketch.* ($\Rightarrow$) Write $E = F(\alpha_1,\ldots,\alpha_k)$ (finitely generated since finite); let $m_i$ be the minimal polynomial of $\alpha_i$. Each $m_i$ has a root in $E$, so by normality splits in $E$; hence $E$ is the splitting field of $f = m_1 m_2 \cdots m_k$. ($\Leftarrow$) The direction that carries content: if $E$ is a splitting field of $f$ and an irreducible $p \in F[x]$ has a root $\alpha \in E$, one compares $E(\beta)$ for any other root $\beta$ of $p$ and shows $[E(\alpha):E] = [E(\beta):E]$ using the uniqueness-of-splitting-field machinery; since $\alpha \in E$ the left side is $1$, forcing $\beta \in E$. $\square$

### Examples

**Example 14.** $\mathbb{Q}(\sqrt2)/\mathbb{Q}$ is normal: it is the splitting field of $x^2-2$ (Example 10). Every degree-2 extension is normal by the same one-root-gives-the-other argument: if $\alpha$ is a root of an irreducible quadratic $x^2+bx+c$, the other root is $-b-\alpha$, already present.

**Non-example.** $\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$ is **not** normal: $x^3-2$ is irreducible over $\mathbb{Q}$ with a root $\sqrt[3]2$ in the field, but the two complex roots are missing (Example 11). The "defect" is repaired by enlarging to the splitting field $\mathbb{Q}(\sqrt[3]2, \omega)$, which *is* normal.

> **Warning (normality is not transitive).** $\mathbb{Q} \subseteq \mathbb{Q}(\sqrt2) \subseteq \mathbb{Q}(\sqrt[4]2)$: each step is a degree-2 extension, hence normal, but the composite $\mathbb{Q}(\sqrt[4]2)/\mathbb{Q}$ is not normal — $x^4 - 2$ is irreducible over $\mathbb{Q}$ (Eisenstein at 2) with root $\sqrt[4]2$ in the field, yet the roots $\pm i\sqrt[4]2$ are absent. Contrast with the Tower Law for degrees, which always composes.

---

## 6. Separable Extensions

### Definition

An irreducible polynomial $f \in F[x]$ is **separable** (可分) if it has no repeated roots in its splitting field. An algebraic element $\alpha$ is separable over $F$ if its minimal polynomial is; an algebraic extension $E/F$ is a **separable extension** if every element of $E$ is separable over $F$.

### Detecting repeated roots: the formal derivative

Define the **formal derivative** $D(\sum a_ix^i) = \sum i\,a_i x^{i-1}$ — a purely algebraic operation (no limits), which still satisfies the sum and product rules.

> **Proposition.** $f$ has a repeated root (in a splitting field) $\iff$ $\gcd(f, Df) \neq 1$.
>
> *Proof.* If $f = (x-\alpha)^2 g$, then $Df = 2(x-\alpha)g + (x-\alpha)^2 Dg$ is divisible by $x - \alpha$, so $x - \alpha$ divides $\gcd(f, Df)$. Conversely if all roots are simple, $f = c\prod(x-\alpha_i)$ with distinct $\alpha_i$, and $Df(\alpha_i) = c\prod_{j\neq i}(\alpha_i - \alpha_j) \neq 0$, so $f$ and $Df$ share no root. $\square$

> **Corollary.** An irreducible $f$ is inseparable $\iff$ $Df = 0$. (For irreducible $f$, $\gcd(f, Df) \neq 1$ forces $f \mid Df$; since $\deg Df < \deg f$, this means $Df = 0$.)
>
> Over a field of characteristic $0$, $Df = 0$ is impossible for non-constant $f$ — so **in characteristic $0$, every algebraic extension is separable.** In characteristic $p$, $Df = 0$ happens exactly when $f$ is a polynomial in $x^p$.

### Examples

**Example 15.** Everything over $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ is separable (characteristic $0$).

**Example 16.** Every extension of finite fields is separable. Reason: $\mathbb{F}_{p^n}$ is the splitting field of $x^{p^n} - x$ (Example 13), whose derivative is $p^n x^{p^n - 1} - 1 = -1 \neq 0$, so all $p^n$ roots are distinct.

**Non-example (the standard inseparable extension).** Let $F = \mathbb{F}_p(t)$, rational functions over $\mathbb{F}_p$, and $f(x) = x^p - t \in F[x]$. One shows $f$ is irreducible, but in its splitting field, letting $\alpha$ be a root ($\alpha^p = t$), the Freshman's Dream (characteristic $p$) gives
$$x^p - t = x^p - \alpha^p = (x - \alpha)^p$$
— a single root repeated $p$ times. So $F(\alpha)/F$ is inseparable. Note this needed characteristic $p$ *and* an infinite base field with the "fresh" element $t$; finite fields dodge this (Example 16).

> **Fields where inseparability never occurs** (e.g. characteristic $0$ fields, finite fields) are called **perfect fields** (完全域). For the rest of this chapter one may safely think of characteristic $0$; separability then holds automatically.

---

## 7. Automorphisms and the Galois Group

We now shift viewpoint — from the *elements* of an extension to its *symmetries*. This is the same move group theory makes everywhere: study an object through its structure-preserving self-maps.

### Definition

Let $E/F$ be a field extension. An **$F$-automorphism** of $E$ is a ring automorphism $\sigma : E \to E$ (bijective, preserving $+$ and $\cdot$ — Section 4 of `ring_field.md`) that fixes $F$ pointwise:
$$\sigma(a) = a \quad \text{for all } a \in F.$$

The set of all $F$-automorphisms of $E$ forms a **group under composition**, denoted
$$\operatorname{Gal}(E/F) = \operatorname{Aut}(E/F),$$
the **Galois group** (伽罗瓦群) of the extension.

*Verification that it is a group:* the identity map fixes $F$; a composition of two $F$-automorphisms is an $F$-automorphism; the inverse of a bijective homomorphism is a homomorphism, and if $\sigma$ fixes $F$ so does $\sigma^{-1}$. $\checkmark$

### The Fundamental Constraint: Automorphisms Permute Roots

> **Proposition.** Let $\sigma \in \operatorname{Gal}(E/F)$ and $f \in F[x]$. If $\alpha \in E$ is a root of $f$, then $\sigma(\alpha)$ is also a root of $f$.

**Proof.** Write $f(x) = c_0 + c_1 x + \cdots + c_n x^n$ with $c_i \in F$. Apply $\sigma$ to $f(\alpha) = 0$:
$$0 = \sigma(0) = \sigma\big(c_0 + c_1\alpha + \cdots + c_n\alpha^n\big) = \sigma(c_0) + \sigma(c_1)\sigma(\alpha) + \cdots + \sigma(c_n)\sigma(\alpha)^n$$
$$= c_0 + c_1\,\sigma(\alpha) + \cdots + c_n\,\sigma(\alpha)^n = f(\sigma(\alpha)),$$
using that $\sigma$ preserves $+$, $\cdot$, and fixes each $c_i \in F$. $\square$

> **Consequences.**
> 1. An automorphism $\sigma$ is completely determined by where it sends the generators: if $E = F(\alpha_1, \ldots, \alpha_k)$, then every element of $E$ is a rational expression in the $\alpha_i$ with coefficients in $F$, and $\sigma$ is pinned down by $\sigma(\alpha_1), \ldots, \sigma(\alpha_k)$.
> 2. Each $\sigma(\alpha_i)$ must be a root of the minimal polynomial of $\alpha_i$ — of which there are at most $\deg m_i$. So $\operatorname{Gal}(E/F)$ is **finite** whenever $E/F$ is finite, and we get the bound $|\operatorname{Gal}(E/F)| \le [E:F]$ (proved precisely below).

### Examples

**Example 17.** $\operatorname{Gal}(\mathbb{C}/\mathbb{R}) = \{\mathrm{id}, \text{conjugation}\} \cong \mathbb{Z}_2$.

Any $\sigma$ fixes $\mathbb{R}$ and must send $i$ to a root of $x^2 + 1$, so $\sigma(i) = \pm i$. Both choices work: $\sigma(i) = i$ gives the identity; $\sigma(i) = -i$ gives complex conjugation (Example 11 of `ring_field.md` verified it is an automorphism, and it fixes exactly $\mathbb{R}$).

**Example 18.** $\operatorname{Gal}(\mathbb{Q}(\sqrt2)/\mathbb{Q}) = \{\mathrm{id},\ \sigma\} \cong \mathbb{Z}_2$, where $\sigma(a + b\sqrt2) = a - b\sqrt2$.

$\sigma$ must send $\sqrt2$ to a root of $x^2 - 2$, i.e. to $\pm\sqrt2$. Note $\sigma$ is "conjugation" again — the pattern of Example 17 with $\sqrt2$ in place of $i$.

**Example 19.** $\operatorname{Gal}(\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}) = \{\mathrm{id}\}$ — trivial, even though the extension has degree 3!

Any $\sigma$ must send $\sqrt[3]2$ to a root of $x^3 - 2$ *lying in* $\mathbb{Q}(\sqrt[3]2)$. But $\mathbb{Q}(\sqrt[3]2) \subset \mathbb{R}$ contains only the one real root (Example 11). So $\sigma(\sqrt[3]2) = \sqrt[3]2$ and $\sigma = \mathrm{id}$.

Here $|\operatorname{Gal}(E/F)| = 1 < 3 = [E:F]$: the group is "too small" for the extension. The culprit is the failure of **normality** — the missing roots leave the automorphisms with nowhere to go. This deficiency is exactly what the next definition rules out.

**Example 20.** $\operatorname{Gal}(\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}) \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (the Klein four-group).

An automorphism may independently send $\sqrt2 \mapsto \pm\sqrt2$ and $\sqrt3 \mapsto \pm\sqrt3$ (each must go to a root of its minimal polynomial, and all four sign combinations do define automorphisms). All four elements have order $\le 2$, so the group is $\mathbb{Z}_2 \times \mathbb{Z}_2$, of order $4 = [E:\mathbb{Q}]$ (Example 7) — this extension has a "full" group.

**Example 21 (Frobenius).** $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) \cong \mathbb{Z}_n$, cyclic, generated by the **Frobenius automorphism**
$$\varphi : \alpha \mapsto \alpha^p.$$
*Why $\varphi$ is a homomorphism:* $(\alpha\beta)^p = \alpha^p\beta^p$ always, and $(\alpha+\beta)^p = \alpha^p + \beta^p$ by Freshman's Dream in characteristic $p$ (the binomial coefficients $\binom{p}{k}$, $0 < k < p$, are divisible by $p$). It fixes $\mathbb{F}_p$ since $a^p = a$ there (Fermat's little theorem). It is injective (field homomorphisms from a field are injective — kernel is an ideal of a simple ring, Example 16 of `ring_field.md`), hence bijective on the finite set $\mathbb{F}_{p^n}$. Finally $\varphi^n = \mathrm{id}$ (that is $\alpha^{p^n} = \alpha$, Example 13) and no smaller power is the identity (a polynomial $x^{p^k} - x$ with $k < n$ has at most $p^k < p^n$ roots), so $\varphi$ generates a cyclic group of order exactly $n$.

---

## 8. Fixed Fields and Galois Extensions

### Definition

Let $G$ be a group of automorphisms of a field $E$. The **fixed field** (固定域) of $G$ is
$$E^G = \{ a \in E \mid \sigma(a) = a \ \text{for all } \sigma \in G \}.$$

*Verification that $E^G$ is a subfield:* if $\sigma(a) = a$ and $\sigma(b) = b$, then $\sigma(a - b) = a - b$ and $\sigma(ab^{-1}) = ab^{-1}$ (automorphisms preserve all field operations). $\checkmark$

By construction $F \subseteq E^{\operatorname{Gal}(E/F)}$ — the base field is always fixed. The pivotal question: **is it *exactly* $F$, or something bigger?**

**Example 22.** For $E = \mathbb{Q}(\sqrt[3]2)$, $F = \mathbb{Q}$: the Galois group is trivial (Example 19), so its fixed field is all of $E \supsetneq F$. The group is too weak to "see" that $\sqrt[3]2$ is not rational.

**Example 23.** For $E = \mathbb{Q}(\sqrt2)$, $F = \mathbb{Q}$: an element $a + b\sqrt2$ fixed by $\sigma$ satisfies $a + b\sqrt2 = a - b\sqrt2$, so $b = 0$. The fixed field is exactly $\mathbb{Q}$. $\checkmark$

### Definition (Galois Extension)

A finite extension $E/F$ is a **Galois extension** (伽罗瓦扩张) if
$$E^{\operatorname{Gal}(E/F)} = F,$$
i.e., the only elements fixed by *every* $F$-automorphism are the elements of $F$ itself — the symmetry group is large enough to detect everything outside $F$.

### Theorem (Characterizations of Galois)

> **Theorem.** For a finite extension $E/F$, the following are equivalent:
>
> 1. $E/F$ is Galois (fixed field of the Galois group is exactly $F$);
> 2. $|\operatorname{Gal}(E/F)| = [E : F]$;
> 3. $E/F$ is **normal and separable**;
> 4. $E$ is the splitting field over $F$ of a separable polynomial.
>
> In general one always has $|\operatorname{Gal}(E/F)| \le [E:F]$; Galois extensions are exactly the case of equality.

*Proof idea for the inequality and for (4) $\Rightarrow$ (2).* Count extensions of automorphisms one generator at a time: an embedding defined on $F(\alpha)$ must send $\alpha$ to a root of its minimal polynomial $m$, giving at most $\deg m = [F(\alpha):F]$ choices — with **exactly** that many available precisely when $m$ splits in $E$ (normality supplies the roots) with distinct roots (separability makes them genuinely different choices). Induction up the tower, multiplying choices, matches the Tower Law's multiplication of degrees. Artin's lemma ($[E : E^G] \le |G|$ for any finite automorphism group $G$) closes the remaining implications. $\square$

*Sanity check against the examples:* $\mathbb{Q}(\sqrt2)/\mathbb{Q}$: order $2 =$ degree $2$, Galois $\checkmark$ (and indeed normal: Example 14). $\mathbb{Q}(\sqrt2,\sqrt3)/\mathbb{Q}$: order $4 =$ degree $4$, Galois $\checkmark$. $\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$: order $1 < 3$, not Galois $\times$ (not normal). $\mathbb{F}_{p^n}/\mathbb{F}_p$: order $n =$ degree $n$, Galois $\checkmark$ (splitting field of the separable $x^{p^n}-x$: Examples 13, 16, 21).

---

## 9. The Fundamental Theorem of Galois Theory

The main event. For a Galois extension, the internal structure of the extension is a perfect mirror of the internal structure of its group.

### Statement

> **Theorem (Fundamental Theorem of Galois Theory / 伽罗瓦理论基本定理).** Let $E/F$ be a finite Galois extension with $G = \operatorname{Gal}(E/F)$. Then the maps
> $$K \;\longmapsto\; \operatorname{Gal}(E/K) \qquad\text{and}\qquad H \;\longmapsto\; E^H$$
> are mutually inverse, **inclusion-reversing** bijections between
> $$\{\text{intermediate fields } F \subseteq K \subseteq E\} \quad\longleftrightarrow\quad \{\text{subgroups } H \le G\}.$$
> Moreover, under this correspondence:
>
> 1. **(Degrees $\leftrightarrow$ indices)** $[E : K] = |H|$ and $[K : F] = [G : H]$ (the index).
> 2. **(Normality $\leftrightarrow$ normality)** $K/F$ is a normal (equivalently, Galois) extension $\iff$ $H \trianglelefteq G$ is a normal subgroup. In that case
> $$\operatorname{Gal}(K/F) \cong G/H.$$

The two uses of the word "normal" — normal *extension* and normal *subgroup* — turn out to be the same phenomenon viewed from the two sides of the correspondence. (And point 2's isomorphism is a First Isomorphism Theorem in disguise: restriction $\operatorname{Gal}(E/F) \to \operatorname{Gal}(K/F)$, $\sigma \mapsto \sigma|_K$, is a surjective group homomorphism with kernel $\operatorname{Gal}(E/K) = H$ — compare Section 9 of `ring_field.md`.)

> **Inclusion-reversing.** Bigger subfield $\Leftrightarrow$ smaller group: $K_1 \subseteq K_2 \iff \operatorname{Gal}(E/K_1) \supseteq \operatorname{Gal}(E/K_2)$. The whole field $E$ pairs with the trivial subgroup $\{e\}$; the base field $F$ pairs with all of $G$. More constraints to fix, fewer symmetries survive.

### Worked Example: the full lattice for $\mathbb{Q}(\sqrt2, \sqrt3)/\mathbb{Q}$

$G = \{\mathrm{id}, \sigma, \tau, \sigma\tau\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2$, where (Example 20):
$$\sigma:\ \sqrt2 \mapsto -\sqrt2,\ \sqrt3 \mapsto \sqrt3; \qquad \tau:\ \sqrt2 \mapsto \sqrt2,\ \sqrt3 \mapsto -\sqrt3; \qquad \sigma\tau:\ \text{both negated}.$$

$G$ has exactly five subgroups: $\{e\}$, $\langle\sigma\rangle$, $\langle\tau\rangle$, $\langle\sigma\tau\rangle$, $G$. The theorem predicts exactly five intermediate fields:

| Subgroup $H$ | $\|H\|$ | Fixed field $E^H$ | $[E^H : \mathbb{Q}] = [G : H]$ |
|---|:---:|---|:---:|
| $\{e\}$ | 1 | $\mathbb{Q}(\sqrt2, \sqrt3)$ | 4 |
| $\langle\tau\rangle$ | 2 | $\mathbb{Q}(\sqrt2)$ | 2 |
| $\langle\sigma\rangle$ | 2 | $\mathbb{Q}(\sqrt3)$ | 2 |
| $\langle\sigma\tau\rangle$ | 2 | $\mathbb{Q}(\sqrt6)$ | 2 |
| $G$ | 4 | $\mathbb{Q}$ | 1 |

*Verification of the interesting row:* which elements does $\sigma\tau$ fix? $\sigma\tau(\sqrt6) = \sigma\tau(\sqrt2)\,\sigma\tau(\sqrt3) = (-\sqrt2)(-\sqrt3) = \sqrt6$. $\checkmark$ On a general element, $\sigma\tau(a + b\sqrt2 + c\sqrt3 + d\sqrt6) = a - b\sqrt2 - c\sqrt3 + d\sqrt6$, fixed iff $b = c = 0$ — fixed field exactly $\mathbb{Q}(\sqrt6)$. $\checkmark$

The payoff: without the theorem, how would one ever be sure that $\mathbb{Q}(\sqrt2,\sqrt3)$ has *no other* intermediate fields? Enumerating subfields directly is hopeless; enumerating subgroups of a group of order 4 is trivial. **The correspondence converts an infinite-seeming field problem into a finite group computation.** Since every subgroup of the abelian $G$ is normal, all five intermediate fields are Galois over $\mathbb{Q}$ — consistent with each being a splitting field ($x^2-2$, $x^2-3$, $x^2-6$, ...).

### Worked Example: $x^3 - 2$ and a non-abelian group

Let $E = \mathbb{Q}(\sqrt[3]2, \omega)$, the splitting field of $x^3-2$ (Example 11), $[E:\mathbb{Q}] = 6$. An automorphism permutes the three roots $\{\sqrt[3]2,\ \omega\sqrt[3]2,\ \omega^2\sqrt[3]2\}$ and is determined by that permutation; since $|G| = [E:\mathbb{Q}] = 6 = |S_3|$, **every** permutation of the roots occurs:
$$\operatorname{Gal}(E/\mathbb{Q}) \cong S_3,$$
the first non-abelian Galois group we meet. Sample dictionary entries:

- The subgroup $\langle r \rangle \cong \mathbb{Z}_3$ of 3-cycles ($r : \sqrt[3]2 \mapsto \omega\sqrt[3]2,\ \omega \mapsto \omega$) is normal in $S_3$ (index 2), with fixed field $\mathbb{Q}(\omega)$ — and indeed $\mathbb{Q}(\omega)/\mathbb{Q}$ *is* Galois (splitting field of $x^2+x+1$), with group $S_3/\mathbb{Z}_3 \cong \mathbb{Z}_2$. $\checkmark$
- The subgroup $\langle s \rangle \cong \mathbb{Z}_2$ generated by the transposition fixing $\sqrt[3]2$ (i.e. $s = $ complex conjugation restricted to $E$) is **not** normal in $S_3$, and its fixed field $\mathbb{Q}(\sqrt[3]2)$ is **not** normal over $\mathbb{Q}$ — Example 19's defective extension reappears, now *explained*: its failure of normality as an extension is the failure of normality of a subgroup of $S_3$. $\checkmark$

### Why this matters: solvability by radicals

Galois theory was invented to answer: *why is there no quintic formula?* The correspondence reduces "$f$ is solvable by radicals" (its roots are expressible via $+,-,\times,\div,\sqrt[n]{\ }$) to a group-theoretic property — the Galois group of $f$ must be a **solvable group** (可解群: built from abelian pieces by successive normal subgroups, mirroring a tower of radical extensions $F \subset F(\sqrt[n_1]{a_1}) \subset \cdots$). For degree $\le 4$, the Galois groups embed in $S_4$, which is solvable — hence the classical quadratic, cubic, and quartic formulas. But a "generic" quintic has Galois group $S_5$, which is **not** solvable (its only nontrivial normal subgroup $A_5$ is simple and non-abelian). Hence:

> **Theorem (Abel–Ruffini, via Galois).** There is no formula in radicals for the roots of a general degree-5 polynomial. Concretely, $x^5 - 6x + 3 \in \mathbb{Q}[x]$ has Galois group $S_5$ and its roots cannot be written in radicals.

The same machinery settles the ancient compass-and-straightedge problems: every constructible number lies in a tower of degree-2 extensions, so its degree over $\mathbb{Q}$ is a power of 2 (Tower Law). Doubling the cube needs $\sqrt[3]2$ of degree 3 — not a power of 2 — impossible. Trisecting $60°$ needs a root of the irreducible cubic $8x^3-6x-1$ — impossible. Millennia-old geometry problems, closed by a divisibility argument on field degrees.

---

## 10. Summary

### The main dictionary

| Field side | Group side |
|---|---|
| Galois extension $E/F$ | Galois group $G = \operatorname{Gal}(E/F)$ |
| Intermediate field $K$ | Subgroup $H = \operatorname{Gal}(E/K)$ |
| $[E:K]$ | $\|H\|$ |
| $[K:F]$ | index $[G:H]$ |
| $K/F$ normal (Galois) | $H \trianglelefteq G$ normal |
| $\operatorname{Gal}(K/F)$ | quotient $G/H$ |
| larger field | smaller subgroup (inclusion-reversing) |
| $f$ solvable by radicals | $\operatorname{Gal}$ of splitting field is a solvable group |

### Hierarchy of extension properties

$$\text{Galois} \;=\; \text{normal} + \text{separable} \;\implies\; \text{finite} \;\implies\; \text{algebraic}$$

| Property | Definition | Detects / guarantees | Can fail |
|---|---|---|---|
| Finite | $[E:F] < \infty$ | forces algebraic; Tower Law applies | $\mathbb{R}/\mathbb{Q}$, $\overline{\mathbb{Q}}/\mathbb{Q}$ |
| Algebraic | every element satisfies a polynomial | closure under $+,\times$; transitive in towers | $\mathbb{Q}(\pi)/\mathbb{Q}$ |
| Normal | one root in $\Rightarrow$ all roots in | $=$ being a splitting field | $\mathbb{Q}(\sqrt[3]2)/\mathbb{Q}$ |
| Separable | minimal polynomials have distinct roots | automatic in char $0$ and over finite fields | $\mathbb{F}_p(t)(\sqrt[p]{t})/\mathbb{F}_p(t)$ |
| Galois | fixed field of $\operatorname{Gal}$ is exactly $F$ | $\|\operatorname{Gal}\| = [E:F]$; the full correspondence | whenever normality or separability fails |

### The through-line from `ring_field.md`

Every construction here rests on the quotient machinery of the previous chapter: irreducible polynomial $\to$ maximal ideal $\to$ field quotient $k[x]/\langle f\rangle$ (Sections 13–14 there) builds the extensions; the First Isomorphism Theorem (for rings there, for groups here in the Fundamental Theorem) organizes their maps; and the ideal-theoretic dictionary "properties of $I$ $\leftrightarrow$ properties of $R/I$" finds its ultimate refinement in the Galois dictionary "subfields of $E$ $\leftrightarrow$ subgroups of $G$."
