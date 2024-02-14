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
        n = np.random.randint(1, 3)

        OP1, OP3, OP5 = np.random.choice(['\\times', '\\div', '\\times', '\\div'], 3, False)
        OP2, OP4 = np.random.choice(['+', '-'], 2)

        c, g, k = np.random.randint(1, 21, 3)
        A, E, I = [c, g, k] * np.reshape(np.random.randint(2, 6, 3), -1)
        B = d = F = h = J = l = pow(10, n)

        A, c = [A, c] if OP3 == '\\div' else [c, A]
        E, g = [E, g] if OP3 == '\\div' else [g, E]
        I, k = [I, k] if OP3 == '\\div' else [k, I]

        if A % 10 != 0 and c % 10 != 0 and E % 10 != 0 and g % 10 != 0 and I % 10 != 0 and k % 10 != 0 :
            d1, d2, d3, d4, d5, d6 = ['%s' % (round(i / pow(10, n), n)) for i in [A, c, E, g, I, k]]

            C, D = [c, d] if OP1 == '\\times' else [d, c]
            G, H = [g, h] if OP3 == '\\times' else [h, g]
            K, L = [k, l] if OP5 == '\\times' else [l, k]

            AD = get_gcd(A, D)
            A1 = A // AD
            D1 = D // AD
            BC = get_gcd(C, B)
            B1 = B // BC
            C1 = C // BC
            f1_n = A1 * C1
            f1_d = B1 * D1

            EH = get_gcd(E, H)
            E1 = E // EH
            H1 = H // EH
            FG = get_gcd(F, G)
            F1 = F // FG
            G1 = G // FG
            f2_n = E1 * G1
            f2_d = F1 * H1

            IL = get_gcd(I, L)
            I1 = I // IL
            L1 = L // IL
            JK = get_gcd(J, K)
            J1 = J // JK
            K1 = K // JK
            f3_n = I1 * K1
            f3_d = J1 * L1

            if 0 < f1_n < 101 and 0 < f2_n < 101 and len(set([f1_d, f2_d, f3_d])) != 1 \
                    and 0 < f3_n < 101 and f1_d != 1 and f2_d != 1 and f3_d != 1 :

                LCM = get_lcm(get_lcm(f1_d, f2_d), f3_d)
                n1 = f1_n * (LCM // f1_d)
                n2 = f2_n * (LCM // f2_d)
                n3 = f3_n * (LCM // f3_d)

                n4 = eval('%s %s %s' % (n1, OP2, n2))
                n5 = eval('%s %s %s' % (n4, OP4, n3))
                if 1 < LCM < 101 and 0 < n1 < 101 and 0 < n2 < 101 and 0 < n3 < 101 and 0 < n4 < 101 and 0 < n5 < 101 \
                        and is_gcd(n5, LCM) and n5 // LCM < 10 and n5 % LCM != 0:
                    break

    A_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (A1, A) if AD != 1 else '%s' % (A)
    B_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (B1, B) if BC != 1 else '%s' % (B)
    C_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (C1, C) if BC != 1 else '%s' % (C)
    D_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (D1, D) if AD != 1 else '%s' % (D)
    E_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (E1, E) if EH != 1 else '%s' % (E)
    F_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (F1, F) if FG != 1 else '%s' % (F)
    G_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (G1, G) if FG != 1 else '%s' % (G)
    H_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (H1, H) if EH != 1 else '%s' % (H)
    I_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (I1, I) if IL != 1 else '%s' % (I)
    J_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (J1, J) if JK != 1 else '%s' % (J)
    K_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (K1, K) if JK != 1 else '%s' % (K)
    L_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (L1, L) if IL != 1 else '%s' % (L)

    c1_a = '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (A_text, B_text, C_text, D_text) \
        if OP1 == '\\times' else '\\frac {%s}{%s} \\div \\frac {%s}{%s}' % (A, B, c, d)
    c1_b = '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (E_text, F_text, G_text, H_text) \
        if OP3 == '\\times' else '\\frac {%s}{%s} \\div \\frac {%s}{%s}' % (E, F, g, h)
    c1_c = '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (I_text, J_text, K_text, L_text) \
        if OP5 == '\\times' else '\\frac {%s}{%s} \\div \\frac {%s}{%s}' % (I, J, k, l)


    c2_a = '\\frac {%s}{%s}' % (f1_n, f1_d) if OP1 == '\\times' else '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (A_text, B_text, C_text, D_text)
    c2_b = '\\frac {%s}{%s}' % (f2_n, f2_d) if OP3 == '\\times' else '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (E_text, F_text, G_text, H_text)
    c2_c = '\\frac {%s}{%s}' % (f3_n, f3_d) if OP5 == '\\times' else '\\frac {%s}{%s} \\times \\frac {%s}{%s}' % (I_text, J_text, K_text, L_text)
    f4 = get_fraction(0, n5, LCM)
    f5 = get_fraction(0, n5, LCM, True)
    c3 = '' if f4 == f5  else ' = %s' % (f5)

    stem = '%s %s %s %s %s %s %s %s %s %s %s =' % (d1, OP1, d2, OP2, d3, OP3, d4, OP4, d5, OP5, d6)
    answer = '%s' % (f5)
    comment = '\\require{cancel}' \
              '\\begin{aligned}[t]' \
              '&%s %s %s %s %s %s %s %s %s %s %s \\\\' \
              '&= %s %s %s %s %s \\\\' \
              '&= %s %s %s %s %s \\\\' \
              '&= \\frac {%s}{%s} %s \\frac {%s}{%s} %s \\frac {%s}{%s}\\\\' \
              '&= \\frac {%s}{%s} %s \\frac {%s}{%s} %s \\frac {%s}{%s}\\\\' \
              '&= %s%s' \
              '\\end{aligned}' \
              '' % (d1, OP1, d2, OP2, d3, OP3, d4, OP4, d5, OP5, d6, c1_a, OP2, c1_b, OP4, c1_c,
                    c2_a, OP2, c2_b, OP4, c2_c,
                    f1_n, f1_d, OP2, f2_n, f2_d, OP4, f3_n, f3_d,
                    n1, LCM, OP2, n2, LCM, OP4, n3, LCM,
                    f4, c3)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')