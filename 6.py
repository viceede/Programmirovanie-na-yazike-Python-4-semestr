def calculate_n_set(psi):
    n_set = set()
    for psi_element in psi:
        if psi_element >= 30 or psi_element <= -86:
            # Используем целочисленное деление для корректного вычисления
            n_value = (psi_element % 3) + ((psi_element + (1 if psi_element % 2 != 0 else 0)) // 2)
            n_set.add(n_value)
    return n_set


def calculate_delta_set(n_set):
    delta_set = set()
    for nu in n_set:
        if nu >= -23 or nu <= -52:
            delta_value = abs(nu) + nu
            delta_set.add(delta_value)
    return delta_set


def calculate_o_set(psi):
    o_set = set()
    for psi_element in psi:
        if -73 <= psi_element <= 42:
            o_value = (psi_element // 9) + (psi_element ** 3)
            o_set.add(o_value)
    return o_set


def calculate_zeta(o_set, delta_set):
    sum_part = 0
    for o in o_set:
        for delta in delta_set:
            sum_part += delta * o + (delta // 5)
    return len(o_set) + sum_part


def main(psi):
    n_set = calculate_n_set(psi)
    delta_set = calculate_delta_set(n_set)
    o_set = calculate_o_set(psi)
    zeta = calculate_zeta(o_set, delta_set)
    return zeta


# Тестовые данные
print(main({-64, 65, 99, 36, -88, -21, -14, -78, -43, -2}))  # Ожидаемый результат: -5526162
print(main({32, -92, 72, -52, -81, 82, -45, 84, 29}))       # Ожидаемый результат: -3142306