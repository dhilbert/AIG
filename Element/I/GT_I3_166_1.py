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


def get_lcm(num1, num2):
    return num1 * num2 // get_gcd(num1, num2)


def generate():
    while True :
        A, D = np.random.randint(0, 11, 2)
        C, F = np.random.choice(np.arange(2, 21), 2, False)
        B = np.random.randint(1, C)
        E = np.random.randint(1, F)
        G = get_lcm(C, F)
        if get_gcd(B, C) == 1 and get_gcd(E, F) == 1 and G < 100 :
            H = B * (G // C)
            I = E * (G // F)
            OP = np.random.choice(['-', '+'], 1)[0] if A*G+H > D*G+I else '+'
            J = A - 1 if (OP == '-' and H < I) else A
            K = H + G if (OP == '-' and H < I) else H
            if K < 101 and H != I:
                L = eval('%s %s %s' % (J, OP, D))
                M = K-I if OP == '-' else H + I
                frac_6 = get_fraction(L, M, G)
                frac_7 = get_fraction(L, M, G, True)
                if L < 10 and M < 101 and M % G != 0 and get_gcd(M % G, G) == 1:
                    break

    frac_1 = get_fraction(A, B, C)
    frac_2 = get_fraction(D, E, F)
    frac_3 = get_fraction(A, H, G)
    frac_4 = get_fraction(D, I, G)
    frac_5 = get_fraction(J, K, G)

    stem = '%s %s %s = ' % (frac_1, OP, frac_2)
    answer = '%s' % (frac_7)
    comment = '%s %s %s = %s %s %s' % (frac_1, OP, frac_2, frac_3, OP, frac_4)
    comment += ' = %s %s %s' % (frac_5, OP, frac_4) if (OP == '-' and H < I) else ''
    comment += ' = %s' % (frac_6)
    comment += ' = %s' % (frac_7) if frac_6 != frac_7 else ''


    return stem, answer, comment