# Exact pressure multiplicity refinement

## Statement

Write

$$
S=N_0^s(T,2T),
\qquad
N=N(T,2T).
$$

Assume the imported interface

$$
S\ge H_{\mathrm{cert}}N+\mathop{\mathrm{tr}}\Psi(M)-o(N),
$$

with

$$
H_{\mathrm{cert}}
=\frac{672457041414544284}{10^{18}},
$$

together with the certified seven-point inequality of
[`sxuff/zeta-positioned-pressure`](https://github.com/sxuff/zeta-positioned-pressure)
having

$$
\varepsilon=\frac{51063}{10^7},
\qquad
b_r\ge0,
\qquad
B:=\sum_{r=1}^6 b_r=\frac3{1150}.
$$

Assume also the imported finite-dimensional block estimate

$$
\mathop{\mathrm{tr}}\Psi(G)\ge h_m(E),
$$

where

$$
h_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\cr
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

Under these imported inputs, the refinement below gives

$$
\liminf_{T\to\infty}\frac SN
\ge 0.673262375584978050386\ldots.
$$

## 1. Exact local pressure inside an m-block

Consider $m$ consecutive simple zeros and their normalized gaps
$g_1,\ldots,g_{m-1}$.

For each seven-point window starting at
$t\in\{0,\ldots,m-7\}$, the local pressure is

$$
\sum_{r=1}^6 b_r g_{t+r}.
$$

After summing all $m-6$ local inequalities, define

$$
c_j
=
\sum_{\substack{0\le t\le m-7,\ 1\le j-t\le6}}
b_{j-t},
\qquad
P_B=\sum_{j=1}^{m-1}c_jg_j.
$$

The pair terms are dominated by the block off-diagonal energy exactly as in
the predecessor, hence

$$
E_B+P_B\ge A_m,
\qquad
A_m:=\varepsilon(m-6).
\tag{1}
$$

The coefficients $c_j$ satisfy the exact identity

$$
\begin{aligned}
\sum_{j=1}^{m-1}c_j
&=
\sum_{j=1}^{m-1}
\sum_{\substack{0\le t\le m-7,\ 1\le j-t\le6}}
b_{j-t} \cr
&=
\sum_{t=0}^{m-7}\sum_{r=1}^6b_r \cr
&=(m-6)B.
\end{aligned}
\tag{2}
$$

No estimate is used in (2).

## 2. Retaining the exact pressure through the block defect

Set

$$
R_m=h_m(A_m),
\qquad
\eta_m=\frac{R_m}{A_m}.
$$

Because $h_m$ is increasing and concave with $h_m(0)=0$, for
$0\le E\le A_m$,

$$
h_m(E)\ge \eta_m E.
\tag{3}
$$

If $E_B\ge A_m$, monotonicity gives

$$
\mathop{\mathrm{tr}}\Psi(G_B)\ge R_m-o(1).
$$

If $E_B<A_m$, equation (1) gives
$P_B\ge A_m-E_B$, hence

$$
\begin{aligned}
\mathop{\mathrm{tr}}\Psi(G_B)+\eta_mP_B
&\ge
\eta_mE_B+\eta_m(A_m-E_B)-o(1) \cr
&=R_m-o(1).
\end{aligned}
$$

Thus in all cases

$$
\mathop{\mathrm{tr}}\Psi(G_B)+\eta_mP_B
\ge R_m-o(1).
\tag{4}
$$

This is the point at which we deliberately do **not** replace $P_B$ by
$B\,\mathrm{span}(B)$.

## 3. Shifted-block averaging with exact multiplicity

Partition the ordered simple zeros into disjoint blocks of $m$ consecutive
points. There are $m$ residue-class shifts of this partition, up to $O(m)$
endpoint points.

For a fixed global gap, as the shift runs through the $m$ possibilities,

- once the gap is a block boundary;
- once it occupies each internal position $j=1,\ldots,m-1$.

Therefore the total pressure coefficient assigned to that gap over all
shifts is exactly

$$
\sum_{j=1}^{m-1}c_j=(m-6)B.
\tag{5}
$$

Averaging (4) over the shifted partitions, using spectral pinching for the
block defects and the imported normalized total-gap relation, gives

$$
\mathop{\mathrm{tr}}\Psi(M)
\ge
\frac{R_m}{m}S
-\eta_m B\frac{m-6}{m}N
-o(N).
\tag{6}
$$

The predecessor's coarse replacement $c_j\le B$ instead produces the larger
penalty $B(m-1)/m$.

## 4. Assembly

Insert (6) into the analytic interface:

$$
S
\ge
H_{\mathrm{cert}}N
+\frac{R_m}{m}S
-\eta_m B\frac{m-6}{m}N
-o(N).
$$

After rearranging,

$$
\frac SN
\ge
\frac{mH_{\mathrm{cert}}-\eta_mB(m-6)}{m-R_m}
-o(1).
\tag{7}
$$

Since $A_m=\varepsilon(m-6)$,

$$
\eta_mB(m-6)=\frac{R_mB}{\varepsilon},
$$

so equivalently

$$
\frac SN
\ge
\frac{mH_{\mathrm{cert}}-R_mB/\varepsilon}{m-R_m}
-o(1).
\tag{8}
$$

## 5. Numerical specialization

The integer scan in `src/check_final_bound.py` selects

$$
m=215.
$$

Then

$$
A_{215}
=
\frac{51063}{10^7}\cdot209
=
1.0672167,
$$

and

$$
R_{215}
=
1.06627687661618780546392584286702014367\ldots.
$$

Formula (7) gives

$$
\frac SN
\ge
0.67326237558497805038619164619309578448\ldots-o(1).
$$

Hence, subject to the imported inputs,

$$
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\gt
\frac{6732623755}{10^{10}}
}.
$$

## 6. Audit note

The novel step is equations (2) and (5): exact pressure multiplicities are
retained until the average over all shifted block partitions. Everything else
is an imported inequality or final arithmetic.

This draft should receive independent mathematical review before being cited
as an established theorem.
