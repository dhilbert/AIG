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


def get_divisor(num):
    n = 0
    divisors = []
    while True :
        n += 1
        if num % n == 0 :
            divisors.append(n)

        if n == num:
            break
    return divisors


def generate():
    while True :
        mode = np.random.choice([1, 1, 0, 0], 3, False)
        frac, num1, num2 = [], [], []
        for m in mode :
            if m == 0 :
                while  True:
                    a = np.random.randint(1, 4)
                    b = pow(10, a)
                    c = np.random.choice(get_divisor(b)[1:-1], 1)[0] + np.random.choice([0, pow(10, a)], 1)[0]
                    if c % 10 != 0 :
                        frac.append('%s' % (round(c/b, a)))
                        num1.append(c)
                        num2.append(b)
                        break
            else :
                while True:
                    a, b  = np.random.randint(1, 21, 2)
                    if is_gcd(a, b) :
                        frac.append(get_fraction(0, a, b, True))
                        num1.append(a)
                        num2.append(b)
                        break
        A, C, E = num1
        B, D, F = num2

        if max(A//B, C//D, E//F) < 5 and A != B and C != D and E != F:
            if np.random.randint(0, 2) == 0 :
                AD = get_gcd(A, D)
                A1 = A // AD
                D1 = D // AD
                CF = get_gcd(C, F)
                C1 = C // CF
                F1 = F // CF
                BE = get_gcd(B, E)
                B1 = B // BE
                E1 = E // BE
                if not (AD == 1 and CF == 1 and BE == 1) :
                    A_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (A1, A) if AD != 1 else '%s' % (A)
                    B_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (B1, B) if BE != 1 else '%s' % (B)
                    C_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (C1, C) if CF != 1 else '%s' % (C)
                    D_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (D1, D) if AD != 1 else '%s' % (D)
                    E_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (E1, E) if BE != 1 else '%s' % (E)
                    F_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (F1, F) if CF != 1 else '%s' % (F)
                    if is_gcd(A1, D1) and is_gcd(C1, F1) and is_gcd(E1, B1) \
                            and is_gcd(B1, C1) and is_gcd(D1, E1) and is_gcd(A1, F1):
                        G = A1 * C1 * E1
                        H = B1 * D1 * F1

                        if G < 101 and 2 < H < 101 and G // H < 10 and G % H != 0 and is_gcd(G % H, H):
                            break

            else :
                BC = get_gcd(B, C)
                B1 = B // BC
                C1 = C // BC
                DE = get_gcd(D, E)
                D1 = D // DE
                E1 = E // DE
                AF = get_gcd(A, F)
                A1 = A // AF
                F1 = F // AF
                if not (BC == 1 and DE == 1 and AF == 1) :
                    A_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (A1, A) if AF != 1 else '%s' % (A)
                    B_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (B1, B) if BC != 1 else '%s' % (B)
                    C_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (C1, C) if BC != 1 else '%s' % (C)
                    D_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (D1, D) if DE != 1 else '%s' % (D)
                    E_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (E1, E) if DE != 1 else '%s' % (E)
                    F_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (F1, F) if AF != 1 else '%s' % (F)

                    if is_gcd(A1, D1) and is_gcd(C1, F1) and is_gcd(E1, B1) \
                            and is_gcd(B1, C1) and is_gcd(D1, E1) and is_gcd(A1, F1) :
                        G = A1 * C1 * E1
                        H = B1 * D1 * F1

                        if G < 101 and 2 < H < 101 and G // H < 10 and G % H != 0 and is_gcd(G%H, H) :
                            break

    frac_1, frac_2, frac_3 = frac
    frac_4 = get_fraction(0, G, H)
    frac_5 = get_fraction(0, G, H, True)

    c1 = '\\frac {%s}{%s} \\times \\frac {%s}{%s} \\times \\frac {%s}{%s}' \
         '' % (A_text, B_text, C_text, D_text, E_text, F_text)
    c2 = ' = %s' % (frac_5) if frac_4 != frac_5 else ''

    stem = '%s \\times %s \\times %s = ' % (frac_1, frac_2, frac_3)
    answer = '%s' % (frac_5)
    comment = '\\require{cancel} \\\\' \
              '%s \\times %s \\times %s = %s = %s%s' % (frac_1, frac_2, frac_3, c1, frac_4, c2)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')