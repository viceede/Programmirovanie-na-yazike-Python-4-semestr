import math


def main(psi_set):
    # Определение множества n
    n_set = set()
    for psi in psi_set:
        if psi >= 30 or psi <= -86:
            n = (psi % 3) + math.floor(psi / 2)
            n_set.add(n)

    # Определение множества delta
    delta_set = set()
    for nu in n_set:
        if nu >= -23 or nu <= -52:
            delta = abs(nu) + nu
            delta_set.add(delta)

    # Определение множества o
    o_set = set()
    for psi in psi_set:
        if -73 <= psi <= 42:
            o = math.floor(psi / 9) + psi ** 3
            o_set.add(o)

    # Вычисление zeta
    zeta = len(o_set)
    for o in o_set:
        for delta in delta_set:
            zeta += 6 * o + math.floor(delta / 5)

    return zeta

print(main((-64, 65, 99, 36, -88, -21, -14, -78, -43, -2)))
print(main((32, -92, 72, -52, -81, 82, -45, 84, 29)))