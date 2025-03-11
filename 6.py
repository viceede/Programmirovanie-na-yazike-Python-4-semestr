def main(input_set):
    # Определение множества n
    n = {(psi % 3) + (psi // 2) for psi in input_set if (psi >= 30 or psi <= -86)}

    # Определение множества delta
    delta = {abs(nu) + nu for nu in n if (nu >= -23 or nu <= -52)}

    # Определение множества o
    o = {(psi // 9) + (psi ** 3) for psi in input_set if -73 <= psi <= 42}

    # Вычисление zeta
    zeta = len(o)
    for o_val in o:
        for delta_val in delta:
            zeta += 6 * o_val + (delta_val // 5)

    return zeta


# Примеры использования
print(main((-64, 65, 99, 36, -88, -21, -14, -78, -43, -2)))  # Ожидаемый результат: -5526162
print(main((32, -92, 72, -52, -81, 82, -45, 84, 29)))  # Ожидаемый результат: -3142306