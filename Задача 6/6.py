import math


def main(psi):
    O = {math.floor(psi_i / 9) + psi_i ** 3 for psi_i in psi if -73 <= psi_i <= 42}

    Delta = {nu + abs(nu) for nu in range(-100, 101) if nu >= -23 or nu <= -52}

    zeta = len(O)
    for o in O:
        for delta in Delta:
            zeta += 6 * o + math.floor(delta / 5)

    return zeta
