import math


def calculate_n_set(psi_set):
    """Вычисляет множество n на основе входного множества psi_set."""
    n_set = set()
    for psi in psi_set:
        if psi >= 30 or psi <= -86:
            n = (psi % 3) + math.ceil(psi / 2)
            n_set.add(n)
    return n_set


def calculate_delta_set(n_set):
    """Вычисляет множество delta на основе множества n_set."""
    delta_set = set()
    for nu in n_set:
        if nu >= -23 or nu <= -52:
            delta = abs(nu) + nu
            delta_set.add(delta)
    return delta_set


def calculate_o_set(psi_set):
    """Вычисляет множество o на основе входного множества psi_set."""
    o_set = set()
    for psi in psi_set:
        if -73 <= psi <= 42:
            o = math.floor(math.floor(psi) / 9) + (psi ** 3)
            o_set.add(o)
    return o_set


def calculate_zeta(o_set, delta_set):
    """Вычисляет значение zeta на основе множеств o_set и delta_set."""
    zeta = len(o_set)
    for o in o_set:
        for delta in delta_set:
            zeta += 6 * o + math.floor(delta / 5)
    return zeta


def main(psi_set):
    """
    Основная функция для вычисления zeta на основе входного множества psi_set.

    :param psi_set: Множество значений psi
    :return: Значение zeta
    """
    n_set = calculate_n_set(psi_set)
    delta_set = calculate_delta_set(n_set)
    o_set = calculate_o_set(psi_set)
    zeta = calculate_zeta(o_set, delta_set)
    return zeta


# Тестовые примеры
print(main({-64, 65, 99, 36, -88, -21, -14, -78, -43, -2}))  # Ожидаемый результат: -5526162
print(main({32, -92, 72, -52, -81, 82, -45, 84, 29}))  # Ожидаемый результат: -3142306