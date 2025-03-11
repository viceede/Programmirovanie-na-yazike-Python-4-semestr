import math


def main(input_set):
    # Определение множества N
    N = {(psi % 3) + (psi // 2) for psi in input_set if (psi >= 30 or psi <= -86)}

    # Определение множества Delta
    Delta = {abs(nu) + nu for nu in N if (nu >= -23 or nu <= -52)}

    # Определение множества O
    O = {(psi // 9) + (psi ** 3) for psi in input_set if -73 <= psi <= 42}

    # Вычисление zeta
    zeta = len(O)
    for o in O:
        for delta in Delta:
            zeta += 6 * o + (delta // 5)

    return zeta


# Примеры использования
print(main((-64, 65, 99, 36, -88, -21, -14, -78, -43, -2)))  # Ожидаемый результат: -5526162
print(main((32, -92, 72, -52, -81, 82, -45, 84, 29)))  # Ожидаемый результат: -3142306
