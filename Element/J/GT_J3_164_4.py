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


def get_lcm(num1, num2):
    return num1 * num2 // get_gcd(num1, num2)


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


def get_frac_common(f1_n, f1_d, f2_n, f2_d) :
    d_lcm = get_lcm(f1_d, f2_d)
    f1_n = f1_n * (d_lcm//f1_d)
    f2_n = f2_n * (d_lcm//f2_d)
    f1 = get_fraction(0, f1_n, d_lcm)
    f2 = get_fraction(0, f2_n, d_lcm)

    return [f1, f2], [f1_n, d_lcm, f2_n, d_lcm]


def get_reduction(numer, denom) :
    gcd = get_gcd(numer, denom)
    n1 = numer // gcd
    n2 = denom // gcd

    return '\\frac {%s}{%s}' % (n1, n2), n1, n2


def generate():
    while True :
        OP1 = np.random.choice(['\\div', '\\times'], 1)[0]
        OP2, OP3 = np.random.choice(['+', '-'], 2)
        A, C, E, G = np.random.randint(1, 21, 4)
        B, D, F, H = np.random.randint(1, 21, 4)
        if is_gcd(A, B) and is_gcd(C, D) and is_gcd(E, F) and is_gcd(G, H) and len(set([D, F, H])) != 1 :
            n1, n2, n3, n4 = A // B, C // D, E // F, G // H
            d1, d2, d3, d4 = A % B, C % D, E % F, G % H
            if max(n1, n2, n3, n4) < 5 and 0 not in [d1, d2, d3, d4]:
                DFH = get_lcm(get_lcm(D, F), H)
                C1 = C * (DFH // D)
                E1 = E * (DFH // F)
                G1 = G * (DFH // H)
                C2 = n2 * DFH + C1
                E2 = n3 * DFH + E1
                G2 = n4 * DFH + G1

                I = eval('%s %s %s' % (C2, OP2, E2))
                J = eval('%s %s %s' % (I, OP3, G2))
                if 0 < I < 51 and 0 < J < 51 and C2 < 51 and E2 < 51 and G2 < 51 and is_gcd(J, DFH):
                    K, L = [J, DFH] if OP1 == '\\times' else [DFH, J]
                    AL = get_gcd(A, L)
                    BK = get_gcd(B, K)
                    if AL != 1 or BK != 1 :
                        A1 = A // AL
                        B1 = B // BK
                        K1 = K // BK
                        L1 = L // AL
                        M = A1 * K1
                        N = B1 * L1
                        if M < 101 and N < 101 and M // N < 10 and M % N != 0 :
                            break


    frac_1 = get_fraction(0, A, B, True)
    frac_2 = get_fraction(0, C, D, True)
    frac_3 = get_fraction(0, E, F, True)
    frac_4 = get_fraction(0, G, H, True)

    frac_5 = '%s \\frac {%s}{%s}' % (n2, C1%DFH, DFH) if n2 != 0 else '\\frac {%s}{%s}' % (C1, DFH)
    frac_6 = '%s \\frac {%s}{%s}' % (n3, E1%DFH, DFH) if n3 != 0 else '\\frac {%s}{%s}' % (E1, DFH)
    frac_7 = '%s \\frac {%s}{%s}' % (n4, G1%DFH, DFH) if n4 != 0 else '\\frac {%s}{%s}' % (G1, DFH)

    frac_8 = get_fraction(0, C2, DFH)
    frac_9 = get_fraction(0, E2, DFH)
    frac_10 = get_fraction(0, G2, DFH)

    frac_11 = get_fraction(0, M, N)
    frac_12 = get_fraction(0, M, N, True)
    A1_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (A1, A) if AL != 1 else '%s' % (A)
    B1_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (B1, B) if BK != 1 else '%s' % (B)
    K1_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (K1, K) if BK != 1 else '%s' % (K)
    L1_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (L1, L) if AL != 1 else '%s' % (L)
    c1 = '&= %s %s \\left( %s %s %s %s %s \\right) \\\\' % (frac_1, OP1, frac_8, OP2, frac_9, OP3, frac_10) \
        if frac_5 != frac_8 or frac_6 != frac_9 or frac_7 != frac_10 else ''
    c2 = '&= \\frac {%s}{%s} \\div \\frac {%s}{%s}\\\\' % (A, B, L, K) if OP1 == '\\div' else ''
    c3 = '&= \\frac {%s}{%s} \\times \\frac {%s}{%s}' % (A1_text, B1_text, K1_text, L1_text)
    c4 = ' = %s' % (frac_12) if frac_11 != frac_12 else ''

    stem = '%s %s \\left( %s %s %s %s %s \\right) =' % (frac_1, OP1, frac_2, OP2, frac_3, OP3, frac_4)
    answer = '%s' % (frac_12)
    comment = '\\begin{aligned}[t]' \
              '%s %s \\left( %s %s %s %s %s \\right) &= %s %s \\left( %s %s %s %s %s \\right) \\\\' \
              '%s' \
              '%s%s\\\\' \
              '&= %s%s' \
              '\\end{aligned}' \
              '' % (frac_1, OP1, frac_2, OP2, frac_3, OP3, frac_4, frac_1, OP1, frac_5, OP2, frac_6, OP3, frac_7,
                    c1, c2, c3, frac_11, c4)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')