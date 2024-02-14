import numpy as np


def get_gcd(num1, num2):
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break
    return gcd


def generate():
    while True :
        A = np.random.randint(2, 11)
        B = np.random.randint(1, A)
        C = np.random.randint(2, 11)
        D = A * C
        E = B * C
        if get_gcd(A, B) == 1 and D < 101 and E < 101 :
            break

    stem = '\\frac {%s}{%s} =' % (E, D)
    answer = '\\frac {%s}{%s}' % (B, A)
    comment = '\\frac {%s}{%s} = \\frac {%s \\div %s}{%s \\div %s} = %s' % (E, D, E, C, D, C, answer)

    return stem, answer, comment