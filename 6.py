import math


def main(psi):
    # Вычисляем множество N
    n_set = set()
    for psi_element in psi:
        if psi_element >= 30 or psi_element <= -86:
            n_value = psi_element % 3 + math.ceil(psi_element / 2)
            n_set.add(n_value)

    # Вычисляем множество Delta
    delta_set = set()
    for nu in n_set:
        if nu >= -23 or nu <= -52:
            delta_value = abs(nu) + nu
            delta_set.add(delta_value)

    # Вычисляем множество O
    o_set = set()
    for psi_element in psi:
        if -73 <= psi_element <= 42:
            o_value = math.floor(psi_element / 9) + psi_element ** 3
            o_set.add(o_value)

    # Вычисляем сумму для zeta
    sum_part = 0
    for o in o_set:
        for delta in delta_set:
            sum_part += delta * o + math.floor(delta / 5)

    # Вычисляем zeta
    zeta = len(o_set) + sum_part

    return zeta