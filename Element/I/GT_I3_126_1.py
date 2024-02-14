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
        D, A = sorted(list(np.random.choice(np.arange(0, 11), 2, False)))
        B = np.random.randint(3, 11)
        C, E = np.random.choice(np.arange(1, B+1), 2, False)
        F = A - D if C > E else A - D - 1
        G = C - E if C > E else (C + B) - E
        if get_gcd(B, C) == 1 and (B==E or get_gcd(B, E) == 1) and get_gcd(B, G) == 1 and G < B :
            if C > E or (C < E and F >= 0) :
                break

    c1 = '' if A-1 == 0 else '%s ' % (A-1)
    frac_1 = get_fraction(A, C, B, True)
    frac_2 = get_fraction(D, E, B, True)
    stem = '%s - %s =' % (frac_1, frac_2)
    answer = '%s' % (get_fraction(F, G, B))
    comment = '%s - %s = %s' % (frac_1, frac_2, answer) if (C > E or B == E) else \
        '%s - %s = %s\\frac {%s}{%s} - %s = %s' % (frac_1, frac_2, c1, B+C, B, frac_2, answer)


    return stem, answer, comment