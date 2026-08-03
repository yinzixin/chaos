This is a one-line consequence of what the ideal notation means.

The key fact. For any commutative ring $R$ and element $a \in R$, the principal ideal is

$$\langle a \rangle = { r a : r \in R } = \text{all multiples of } a.$$

In particular $a$ itself belongs to $\langle a\rangle$ (take $r = 1$).

The argument. Suppose $\langle f \rangle = \langle g \rangle$. Then

$$g ;\in; \langle g \rangle ;=; \langle f \rangle.$$

Being an element of $\langle f\rangle$ means $g$ is a multiple of $f$ — i.e. $g = qf$ for some $q \in k[x]$. That is exactly the statement $f \mid g$. $\square$

Why it matters here. Notice the reasoning is symmetric: the same step run the other way ($f \in \langle f\rangle = \langle g\rangle$) gives $g \mid f$. So $\langle f\rangle = \langle g\rangle$ actually forces $f \mid g$ and $g \mid f$ — the two polynomials are associates (they differ by a unit, i.e. a nonzero constant in $k[x]$).

That's precisely why the line at ring_field.md:841 is useful in the proof. The author has $\langle f \rangle \subseteq \langle g\rangle$ from $f = gh$, and wants to rule out equality. If equality held, then $f \mid g$ would give $\deg f \le \deg g$. But $f = gh$ with $\deg h \ge 1$ means $\deg g = \deg f - \deg h < \deg f$ — a contradiction. Hence the inclusion is strict, $\langle f\rangle \subsetneq \langle g\rangle$, which is what breaks maximality.

(One caveat worth keeping in mind: the clean "$\langle f\rangle=\langle g\rangle \iff$ associates" statement relies on $k[x]$ being an integral domain, which it is since $k$ is a field. In a general ring with zero divisors, equal principal ideals need not force associativity — but the direction used here, $\langle f\rangle=\langle g\rangle \Rightarrow f\mid g$, holds in any commutative ring, since it only uses $g \in \langle g\rangle$.)