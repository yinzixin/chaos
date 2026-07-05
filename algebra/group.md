# Groups — Prior Knowledge

This note collects the definitions of semigroup, group, and abelian group. These structures are prerequisites for the study of rings and fields, where they appear as the additive and multiplicative components of a ring.

---

## 1. Binary Operations

A **binary operation** on a set $S$ is a function $* : S \times S \to S$. The key requirement is **closure**: the result of combining any two elements of $S$ must again lie in $S$.

---

## 2. Semigroup

### Definition

A **semigroup** is a pair $(S, *)$ where $S$ is a non-empty set and $*$ is a binary operation on $S$ satisfying:

1. **(Associativity)** For all $a, b, c \in S$, $(a * b) * c = a * (b * c)$.

That's the only requirement — no identity, no inverses.

### Examples

- $(\mathbb{Z}^+, +)$: positive integers under addition. There is no identity ($0 \notin \mathbb{Z}^+$), but addition is associative.
- $(M_n(\mathbb{R}), \cdot)$: $n \times n$ matrices under multiplication. Associative, but no inverse exists for singular matrices.
- $(\mathbb{Z}, \max)$: integers under the operation $a * b = \max(a, b)$. Associative, but no identity.

---

## 3. Group

### Definition

A **group** is a pair $(G, *)$ where $G$ is a non-empty set and $*$ is a binary operation on $G$ satisfying:

1. **(Associativity)** For all $a, b, c \in G$, $(a * b) * c = a * (b * c)$.
2. **(Identity)** There exists an element $e \in G$ such that $a * e = e * a = a$ for all $a \in G$.
3. **(Inverses)** For each $a \in G$, there exists $a^{-1} \in G$ such that $a * a^{-1} = a^{-1} * a = e$.

A group is thus a semigroup with an identity and inverses.

> **Note:** The identity element $e$ is unique, and the inverse $a^{-1}$ of each element is unique. Both facts follow from the axioms alone.

### Examples

- $(\mathbb{Z}, +)$: integers under addition. Identity is $0$, inverse of $n$ is $-n$.
- $(\mathbb{Q} \setminus \{0\}, \cdot)$: non-zero rationals under multiplication. Identity is $1$, inverse of $q$ is $1/q$.
- $(S_n, \circ)$: the **symmetric group** of all permutations of $\{1, \ldots, n\}$ under composition. Non-abelian for $n \geq 3$.
- $(\mathbb{Z}_n, +)$: integers modulo $n$ under addition mod $n$. Identity is $0$, inverse of $k$ is $n - k$.

### Non-example

$(\mathbb{Z}, \cdot)$ is **not** a group: $2$ has no multiplicative inverse in $\mathbb{Z}$ since $1/2 \notin \mathbb{Z}$.

---

## 4. Abelian Group

### Definition

A group $(G, *)$ is called **abelian** (or **commutative**) if it additionally satisfies:

4. **(Commutativity)** For all $a, b \in G$, $a * b = b * a$.

### Examples

- $(\mathbb{Z}, +)$, $(\mathbb{Q}, +)$, $(\mathbb{R}, +)$, $(\mathbb{C}, +)$ are all abelian groups.
- $(\mathbb{R} \setminus \{0\}, \cdot)$ is abelian.
- $(S_n, \circ)$ for $n \geq 3$ is a group but **not** abelian — for example, in $S_3$, swapping elements 1↔2 then 2↔3 gives a different result than doing them in the opposite order.

---

## 5. Relationship Between the Structures

$$\text{Semigroup} \xrightarrow{+\,\text{identity}} \text{Monoid} \xrightarrow{+\,\text{inverses}} \text{Group} \xrightarrow{+\,\text{commutativity}} \text{Abelian Group}$$

> A **monoid** is a semigroup with an identity element. It sits between semigroup and group in the hierarchy, though we will not need it further in this chapter.

---

## 6. Connection to Rings

A **ring** $(R, +, \cdot)$ is built from two of these structures layered on the same set:

| Component | Structure |
|---|---|
| $(R, +)$ | Abelian group |
| $(R, \cdot)$ | Semigroup |

The distributive laws then tie the two operations together. This is why the theory of groups is the natural starting point before studying rings — every ring contains an abelian group inside it.

See [ring_field.md](ring_field.md) for the full definition and theory of rings.
