from math import floor


def main(psi):
    o = {floor(psi_i / 9) + psi_i ** 3 for psi_i in psi if -73 <= psi_i <= 42}

    Delta = {nu + abs(nu) for nu in range(-100, 101) if -52 <= nu <= -23}

    n = {psi_i % 3 + floor(psi_i / 2) for psi_i in psi if psi_i >= 30 or psi_i <= -86}

    zeta = len(O)
    for o in O:
        for delta in Delta:
            zeta += 6 * o + floor(delta / 5)

    return zeta

x={-64, 65, 99, 36, -88, -21, -14, -78, -43, -2}
print(main(x))