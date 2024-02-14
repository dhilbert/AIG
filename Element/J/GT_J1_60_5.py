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


def get_lcm(num1, num2):
    return num1 * num2 // get_gcd(num1, num2)


def generate():
    while True :
        OP1, OP2, OP3 = np.random.choice(['+', '-'], 3)
        A, C, E, G = np.random.randint(1, 11, 4)
        B, D, F, H = sorted(list(np.random.choice(np.arange(2, 21), 4, False)))
        LCM = get_lcm(get_lcm(get_lcm(B, D), F), H)
        if len(set([B, D, F, H])) > 2 and A < B and C < D and E < F and G < H and \
                is_gcd(A, B) and is_gcd(C, D) and is_gcd(E, F) and is_gcd(G, H) and LCM < 101 :
            A1 = A * (LCM // B)
            C1 = C * (LCM // D)
            E1 = E * (LCM // F)
            G1 = G * (LCM // H)
            N1 = eval('%s %s %s' % (A1, OP1, C1))
            N2 = eval('%s %s %s' % (N1, OP2, E1))
            N3 = eval('%s %s %s' % (N2, OP3, G1))
            if min(N1, N2, N3) > 0 and max(N1, N2, N3) < 101 and is_gcd(N3, LCM):
                break

    f1 = get_fraction(0, A, B)
    f2 = get_fraction(0, C, D)
    f3 = get_fraction(0, E, F)
    f4 = get_fraction(0, G, H)

    f5 = get_fraction(0, A1, LCM)
    f6 = get_fraction(0, C1, LCM)
    f7 = get_fraction(0, E1, LCM)
    f8 = get_fraction(0, G1, LCM)

    f9 = get_fraction(0, N3, LCM)
    f10 = get_fraction(0, N3, LCM, True)
    c1 = ' = %s' % (f10) if f9 != f10 else ''

    stem = '%s %s %s %s %s %s %s =' % (f1, OP1, f2, OP2, f3, OP3, f4)
    answer = '%s' % (f10)
    comment = '\\begin{aligned}[t]' \
              '%s %s %s %s %s %s %s &= %s %s %s %s %s %s %s \\\\' \
              '&= %s%s' \
              '\\end{aligned}' \
              '' % (f1, OP1, f2, OP2, f3, OP3, f4, f5, OP1, f6, OP2, f7, OP3, f8,
                    f9, c1)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')