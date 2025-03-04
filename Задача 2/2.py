import math


def main(x):
    if x < 40:
        return (1 - x - 50 * x**3) ** 3
    elif 40 <= x < 114:
        return 62 * ((x**3 / 70 - x**2 / 60 - 34 * x) ** 3) - math.log10(x**7)
    elif 114 <= x < 213:
        return x**7 / 48
    else:  # x >= 213
        return (x**2 - 3 - x) / 24 - 43 * x**3
