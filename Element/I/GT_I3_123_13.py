import numpy as np


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
    A = np.random.randint(1, 10)
    B = np.random.randint(2, 11)
    C = A - 1

    frac_1 = '\\frac {%s}{%s}' % (B, B) if C == 0 else '%s \\frac {%s}{%s}' % (C, B, B)
    c1 = '' if C == 0 else '%s ' % (C)
    stem = '%s = %s\\frac{ \\left( \\quad \\right )}{%s}' % (A, c1, B)
    answer = '%s' % (frac_1)
    comment = '%s = %s' % (A, frac_1)

    return stem, answer, comment