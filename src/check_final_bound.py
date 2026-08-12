"""High-precision scan plus interval verification of the final lower bound."""

from fractions import Fraction
import mpmath as mp
from mpmath import iv

mp.mp.dps = 100
iv.dps = 100

EPS = Fraction(51_063, 10_000_000)
B = Fraction(3, 1_150)
H = Fraction(672_457_041_414_544_284, 10**18)
SAFE = Fraction(6_732_623_755, 10_000_000_000)

def mpq(x: Fraction):
    return mp.mpf(x.numerator) / x.denominator

def iq(x: Fraction):
    return iv.mpf(x.numerator) / x.denominator

def h_m_float(m, E):
    threshold = mp.mpf(m) / (m - 1)
    if E <= threshold:
        return E
    return E / m + 2 * mp.sqrt(mp.mpf(m - 1) * E / m) - 1

def bound_float(m):
    A = mpq(EPS) * (m - 6)
    R = h_m_float(m, A)
    eta = R / A
    value = (m * mpq(H) - eta * mpq(B) * (m - 6)) / (m - R)
    return value, A, R, eta

# High-precision search for a convenient block length. The theorem only needs
# one rigorously verified m; optimality of the scan is not part of the proof.
best = None
for m in range(7, 5000):
    value, A, R, eta = bound_float(m)
    if best is None or value > best[0]:
        best = (value, m, A, R, eta)

value, m, A, R, eta = best
assert m == 215

# Rigorous interval recomputation at m=215.
M = 215
Ai = iq(EPS) * (M - 6)
threshold_i = iv.mpf(M) / (M - 1)

assert Ai.a > threshold_i.b
Ri = Ai / M + 2 * (((M - 1) * Ai / M) ** iv.mpf("0.5")) - 1
etai = Ri / Ai
bound_i = (M * iq(H) - etai * iq(B) * (M - 6)) / (M - Ri)
safe_i = iq(SAFE)

print(f"scan_best_m={m}")
print(f"float_A={mp.nstr(A, 100)}")
print(f"float_R={mp.nstr(R, 100)}")
print(f"float_eta={mp.nstr(eta, 100)}")
print(f"float_bound={mp.nstr(value, 100)}")
print(f"float_percent={mp.nstr(100*value, 100)}")
print(f"interval_A={Ai}")
print(f"interval_R={Ri}")
print(f"interval_eta={etai}")
print(f"interval_bound={bound_i}")
print(f"safe_lower={SAFE}")
print(f"interval_verified={bound_i.a > safe_i.b}")

assert bound_i.a > safe_i.b
