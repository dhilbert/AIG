import numpy as np


def is_gcd(num1, num2):
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break

    if gcd == 1 :
        return True
    else :
        return False


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
    while True:
        A = np.random.randint(2, 10)
        B = np.random.randint(2, 11)
        C = np.random.randint(1, A)
        D = A * B
        E = np.random.randint(1, D)
        if D < 101 and E < 101 :
            F = C * A
            G = E + F
            H = G % D
            if is_gcd(B, C) and is_gcd(D, E) and (D==G or is_gcd(H, D)) and G // D < 2:
                break

    mode = np.random.randint(0, 2)
    c1 = ' = 1' if G == D else ' = %s' % (get_fraction(0, G, D, True)) if G > D else ''
    if mode == 0 :
        stem = '\\frac {%s}{%s} + \\frac {%s}{%s}' % (E, D, C, B)
        answer = '%s' % (get_fraction(0, G, D, True))
        comment = '%s = \\frac {%s}{%s} + \\frac {%s}{%s} = \\frac {%s + %s}{%s} = \\frac {%s}{%s}%s' \
                  '' % (stem, E, D, F, D, E, F, D, G, D, c1)
    else :
        stem = '\\frac {%s}{%s} + \\frac {%s}{%s}' % (C, B, E, D)
        answer = '%s' % (get_fraction(0, G, D, True))
        comment = '%s = \\frac {%s}{%s} + \\frac {%s}{%s} = \\frac {%s + %s}{%s} = \\frac {%s}{%s}%s' \
                  '' % (stem, F, D, E, D, F, E, D, G, D, c1)

    stem = '%s =' % (stem)
    return stem, answer, comment