import math


def main(psi_set):
    # Определение множества N
    N = set()
    for psi in psi_set:
        if psi >= 30 or psi <= -86:
            n = (psi % 3) + math.ceil(psi / 2)
            N.add(n)

    # Определение множества Delta
    Delta = set()
    for nu in N:
        if nu >= -23 or nu <= -52:
            delta = abs(nu) + nu
            Delta.add(delta)

    # Определение множества O
    O = set()
    for psi in psi_set:
        if -73 <= psi <= 42:
            o = math.floor(math.floor(psi) / 9) + (psi ** 3)
            O.add(o)

    # Вычисление zeta
    zeta = len(O)
    for o in O:
        for delta in Delta:
            zeta += 6 * o + math.floor(delta / 5)

    return zeta

print(main({-64, 65, 99, 36, -88, -21, -14, -78, -43, -2}))  # Ожидаемый результат: -5526162
print(main({32, -92, 72, -52, -81, 82, -45, 84, 29}))  # Ожидаемый результат: -3142306