# Exact pressure multiplicity refinement

## Summary

This document records the new combinatorial step: retain the exact pressure multiplicities from the seven-point certificate until the shifted-block averaging stage.

Let

\[
B=\sum_{r=1}^{6}b_r=\frac3{1150}.
\]

For an \(m\)-point block define

\[
c_j=\sum_{\substack{0\le t\le m-7\\1\le j-t\le6}}b_{j-t}.
\]

Then double counting gives

\[
\sum_{j=1}^{m-1}c_j=(m-6)B.
\]

A fixed global gap appears in every internal position exactly once under the \(m\) shifted partitions, so its total pressure charge is also \((m-6)B\).

## Bound assembly

Using the imported constants

\[
H_{cert}=672457041414544284/10^{18},
\]

\[
\varepsilon=51063/10^7,
\]

and the imported finite block profile \(h_m\), the resulting bound is

\[
\frac{N_0^s(T,2T)}{N(T,2T)}\ge
\frac{mH_{cert}-\eta_mB(m-6)}{m-R_m}-o(1).
\]

The arithmetic scan selects

\[
m=215,
\]

and gives

\[
0.673262375584978050386191646193095784\ldots.
\]

Therefore the safe published lower bound is

\[
\boxed{67.32623755\%}.
\]

## Scope note

This repository proves the multiplicity refinement and checks the arithmetic. The analytic inequality, interval certificate, and finite-dimensional profile are imported from the preceding lineage and remain outside the proof boundary here.
