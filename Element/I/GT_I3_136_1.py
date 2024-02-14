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
        D, A = sorted(list(np.random.randint(0, 11, 2)))
        C, F = np.random.choice(np.arange(2, 21), 2, False)
        B = np.random.randint(1, C)
        E = np.random.randint(1, F)

        G = get_lcm(C, F)
        if G != C and G != F :
            H = B * (G//C)
            I = E * (G//F)
            f1_v = A*G + H
            f2_v = D*G + I
            if G < 100 and f1_v > f2_v and H != I:
                J = A - D if H > I else A - D - 1
                K = H - I if H > I else G + H - I
                if (K==G or get_gcd(K, G) == 1) :
                    break

    frac_1 = get_fraction(A, B, C, True)
    frac_2 = get_fraction(D, E, F, True)
    frac_3 = get_fraction(A, H, G, True)
    frac_4 = get_fraction(D, I, G, True)
    frac_5 = get_fraction(A-1, G+H, G)
    frac_6 = get_fraction(J, K, G)
    frac_7 = get_fraction(J, K, G, True)

    stem = '%s - %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_7)
    comment = '%s - %s = %s - %s' % (frac_1, frac_2, frac_3, frac_4)
    comment += '' if H > I else ' = %s - %s' % (frac_5, frac_4)
    comment += ' = %s' % (frac_6)
    comment += ' = %s' % (frac_7) if frac_6 != frac_7 else ''

    return stem, answer, comment