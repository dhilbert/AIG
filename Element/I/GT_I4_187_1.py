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
        A, D = np.random.randint(0, 11, 2)
        C, F = np.random.randint(1, 10, 2)
        B, E = np.random.randint(1, 10, 2)

        if (B < C and is_gcd(B, C) and F == 1 and F != E) or (E < F and is_gcd(E, F) and C == 1 and C != B) :
            G = A * C + B if F == 1 else A + B // C
            H = D + E // F if F ==1 else D * F + E
            I = get_gcd(G, F)
            J = get_gcd(C, H)
            if I != 1 or J != 1 and I != J:
                G1 = G // I
                C1 = C // J
                H1 = H // J
                F1 = F // I

                K = G1 * H1
                L = C1 * F1
                if 1 < L < 301 and K < 301 and K // L < 6 and K % L != 0 and is_gcd(K % L, L):
                    break

    frac_1 = get_fraction(A, B, C, True)
    frac_2 = get_fraction(D, E, F, True)
    frac_3 = get_fraction(0, G1*H1, C1*F1)
    frac_4 = get_fraction(0, G1*H1, C1*F1, True)

    if J == 1:
        c1 = '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' \
             '\\times' \
             '\\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' % (G1, G, C, H, F1, F)
    else :
        c1 = '\\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
             '\\times' \
             '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' % (G, C1, C, H1, H, F)
    c2 = '\\frac {%s \\times %s}{%s \\times %s}' % (G1, H1, C1, F1)

    c3 = ' = %s' % (frac_4) if frac_3 != frac_4 else ''

    stem = '%s \\times %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_4)
    comment = '\\require{cancel} \\\\' \
              '%s \\times %s = \\frac {%s}{%s} \\times \\frac {%s}{%s} = %s = %s = %s%s' \
              '' % (frac_1, frac_2, G, C, H, F, c1, c2, frac_3, c3)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')