import math


def main(input_set):
    # Вычисляем множество n
    n = {
        psi % 3 + psi // 2
        for psi in input_set
        if (psi >= 30 or psi <= -86)
    }

    # Вычисляем множество delta
    delta = {
        abs(nu) + nu
        for nu in n
        if (nu >= -23 or nu <= -52)
    }

    # Вычисляем множество o
    o = {
        abs(psi // 9) + psi ** 3
        for psi in input_set
        if -73 <= psi <= 42
    }

    # Вычисляем сумму для каждого элемента в o x delta
    sum_part = sum(
        60 + math.floor(d / 5)
        for d in delta
    )

    # Вычисляем итоговое значение zeta
    zeta = len(o) + sum_part

    return zeta