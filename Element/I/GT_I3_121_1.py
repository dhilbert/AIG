import numpy as np


def get_gcd(num1, num2):
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break
    return gcd


def get_fraction(num1, num2, num3, transform=False) :
    if transform :
        if num2 % num3 == 0:
            result = str(num1 + num2//num3)
        else :
            num1 = '' if num1 + (num2//num3) == 0 else num1 + (num2//num3)
            result = '%s \\frac {%s}{%s}' % (num1, num2 % num3, num3)
    else :
        if num2 % num3 == 0 :
            result = '\\frac {%s}{%s}' % (str(num1+num2//num3), 1)
        else :
            num1 = '' if num1 == 0 else num1
            result = '%s \\frac {%s}{%s}' % (num1, num2, num3)

    return result.strip()


def generate():
    while True :
        A = np.random.randint(1, 10)
        B = np.random.randint(2, 11)
        C = np.random.randint(1, B)
        D = B*A - C
        if get_gcd(B, C) == 1 and get_gcd(B, D) == 1 :
            break

    frac_1 = get_fraction(0, C, B)
    frac_2 = '\\frac {%s}{%s}' % (A*B, B)
    frac_3 = get_fraction(0, D, B)
    frac_4 = get_fraction(0, D, B, True)

    c1 = ' = %s' % (frac_4) if frac_3 != frac_4 else ''
    stem = '%s - %s =' % (A, frac_1)
    answer = '%s' % (frac_4)
    comment = '%s - %s = %s - %s = %s%s' \
              '' % (A, frac_1, frac_2, frac_1, frac_3, c1)
    return stem, answer, comment