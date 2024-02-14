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
        B, D = np.random.choice(np.arange(2, 10), 2, False)
        A = np.random.randint(1, B)
        C = np.random.randint(1, D)

        E, F = np.random.randint(0, 4, 2)
        G = E * B + A
        H = F * D + C
        I = get_gcd(G, D)
        J = get_gcd(H, B)
        if I != 1 or J != 1 :
            G1 = G // I
            B1 = B // J
            H1 = H // J
            D1 = D // I
            K = G1 * H1
            L = B1 * D1
            if K < 301 and 1 < L < 301 and is_gcd(K, L) and K // L < 5 and K % L != 0:
                break

    frac_1 = get_fraction(E, A, B)
    frac_2 = get_fraction(F, C, D)
    frac_3 = get_fraction(0, G, B)
    frac_4 = get_fraction(0, H, D)
    frac_5 = get_fraction(0, K, L)
    frac_6 = get_fraction(0, K, L, True)

    c1 = '' if E == 0 and F == 0 else ' = %s \\times %s' % (frac_3, frac_4)
    c4 = ' = %s' % (frac_6) if frac_5 != frac_6 else ''
    if I != 1 and J != 1 :
        c2 = ' = \\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
             '\\times' \
             '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
             '' % (G1, G, B1, B, H1, H, D1, D)
        c3 = ' = \\frac {%s \\times %s}{%s \\times %s}' % (G1, H1, B1, D1)
    elif I != 1 :
        c2 = ' = \\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' \
             '\\times' \
             '\\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
             '' % (G1, G, B, H, D1, D)
        c3 = ' = \\frac {%s \\times %s}{%s \\times %s}' % (G1, H, B, D1)
    else :
        c2 = ' = \\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
             '\\times' \
             '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' \
             '' % (G, B1, B, H1, H, D)
        c3 = ' = \\frac {%s \\times %s}{%s \\times %s}' % (G, H1, B1, D)

    stem = '%s \\times %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_6)
    comment = '\\require{cancel} \\\\' \
              '%s \\times %s %s%s%s = %s%s' % (frac_1, frac_2, c1, c2, c3, frac_5, c4)

    return stem, answer, comment
