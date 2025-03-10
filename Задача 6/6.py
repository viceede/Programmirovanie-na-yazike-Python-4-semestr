from math import floor


def main(Psi):
    O = {floor(psi / 9) + psi ** 3 for psi in Psi if -73 <= psi <= 42}
    N = {psi % 3 + psi // 2 for psi in Psi if psi >= 30 or psi <= -86}
    Delta = {abs(nu) + nu for nu in range(-23, -51, -1)}

    zeta = len(O) + sum(60 + abs(delta) // 5 for o in O for delta in Delta)
    return zeta