import math


def calc(delta_set):
    answ = 0
    for delta in delta_set:
        answ += math.floor(delta / 5)
    return answ


def main(input_set):
    O = {math.floor(psi / 9) + psi ** 3 for psi in input_set if -73 <= psi <= 42}

    Delta = {nu + abs(nu) for nu in range(-100, 101) if -52 <= nu <= -23}

    answ = len(O) + sum(6 * o for o in O) + calc(Delta) * len(O)

    return answ
