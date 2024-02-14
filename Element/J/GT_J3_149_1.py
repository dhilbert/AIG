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
        OP1, OP3 = np.random.choice(['-', '+'], 2)
        OP2, OP4 = np.random.choice(['\\div', '\\times'], 2)
        A, C, e, G, i = np.random.randint(1, 21, 5)
        B, D, f, H, j = np.random.randint(2, 21, 5)

        E, F = [e, f] if OP2 == '\\times' else [f, e]
        I, J = [i, j] if OP4 == '\\times' else [j, i]

        if A != B and C != D and e != f and G != H and i != j and I != 1 and J != 1 and \
            is_gcd(A, B) and is_gcd(C, D) and is_gcd(e, f) and is_gcd(G, H) and is_gcd(i, j) :

            CF = get_gcd(C, F)
            C1 = C // CF
            F1 = F // CF
            DE = get_gcd(D, E)
            D1 = D // DE
            E1 = E // DE
            K = C1 * E1
            L = D1 * F1

            GJ = get_gcd(G, J)
            G1 = G // GJ
            J1 = J // GJ
            HI = get_gcd(H, I)
            H1 = H // HI
            I1 = I // HI
            M = G1 * I1
            N = H1 * J1

            if (CF != 1 or DE != 1) and (GJ !=1 or HI != 1) and \
                    1 < L < 21 and 1 < N <21 and 0 < K < 21 and 0 < M < 21 and B != L and L != N and B != N:

                LCM = get_lcm(get_lcm(B, L), N)
                A1 = A * (LCM // B)
                K1 = K * (LCM // L)
                M1 = M * (LCM // N)
                O = eval('%s %s %s' % (A1, OP1, K1))
                P = eval('%s %s %s' % (O, OP3, M1))
                if LCM < 51 and 0 < A1 < 51 and 0 < K1 < 51 and 0 < M1 < 51 and 0 < O < 51 and 0 < P < 51 \
                        and is_gcd(P, LCM):
                    break

    f1 = get_fraction(0, A, B, True)
    f2 = get_fraction(0, C, D, True)
    f3 = get_fraction(0, e, f, True)
    f4 = get_fraction(0, G, H, True)
    f5 = get_fraction(0, i, j, True)

    f6 = get_fraction(0, A, B)
    f7 = get_fraction(0, C, D)
    f8 = get_fraction(0, e, f)
    f9 = get_fraction(0, G, H)
    f10 = get_fraction(0, i, j)

    f11 = get_fraction(0, K, L)
    f12 = get_fraction(0, M, N)
    f13 = get_fraction(0, P, LCM)
    f14 = get_fraction(0, P, LCM, True)

    # A, C, e, G, i = np.random.randint(1, 21, 5)
    # B, D, f, H, j = np.random.randint(2, 21, 5)

    C_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (C1, C) if CF != 1 else '%s' % (C)
    D_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (D1, D) if DE != 1 else '%s' % (D)
    E_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (E1, E) if DE != 1 else '%s' % (E)
    F_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (F1, F) if CF != 1 else '%s' % (F)
    G_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (G1, G) if GJ != 1 else '%s' % (G)
    H_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (H1, H) if HI != 1 else '%s' % (H)
    I_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (I1, I) if HI != 1 else '%s' % (I)
    J_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (J1, J) if GJ != 1 else '%s' % (J)

    exp_1 = '%s %s %s %s %s %s %s %s %s' % (f1, OP1, f2, OP2, f3, OP3, f4, OP4, f5)
    exp_2 = '%s %s %s %s %s %s %s %s %s' % (f6, OP1, f7, OP2, f8, OP3, f9, OP4, f10)
    c1 = '' if exp_1 == exp_2 else '&= %s \\\\' % (exp_2)
    c1 = '' if OP2 == '\\times' and OP4 == '\\times' else c1
    c2 = '' if f13 == f14 else ' = %s' % (f14)

    stem = '%s =' % (exp_1)
    answer = '%s' % (f14)
    comment = '\\require{cancel} \\\\' \
              '\\begin{aligned}[t] \\\\' \
              '%s %s' \
              '&= %s %s \\frac {%s}{%s} \\times \\frac {%s}{%s} %s \\frac {%s}{%s} \\times \\frac {%s}{%s} \\\\' \
              '&= %s %s %s %s %s \\\\' \
              '&= \\frac {%s}{%s} %s \\frac {%s}{%s} %s \\frac {%s}{%s} \\\\'\
              '&= %s%s'\
              '\\end{aligned}' \
              ''% (exp_1, c1,
                   f6, OP1, C_text, D_text, E_text, F_text, OP3, G_text, H_text, I_text, J_text,
                   f6, OP1, f11, OP3, f12,
                   A1, LCM, OP1, K1, LCM, OP3, M1, LCM,
                   f13, c2)




    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')