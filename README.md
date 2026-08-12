# A 67.3262375585% lower bound for simple zeros of the Riemann zeta function

This repository records a short refinement of the block-averaging deduction in
[`sxuff/zeta-positioned-pressure`](https://github.com/sxuff/zeta-positioned-pressure).

Subject to the same imported analytic interface and the same certified
seven-point inequality used there, the refinement gives

$$
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge 0.6732623755849780503\ldots
\gt \frac{6732623755}{10^{10}}.
$$

That is **67.3262375585%**.

> [!IMPORTANT]
> This is a same-day research draft, not a peer-reviewed theorem and not a
> proof of the Riemann hypothesis. The new contribution here is a finite
> combinatorial averaging identity. The analytic interface and the seven-point
> interval certificate are imported from prior work and are not reverified in
> this repository.

**Formal manuscript:** [PDF](paper/main.pdf) · [LaTeX source](paper/main.tex) · [Proof notes](proof.md)

[Lineage](docs/lineage.md) · [Exact parameters](candidate.json) · [Checks](src/)

## Where this sits

| Source | Reported lower bound |
| --- | ---: |
| Anthropic / Claude, Theorem D | 67.2500703679% |
| `ainta/zeta-simple-zeros` | 67.3008527927% |
| `trmdy/zeta-simple-zeros-673137` | 67.3137630699% |
| `sxuff/zeta-positioned-pressure` | 67.3205978423% |
| **this repository** | **67.3262375585%** |

The comparison is only meaningful under the same imported analytic interface.

## The new idea

Let a local seven-point certificate use six nonnegative gap-pressure
coefficients $b_1,\ldots,b_6$, with total

$$
B=\sum_{r=1}^6 b_r=\frac{3}{1150}.
$$

For an $m$-point block, summing the local certificate over all $m-6$
seven-point windows gives an exact pressure term

$$
P_B=\sum_{j=1}^{m-1} c_j g_j,
$$

where $c_j$ is the sum of the local pressure coefficients of all windows
containing the $j$-th block gap. Double counting gives the exact identity

$$
\sum_{j=1}^{m-1} c_j=(m-6)B.
$$

The predecessor replaces every $c_j$ by the uniform upper bound $B$, which
later costs $B(m-1)$ over the shifted block partitions. If the exact $c_j$'s
are retained until the shifted-partition average, each global gap occupies
every internal block position exactly once, so its total charge over all $m$
shifts is instead

$$
(m-6)B.
$$

No new local interval search is needed.

## Final formula

Using the predecessor's certified values

$$
H_{\mathrm{cert}}=\frac{672457041414544284}{10^{18}},
\qquad
\varepsilon=\frac{51063}{10^7},
\qquad
B=\frac3{1150},
$$

put

$$
A_m=\varepsilon(m-6),
\qquad
R_m=h_m(A_m),
\qquad
\eta_m=\frac{R_m}{A_m},
$$

where the imported sharp block profile is

$$
h_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\cr
E/m+2\sqrt{(m-1)E/m}-1,&E\ge m/(m-1).
\end{cases}
$$

The exact-pressure average gives

$$
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{mH_{\mathrm{cert}}-\eta_m B(m-6)}{m-R_m}
-o(1).
$$

Scanning integer block lengths selects $m=215$, yielding

$$
0.673262375584978050386\ldots.
$$

## Reproduction

Requires Python 3.10+ and `mpmath>=1.3.0`.

```bash
python3 src/check_multiplicity.py
python3 src/check_final_bound.py
```

Or run both:

```bash
sh run.sh
```

`check_multiplicity.py` verifies the exact pressure-position count using the
rational pressure coefficients published by the predecessor.
`check_final_bound.py` performs the high-precision scan and a 100-digit
interval verification of the published safe lower bound.

## Trust boundary

**Established in this repository**

- the exact pressure multiplicity identity;
- the shifted-partition pressure average;
- the final high-precision and interval arithmetic;
- the integer scan selecting $m=215$ as the best value in the scanned range.

**Imported, not reproved here**

- the analytic inequality
  $S\ge H_{\mathrm{cert}}N+\mathop{\mathrm{tr}}\Psi(M)-o(N)$;
- the certified local seven-point inequality $F\ge 51063/10^7$;
- the sharp finite-$m$ Gram profile $h_m$;
- the normalization that the total normalized simple-zero gap length is
  $N+o(N)$.

These inputs are taken from the Anthropic / `trmdy` / `sxuff` lineage. If an
imported input fails, the bound here fails with it.

## Attribution

The analytic framework originates with Anthropic's work on simple zeros.
The re-optimized window, seven-point stability method and subsequent
refinements are due to the repositories listed in
[`docs/lineage.md`](docs/lineage.md).
`sxuff/zeta-positioned-pressure` supplies the positioned-pressure certificate
and the certified constants used here.

This repository contributes only the exact pressure-multiplicity retention
through shifted-block averaging and the resulting arithmetic improvement.

## License

The original material in this repository is released under the MIT License.
No license is asserted over third-party repositories or their code. This
repository does not copy the predecessor's verifier; it references its
certified outputs as external inputs.
