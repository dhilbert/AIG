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
    while True:
        A, B, C, D = np.random.randint(2, 21, 4)
        F, G = divmod(A, B)
        H, I = divmod(C, D)
        J = A * D
        K = B * I
        if G != 0 and I != 0 and J < 51 and K < 51 and is_gcd(J, K) and J // K < 5 :

            if ((A==B) or (A < B and is_gcd(A, B))) and ((C==D) or (C < D and is_gcd(C, D))) and F < 5 and H < 5 :
                f1 = get_fraction(F, G, B, True)
                f2 = get_fraction(H, I, D, True)
                f3 = get_fraction(H, D, I)
                break

    f5 = get_fraction(0, J, K)
    f6 = get_fraction(0, J, K, True)
    c1 = ' = %s' % (f6) if f5 != f6 else ''

    mode = np.random.randint(0, 4)
    if mode == 0 :
        stem = '%s \\times x = %s' % (f2, f1)
    elif mode == 1 :
        stem = 'x \\times %s = %s' % (f2, f1)
    elif mode == 2 :
        stem = '%s = %s \\times x' % (f1, f2)
    else :
        stem = '%s = x \\times %s' % (f1, f2)
    answer = '%s' % (f6)
    comment = 'x = %s \\div %s = %s \\times %s = %s%s' % (f1, f2, f1, f3, f5, c1)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')