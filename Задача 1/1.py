import math


def main(z):
    chislitel = (37 * z ** 4 - 51 * (math.cos(8 * z - z ** 3)) ** 2)
    znamenatel = (49 * z ** 4 - 1)
    b = (math.log2(z)) ** 2 / 21
    c = 31
    ex = (chislitel/znamenatel) + b + c
    return '%.2e' % ex

print(main(0.08))