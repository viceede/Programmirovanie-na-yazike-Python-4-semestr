from math import floor


def main(Psi):
    O = set()
    for psi in Psi:
        if -73 <= psi <= 42:
            O.add(floor(psi / 9) + psi ** 3)

    N = set()
    for psi in Psi:
        if psi >= 30 or psi <= -86:
            N.add(psi % 3 + psi // 2)

    Delta = set()
    for nu in range(-23, -53, -1):  # Исправленный диапазон
        if nu in range(-52, -22):  # Условие наличия в N
            Delta.add(abs(nu) + nu)

    zeta = len(O)
    for o in O:
        for delta in Delta:
            zeta += 60 + abs(delta) // 5

    return zeta

print(main({32, -92, 72, -52, -81, 82, -45, 84, 29}))