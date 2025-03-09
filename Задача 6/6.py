from math import floor


def calculate_o_set(psi):
    return {floor(psi_i / 9) + psi_i ** 3 for psi_i in psi if -73 <= psi_i <= 42}


def calculate_delta_set():
    return {nu + abs(nu) for nu in range(-100, 100) if nu >= -23 or nu <= -52}


def calculate_n_set(psi):
    return {psi_i % 3 + floor(psi_i / 2) for psi_i in psi if psi_i >= 30 or psi_i <= -86}


def main(psi):
    o_set = calculate_o_set(psi)
    delta_set = calculate_delta_set()
    n_set = calculate_n_set(psi)

    zeta = len(o_set)
    for o in o_set:
        for delta in delta_set:
            zeta += 6 * o + floor(delta / 5)

    return zeta
