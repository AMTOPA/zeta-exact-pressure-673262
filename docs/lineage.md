# Lineage and prior art

Every row below concerns the same quantity,

$$
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)},
$$

subject to the trust boundary stated by each source.

| Source | Bound advertised by source | Main lever |
| --- | ---: | --- |
| Anthropic / Claude | 0.672500703679... | unconditional trace/inertia framework |
| `ainta/zeta-simple-zeros` | 0.673008527927... | seven-point stability certificate |
| `trmdy/zeta-simple-zeros-673137` | 0.673137630699... | re-optimized window and weighted seven-point certificate |
| `sxuff/zeta-positioned-pressure` | 0.673205978423... | position-dependent pressure and sharp finite-$m$ profile |
| **this repository** | **0.673262375585...** | **exact pressure multiplicity under shifted averaging** |

## Immediate predecessor

Repository:

[`sxuff/zeta-positioned-pressure`](https://github.com/sxuff/zeta-positioned-pressure)

The predecessor certifies the local target

$$
\varepsilon=\frac{51063}{10^7}
$$

with total pressure

$$
B=\frac3{1150},
$$

and imports the analytic constant

$$
H_{\mathrm{cert}}
=\frac{672457041414544284}{10^{18}}.
$$

Its published final block deduction upper-bounds every internal pressure
coefficient by $B$, producing a shifted-average pressure penalty proportional
to $m-1$.

The present refinement keeps the exact internal coefficients $c_j$. Their sum
is

$$
\sum_{j=1}^{m-1}c_j=(m-6)B,
$$

and each global gap traverses every internal block position once over the
$m$ shifts. This changes only the global pressure bookkeeping; no local
certificate is changed.

## Scope

This repository does not claim an independent verification of the
predecessor's interval arithmetic or of the Anthropic analytic interface.
It is intended to isolate a short, auditable combinatorial refinement.
