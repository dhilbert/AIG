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
        D = A - 1
        E = B + C
        if (B == C or get_gcd(B, C) == 1) :
            break

    frac_1 = get_fraction(A, C, B, True) if B != C else get_fraction(A-1, 1, 1, True)
    frac_2 = get_fraction(D, E, B)
    c1 = '' if D == 0 else '%s ' % (D)

    stem = '%s = %s\\frac { \\left( \\quad \\right) }{%s}' % (frac_1, c1, B)
    answer = '%s' % (E)
    comment = '%s = %s\\frac {%s + %s}{%s} = %s' % (frac_1, c1, B, C, B, frac_2)

    return stem, answer, comment