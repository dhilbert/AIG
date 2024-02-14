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


def get_frac_common(f1_n, f1_d, f2_n, f2_d, transform=False) :
    d_lcm = get_lcm(f1_d, f2_d)
    f1_n = f1_n * (d_lcm//f1_d)
    f2_n = f2_n * (d_lcm//f2_d)
    f1 = get_fraction(0, f1_n, d_lcm, transform)
    f2 = get_fraction(0, f2_n, d_lcm, transform)

    return [f1, f2], [f1_n, d_lcm, f2_n, d_lcm]


def get_reduction(numer, denom) :
    gcd = get_gcd(numer, denom)
    n1 = numer // gcd
    n2 = denom // gcd

    return '\\frac {%s}{%s}' % (n1, n2), n1, n2



def generate():
    while True :
        OP1, OP3, OP5 = np.random.choice(['-', '+'], 3)
        OP2, OP4 = np.random.choice(['\\times', '\\div'], 2)
        A, C, E, G, I, K = np.random.randint(1, 11, 6)
        B, D, F, H, J, L = np.random.randint(2, 11, 6)

        if B != D and F != H and J != L  \
            and is_gcd(A, B) and is_gcd(C, D) and is_gcd(E, F) and is_gcd(G, H) and is_gcd(I, J) and is_gcd(K, L) :

            BD = get_lcm(B, D)
            A1 = A * (BD // B)
            C1 = C * (BD // D)
            M = eval('%s %s %s' % (A1, OP1, C1))

            FH = get_lcm(F, H)
            E1 = E * (FH // F)
            G1 = G * (FH // H)
            N = eval('%s %s %s' % (E1, OP3, G1))

            JL = get_lcm(J, L)
            I1 = I * (JL // J)
            K1 = K * (JL // L)
            O = eval('%s %s %s' % (I1, OP5, K1))


            if 0 < M < 51 and 0 < N < 51 and 0 < O < 51 and 1 < BD < 51 and 1 < FH < 51 and 1 < JL < 51 \
                    and is_gcd(M, BD) and is_gcd(N, FH) and is_gcd(O, JL):

                P, Q = M, BD
                R, S = [N, FH] if OP2 == '\\times' else [FH, N]
                T, U = [O, JL] if OP4 == '\\times' else [JL, O]



                if np.random.randint(0, 2) == 0 :
                    # P, R, T
                    # Q, S, U
                    PS = get_gcd(P, S)
                    P1 = P // PS
                    S1 = S // PS

                    RU = get_gcd(R, U)
                    R1 = R // RU
                    U1 = U // RU

                    QT = get_gcd(Q, T)
                    Q1 = Q // QT
                    T1 = T // QT

                    W = P1 * R1 * T1
                    V = Q1 * S1 * U1

                    if 0 < W < 51 and 1 < V < 51 and is_gcd(U, V) :
                        P_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (P1, P) if PS != 1 else '%s' % (P)
                        Q_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (Q1, Q) if QT != 1 else '%s' % (Q)
                        R_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (R1, R) if RU != 1 else '%s' % (R)
                        S_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (S1, S) if PS != 1 else '%s' % (S)
                        T_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (T1, T) if QT != 1 else '%s' % (T)
                        U_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (U1, U) if RU != 1 else '%s' % (U)
                        break

                else :
                    QR = get_gcd(Q, R)
                    Q1 = Q // QR
                    R1 = R // QR

                    ST = get_gcd(S, T)
                    S1 = S // ST
                    T1 = T // ST

                    PU = get_gcd(P, U)
                    P1 = P // PU
                    U1 = U // PU

                    W = P1 * R1 * T1
                    V = Q1 * S1 * U1

                    if 0 < W < 51 and 1 < V < 51 and is_gcd(U, V) and U // V < 10 :
                        P_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (P1, P) if PU != 1 else '%s' % (P)
                        Q_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (Q1, Q) if QR != 1 else '%s' % (Q)
                        R_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (R1, R) if QR != 1 else '%s' % (R)
                        S_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (S1, S) if ST != 1 else '%s' % (S)
                        T_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (T1, T) if ST != 1 else '%s' % (T)
                        U_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (U1, U) if PU != 1 else '%s' % (U)
                        break


    f1 = get_fraction(0, A, B, True)
    f2 = get_fraction(0, C, D, True)
    f3 = get_fraction(0, E, F, True)
    f4 = get_fraction(0, G, H, True)
    f5 = get_fraction(0, I, J, True)
    f6 = get_fraction(0, K, L, True)

    f7 = get_fraction(0, A1, BD)
    f8 = get_fraction(0, C1, BD)
    f9 = get_fraction(0, E1, FH)
    f10 = get_fraction(0, G1, FH)
    f11 = get_fraction(0, I1, JL)
    f12 = get_fraction(0, K1, JL)

    f13 = get_fraction(0, M, BD)
    f14 = get_fraction(0, N, FH)
    f15 = get_fraction(0, O, JL)

    f16 = get_fraction(0, W, V)
    f17 = get_fraction(0, W, V, True)
    c1 = ' = %s' % (f17) if f16 != f17 else ''

    stem = '\\left( %s %s %s \\right) %s \\left( %s %s %s \\right) %s \\left( %s %s %s \\right) =' \
           '' % (f1, OP1, f2, OP2, f3, OP3, f4, OP4, f5, OP5, f6)
    answer = '%s' % (f17)
    comment = '\\require{cancel} \\\\' \
              '\\begin{aligned}[t] \\\\' \
              '\\left( %s %s %s \\right) %s \\left( %s %s %s \\right) %s \\left( %s %s %s \\right)' \
              '&= \\left( %s %s %s \\right) %s \\left( %s %s %s \\right) %s \\left( %s %s %s \\right) \\\\' \
              '&= %s %s %s %s %s \\\\' \
              '&= \\frac {%s}{%s} \\times \\frac {%s}{%s} \\times \\frac {%s}{%s} \\\\' \
              '&= %s%s' \
              '\\end{aligned}' \
              '' % (f1, OP1, f2, OP2, f3, OP3, f4, OP4, f5, OP5, f6,
                    f7, OP1, f8, OP2, f9, OP3, f10, OP4, f11, OP5, f12,
                    f13, OP2, f14, OP4, f15,
                    P_text, Q_text, R_text, S_text, T_text, U_text,
                    f16, c1)







    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')