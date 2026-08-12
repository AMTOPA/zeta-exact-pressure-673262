# Exact pressure multiplicity refinement

## Statement

Write

```math
S=N_0^s(T,2T),\qquad N=N(T,2T).
```

Assume the imported interface

```math
S\ge H_{\mathrm{cert}}N+\mathrm{tr}\,\Psi(M)-o(N),
```

with

```math
H_{\mathrm{cert}}
=\frac{672457041414544284}{10^{18}},
```

together with the certified seven-point inequality of
[`sxuff/zeta-positioned-pressure`](https://github.com/sxuff/zeta-positioned-pressure),
with

```math
\varepsilon=\frac{51063}{10^7},\qquad
b_r\ge 0,\qquad
B:=\sum_{r=1}^6 b_r=\frac{3}{1150}.
```

Assume also the imported finite-dimensional block estimate

```math
\mathrm{tr}\,\Psi(G)\ge h_m(E),
```

where

```math
h_m(E)=
\begin{cases}
E, & 0\le E\le \dfrac{m}{m-1}, \\
\dfrac{E}{m}+2\sqrt{\dfrac{m-1}{m}E}-1,
& E\ge \dfrac{m}{m-1}.
\end{cases}
```

Under these imported inputs, the refinement below gives

```math
\liminf_{T\to\infty}\frac{S}{N}
\ge 0.673262375584978050386\ldots.
```

---

## 1. Exact local pressure inside an m-point block

Consider $m$ consecutive simple zeros with normalized gaps
$g_1,\ldots,g_{m-1}$.

For each seven-point window starting at
$t\in\{0,\ldots,m-7\}$, the local pressure is

```math
\sum_{r=1}^{6} b_r g_{t+r}.
```

After summing all $m-6$ local inequalities, define

```math
c_j
=
\sum_{\substack{0\le t\le m-7\\1\le j-t\le 6}}
b_{j-t},
\qquad
P_B=\sum_{j=1}^{m-1}c_jg_j.
```

The pair terms are dominated by the block off-diagonal energy exactly as in
the predecessor, hence

```math
E_B+P_B\ge A_m,
\qquad
A_m:=\varepsilon(m-6).
\tag{1}
```

The coefficients $c_j$ satisfy the exact identity

```math
\begin{aligned}
\sum_{j=1}^{m-1}c_j
&=
\sum_{j=1}^{m-1}
\sum_{\substack{0\le t\le m-7\\1\le j-t\le6}}
b_{j-t} \\
&=
\sum_{t=0}^{m-7}\sum_{r=1}^{6}b_r \\
&=(m-6)B.
\end{aligned}
\tag{2}
```

Equation (2) is an exact double-counting identity; no estimate is used.

---

## 2. Retaining the exact pressure through the block defect

Set

```math
R_m=h_m(A_m),
\qquad
\eta_m=\frac{R_m}{A_m}.
```

Because $h_m$ is increasing and concave with $h_m(0)=0$, for
$0\le E\le A_m$ we have

```math
h_m(E)\ge \eta_m E.
\tag{3}
```

If $E_B\ge A_m$, monotonicity gives

```math
\mathrm{tr}\,\Psi(G_B)\ge R_m-o(1).
```

If $E_B<A_m$, equation (1) gives
$P_B\ge A_m-E_B$. Therefore

```math
\begin{aligned}
\mathrm{tr}\,\Psi(G_B)+\eta_mP_B
&\ge
\eta_mE_B+\eta_m(A_m-E_B)-o(1) \\
&=R_m-o(1).
\end{aligned}
```

Thus in all cases

```math
\mathrm{tr}\,\Psi(G_B)+\eta_mP_B
\ge R_m-o(1).
\tag{4}
```

The important point is that we do **not** replace $P_B$ at this stage by the
coarser quantity $B\,\mathrm{span}(B)$.

---

## 3. Shifted-block averaging with exact multiplicity

Partition the ordered simple zeros into disjoint blocks of $m$ consecutive
points. There are $m$ residue-class shifts of this partition, apart from
$O(m)$ endpoint effects.

Fix one global gap. As the partition shift runs through all $m$ possibilities:

1. the gap is a block boundary exactly once;
2. it occupies each internal position $j=1,\ldots,m-1$ exactly once.

Therefore its total pressure coefficient over all shifted partitions is

```math
\sum_{j=1}^{m-1}c_j=(m-6)B.
\tag{5}
```

Averaging equation (4) over the shifted partitions, using spectral pinching
for the block defects and the imported normalized total-gap relation, gives

```math
\mathrm{tr}\,\Psi(M)
\ge
\frac{R_m}{m}S
-\eta_m B\frac{m-6}{m}N
-o(N).
\tag{6}
```

For comparison, the predecessor first applies $c_j\le B$. That coarse step
leads to the larger pressure penalty $B(m-1)/m$.

---

## 4. Assembly

Insert equation (6) into the analytic interface:

```math
S
\ge
H_{\mathrm{cert}}N
+\frac{R_m}{m}S
-\eta_m B\frac{m-6}{m}N
-o(N).
```

Rearranging gives

```math
\frac{S}{N}
\ge
\frac{mH_{\mathrm{cert}}-\eta_mB(m-6)}{m-R_m}
-o(1).
\tag{7}
```

Since $A_m=\varepsilon(m-6)$,

```math
\eta_mB(m-6)=\frac{R_mB}{\varepsilon}.
```

Hence equation (7) is equivalent to

```math
\frac{S}{N}
\ge
\frac{mH_{\mathrm{cert}}-R_mB/\varepsilon}{m-R_m}
-o(1).
\tag{8}
```

---

## 5. Numerical specialization

The integer scan in [`src/check_final_bound.py`](src/check_final_bound.py)
selects

```math
m=215.
```

Then

```math
A_{215}
=
\frac{51063}{10^7}\cdot209
=
1.0672167,
```

and

```math
R_{215}
=
1.06627687661618780546392584286702014367\ldots.
```

Equation (7) gives

```math
\frac{S}{N}
\ge
0.67326237558497805038619164619309578448\ldots-o(1).
```

Consequently, subject to the imported inputs,

```math
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
>
\frac{6732623755}{10^{10}}
}.
```

Equivalently, the safe published percentage is

```math
\boxed{67.32623755\%}.
```

---

## 6. What is new, and what is imported

### New in this repository

The new ingredient is precisely the retention of the exact pressure
multiplicities through shifted-block averaging, especially equations (2) and
(5). The final high-precision arithmetic is also checked independently by the
included scripts and GitHub Actions.

### Imported from the preceding lineage

The following are **not** reproved here:

- the analytic interface involving $H_{\mathrm{cert}}$ and
  $\mathrm{tr}\,\Psi(M)$;
- the seven-point interval certificate $F\ge 51063/10^7$;
- the finite-dimensional profile $h_m$;
- the spectral pinching and normalized total-gap relation used in the block
  average.

See [`THIRD_PARTY.md`](THIRD_PARTY.md) and
[`docs/lineage.md`](docs/lineage.md) for the dependency chain.

> **Research status.** This is a research draft. The exact-multiplicity step
> should receive independent mathematical review before the resulting constant
> is cited as an established theorem.
