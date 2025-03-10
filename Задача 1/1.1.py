import math


def main(z):
    chislitel = (37 * pow(z, 4) - 51 * pow(math.cos(8 * z - pow(z, 3)), 2))
    znamenatel = (49 * pow(z, 4) - 1)
    b = pow(math.log2(z), 2) / 21
    c = 31
    ex = (chislitel / znamenatel) + b + c
    return '%.2e' % ex
