**1. 设F是一个域，令 
        $$ S=\{aE_{11} | a \in F\} $$
证明： $S$是 $M_n(F)$的一个子环，并求单位元。**

 $E_{11}$ denotes a matrix unit — specifically, the matrix with a $1$ in the $(1,1)$ position and $0$ s everywhere else.

 

证：

**第一步：证明 $S$ 是 $M_n(F)$ 的子环。**

由子环判定定理，只需证明 $S$ 非空，且对减法和乘法封闭。

(1) 非空：取 $a=0$，则 $0\cdot E_{11}=0\in S$，故 $S\neq\varnothing$。

(2) 对减法封闭：任取 $aE_{11},\,bE_{11}\in S$（$a,b\in F$），有
$$aE_{11}-bE_{11}=(a-b)E_{11}.$$
因为 $F$ 是域，$a-b\in F$，所以 $(a-b)E_{11}\in S$。

(3) 对乘法封闭：由矩阵单位的乘法规则 $E_{ij}E_{kl}=\delta_{jk}E_{il}$，得
$$E_{11}E_{11}=E_{11}.$$
于是
$$(aE_{11})(bE_{11})=ab\,(E_{11}E_{11})=ab\,E_{11}.$$
因为 $F$ 是域，$ab\in F$，所以 $ab\,E_{11}\in S$。

综上，$S$ 对减法和乘法都封闭，且非空，故 $S$ 是 $M_n(F)$ 的子环。

**第二步：求 $S$ 的单位元。**

因为 $F$ 是域，故 $1\in F$，从而 $E_{11}=1\cdot E_{11}\in S$。

对任意 $aE_{11}\in S$，由 $E_{11}E_{11}=E_{11}$ 可得
$$E_{11}\cdot(aE_{11})=a(E_{11}E_{11})=aE_{11},$$
$$(aE_{11})\cdot E_{11}=a(E_{11}E_{11})=aE_{11}.$$

所以 $E_{11}$ 是 $S$ 中关于乘法的单位元，即 $S$ 的单位元为 $E_{11}$。

**注：** 当 $n\geq 2$ 时，$E_{11}\neq I_n$，即 $S$ 的单位元 $E_{11}$ 与 $M_n(F)$ 的单位元 $I_n$ 不同。这说明子环的单位元未必与母环的单位元相同（$S$ 是没有单位元 $I_n$ 的子环，但作为独立的环，它自身有单位元 $E_{11}$）。

$\blacksquare$


**2. 设R是有单位元的环，证明：R的每一个非平凡理想都不可能有此单位元。**

证：

设 $1$ 是 $R$ 的单位元，$I$ 是 $R$ 的一个非平凡理想（即 $I\neq R$）。要证 $1\notin I$（从而 $I$ 不含 $R$ 的单位元）。

用反证法。假设 $1\in I$。

因为 $I$ 是 $R$ 的理想，所以对任意 $r\in R$，都有
$$r=r\cdot 1\in R\cdot I\subseteq I.$$

于是对每个 $r\in R$ 都有 $r\in I$，即 $R\subseteq I$。又因为 $I\subseteq R$（$I$ 是 $R$ 的子集），所以
$$I=R.$$

这与 $I$ 是非平凡理想（$I\neq R$）矛盾。

故假设不成立，即 $1\notin I$。因此 $R$ 的每一个非平凡理想都不含 $R$ 的单位元 $1$，也就不可能以 $1$ 作为其单位元。

$\blacksquare$

**注：** 这里的关键是理想的"吸收性"：$R\cdot I\subseteq I$ 且 $I\cdot R\subseteq I$。正是这一点使得只要 $1\in I$，就能把 $R$ 中的每个元素"吸收"进 $I$ 中，从而迫使 $I=R$。这与第1题形成对比：第1题中的 $S$ 只是子环而非理想，所以它可以拥有一个与 $M_n(F)$ 的单位元 $I_n$ 不同的单位元 $E_{11}$；而理想因为具备吸收性，一旦是非平凡的（$\neq R$），就绝不可能包含 $R$ 的单位元。
If the statment is asking: that $I$ (as a ring in its own right) has no unity at all — not even one different from $1$, the way $S={aE_{11}}$ in problem 1 had its own unity $E_{11}\neq I_n$. That's a stronger claim, and it needs more work — and actually isn't true for a general ring.

Counterexample showing the stronger claim needs an extra hypothesis:
Let $R=\mathbb{Z}\times\mathbb{Z}$ (unity $(1,1)$), and $I=\mathbb{Z}\times{0}$, a proper ideal. Then $e=(1,0)\in I$ satisfies $e\cdot x=x$ for every $x=(a,0)\in I$, so $e$ is a unity of $I$ — just not the unity of $R$. The proof I gave doesn't rule this out, and indeed it can't, because it's false here.

The mechanism: $e=(1,0)$ is a nontrivial idempotent ($e^2=e$, $e\neq0,1$). Whenever $R$ has such an idempotent, it decomposes as $R\cong eR\times(1-e)R$, and $eR$ is a proper ideal with its own unity $e$. This is only possible because $R=\mathbb{Z}\times\mathbb{Z}$ has zero divisors: $e(e-1)=(1,0)(0,-1)=(0,0)$ with $e\neq0,1$.

So the stronger statement is true only with an extra hypothesis — e.g. $R$ has no zero divisors:

Suppose $I$ is a nonzero proper ideal with unity $e\in I$. Then $e^2=e$, so $e(e-1)=0$. If $R$ has no zero divisors, this forces $e=0$ or $e=1$.
- $e=0 \Rightarrow$ for all $x\in I$, $x=e\cdot x=0$, so $I={0}$ — excluded since $I$ is nontrivial (nonzero).
- $e=1 \Rightarrow 1\in I \Rightarrow I=R$ (by the absorption argument) — contradicts $I\neq R$.

Either way, contradiction — so under "no zero divisors," $I$ has no unity whatsoever.


**3. 证明：域F没有非平凡的理想。**

证：

设 $I$ 是域 $F$ 的一个理想。要证：$I=\{0\}$ 或 $I=F$（即 $F$ 不存在既非零又非 $F$ 本身的理想）。

只需证明：若 $I\neq\{0\}$，则 $I=F$。

设 $I\neq\{0\}$，则存在 $a\in I$ 且 $a\neq 0$。

因为 $F$ 是域，$a\neq 0$，所以 $a$ 在 $F$ 中有逆元 $a^{-1}\in F$。

因为 $I$ 是 $F$ 的理想，故对任意 $r\in F$ 都有 $rI\subseteq I$；取 $r=a^{-1}$，得
$$a^{-1}\cdot a\in I,$$
即
$$1=a^{-1}a\in I.$$

于是对任意 $r\in F$，由理想的吸收性，
$$r=r\cdot 1\in F\cdot I\subseteq I.$$

所以 $F\subseteq I$。又 $I\subseteq F$，故
$$I=F.$$

综上，$F$ 的理想只有 $\{0\}$ 和 $F$ 本身，即域 $F$ 没有非平凡（既非零又非 $F$）的理想。

$\blacksquare$

**注（与第2题的联系）：** 第2题说明"非平凡理想不含单位元 $1$"；本题反过来说明，在域中"只要理想非零就必含 $1$"——因为域中每个非零元都可逆。两者结合：域中一个理想如果非零，就含 $1$，从而（由吸收性）等于 $F$；因此域中不存在非零的非平凡理想，非平凡理想只能是 $\{0\}$——但 $\{0\}$ 本身通常不算"非平凡"，所以域的理想只有 $\{0\}$ 与 $F$ 这两个"平凡"选项，不存在真正意义上的非平凡理想。

**4. R是一个有单位元 $1(\neq 0)$的交换环，证明如果R没有非平凡的理想，那么R是一个域。**

证：

要证 $R$ 是域，即证：$R$ 是有单位元 $1\neq 0$ 的交换环（已知），且 $R$ 中每个非零元都有逆元。

任取 $a\in R$，$a\neq 0$。考虑由 $a$ 生成的主理想
$$Ra=\{ra\mid r\in R\}.$$

（因 $R$ 交换，$Ra$ 是 $R$ 的理想：对任意 $r_1a,\,r_2a\in Ra$，$r_1a-r_2a=(r_1-r_2)a\in Ra$；对任意 $s\in R$，$s(ra)=(sr)a\in Ra$。）

因为 $a=1\cdot a\in Ra$ 且 $a\neq 0$，所以 $Ra\neq\{0\}$。

因为 $R$ 没有非平凡理想，$R$ 的理想只能是 $\{0\}$ 或 $R$。由 $Ra\neq\{0\}$，故
$$Ra=R.$$

于是 $1\in R=Ra$，即存在 $b\in R$，使得
$$ba=1.$$

又因为 $R$ 是交换环，故 $ab=ba=1$。所以 $b$ 是 $a$ 的逆元，即 $a$ 在 $R$ 中可逆。

因为 $a$ 是任意非零元，所以 $R$ 中每个非零元都可逆。又 $R$ 是有单位元 $1\neq 0$ 的交换环，故 $R$ 是一个域。

$\blacksquare$

**注：** 本题是第3题的逆命题。第3题："域 $\Rightarrow$ 无非平凡理想"；本题："（交换、有 $1\neq0$ 的环）无非平凡理想 $\Rightarrow$ 域"。两者合起来说明：对于有单位元 $1\neq 0$ 的交换环 $R$，
$$R\text{ 是域} \iff R\text{ 没有非平凡理想}.$$
证明的核心技巧一致：都是利用"理想一旦含非零元、含可逆元或含 $1$，就吸收整个环"这一事实（即第2题揭示的吸收性）来回收利用。

**5. 证明：若 $\sigma$是环$R$到$\tilde R$的一个环同构，且$R$有单位元1， 则 $\sigma(1)$是$\tilde R$的单位元。从而$\sigma$是$R$到$\tilde R$的双射，且$\sigma$是$R$到$\tilde R$的环同态。**

证：

因为 $\sigma$ 是环同构，按定义 $\sigma$ 同时具备两条性质，它们正是下面证明中要用到的：

(i) $\sigma$ 是环同态：对任意 $x,y\in R$，$\sigma(xy)=\sigma(x)\sigma(y)$；

(ii) $\sigma$ 是双射，特别地是满射：对任意 $\tilde y\in\tilde R$，存在 $x\in R$，使得 $\sigma(x)=\tilde y$。

下面证明 $\sigma(1)$ 是 $\tilde R$ 的单位元，即证：对任意 $\tilde y\in\tilde R$，都有
$$\sigma(1)\cdot\tilde y=\tilde y\cdot\sigma(1)=\tilde y.$$

任取 $\tilde y\in\tilde R$。由 (ii)，存在 $x\in R$ 使得 $\sigma(x)=\tilde y$。

利用 (i) 及 $1$ 是 $R$ 的单位元（$1\cdot x=x\cdot1=x$），得
$$\sigma(1)\cdot\tilde y=\sigma(1)\cdot\sigma(x)=\sigma(1\cdot x)=\sigma(x)=\tilde y,$$
$$\tilde y\cdot\sigma(1)=\sigma(x)\cdot\sigma(1)=\sigma(x\cdot1)=\sigma(x)=\tilde y.$$

因为 $\tilde y$ 是 $\tilde R$ 中任意元素，所以 $\sigma(1)$ 对 $\tilde R$ 中每个元素都满足单位元的定义，即 $\sigma(1)$ 是 $\tilde R$ 的单位元。

$\blacksquare$

**注：** 证明中两处假设缺一不可：
- 若只用 (i)（$\sigma$ 是同态）而没有 (ii)（满射），只能得到 $\sigma(1)$ 是 $\sigma(R)$（$\sigma$ 的像）的单位元，而不一定是整个 $\tilde R$ 的单位元。例如嵌入同态 $\sigma:\mathbb{Z}\to\mathbb{Z}\times\mathbb{Z}$，$\sigma(n)=(n,0)$ 是单同态但非满射，$\sigma(1)=(1,0)$ 只是子环 $\mathbb{Z}\times\{0\}$（第2题中出现过的例子）的单位元，而不是 $\mathbb{Z}\times\mathbb{Z}$ 的单位元 $(1,1)$。
- 所以"满同态 + 定义域有单位元"只能保证像中有一个"局部单位元"；而"同构"（同态 + 双射）才能保证 $\sigma(1)$ 是整个陪域 $\tilde R$ 的单位元——这正是本题结论成立的关键所在。

