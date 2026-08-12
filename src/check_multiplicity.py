"""Exact rational check of the pressure-position multiplicity identity."""

from fractions import Fraction

M = 215
Q = 6

DEN = 2_300_000_000
NUMS = [831_522, 1_096_590, 1_071_888, 1_071_888, 1_096_590, 831_522]
b = [Fraction(x, DEN) for x in NUMS]
B = sum(b, Fraction(0))

assert B == Fraction(3, 1150)

# c[j-1] is the total local pressure coefficient carried by internal
# block gap j, 1 <= j <= M-1.
c = []
for j in range(1, M):
    coeff = Fraction(0)
    for t in range(0, M - Q):
        r = j - t
        if 1 <= r <= Q:
            coeff += b[r - 1]
    c.append(coeff)

lhs = sum(c, Fraction(0))
rhs = (M - Q) * B

print(f"m={M}")
print(f"B={B}")
print(f"sum_c={lhs}")
print(f"(m-q)B={rhs}")
print(f"identity_verified={lhs == rhs}")

assert lhs == rhs

# Across all m shifted partitions a fixed global gap is a boundary once
# and occupies each internal position j=1,...,m-1 exactly once.
print(f"shift_total_per_global_gap={lhs}")
print(f"shift_average_per_global_gap={lhs / M}")
