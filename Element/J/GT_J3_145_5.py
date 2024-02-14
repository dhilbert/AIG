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
        OP2, OP3 = np.random.choice(['+', '-'], 2)
        OP4 = np.random.choice(['*', '//'])

        A, B = np.random.choice(np.arange(1, 21), 2, False)
        C = np.random.randint(1, 21)
        D = np.random.randint(2, 21)
        E, F = np.random.choice(np.arange(1, 21), 2, False)
        G = np.random.randint(2, 21)
        BD = get_gcd(B, D)
        if is_gcd(C, D) and BD != 1 and BD != D:
            B1 = B // BD
            D1 = D // BD
            H = eval('%s %s %s' % (E, OP3, F))
            I = B1*C
            if H > 0 and 0 < I < D1*A and H != G:
                if (OP4 == '//' and H % G == 0 and H // G > 1) or OP4 == '*' and H * G < 100 and A > BD  :
                    J = int(eval('%s %s %s' % (H, OP4, G)))
                    K = A - 1 - (I // D1)
                    L = D1 - (I % D1)
                    M = eval('%s %s %s' % (K, OP2, J))
                    if 0 <= M < 10 and is_gcd(D1, L) :
                        break

    c1 = '\\displaystyle \\overset{%s} {\\cancel{%s}}' \
         '\\times' \
         '\\frac {%s}{\\displaystyle \\underset{%s} {\cancel{%s}}}' \
         '' % (B1, B, C, D1, D)

    OP4 = '\\times' if OP4 == '*' else '\\div'
    frac_1 = get_fraction(0, C, D, True)
    frac_2 = get_fraction(0, I, D1)
    frac_3 = get_fraction(0, I, D1, True)
    frac_4 = '%s \\frac {%s}{%s}' % (A-1, D1, D1)
    frac_5 = get_fraction(K, L, D1)
    frac_6 = get_fraction(M, L, D1)
    c2 = ' = %s - %s %s %s' % (A, frac_3, OP2, J) if frac_2 != frac_3 else ''
    stem = '%s - %s \\times %s %s \\left( %s %s %s \\right) %s %s' % (A, B, frac_1, OP2, E, OP3, F, OP4, G)
    answer = '%s' % (frac_6)
    comment = '\\begin{aligned}[t]' \
              '%s - %s \\times %s %s \\left( %s %s %s \\right) %s %s ' \
              '& = %s - %s %s %s %s %s  \\\\' \
              '& = %s - %s %s %s%s \\\\' \
              '& = %s - %s %s %s \\\\' \
              '&= %s %s %s\\\\' \
              '& = %s'  \
              '\\end{aligned}' \
              '' % (A, B, frac_1, OP2, E, OP3, F, OP4, G,
                    A, c1, OP2, H, OP4, G,
                    A, frac_2, OP2, J, c2,
                    frac_4, frac_3, OP2, J,
                    frac_5, OP2, J, frac_6)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')