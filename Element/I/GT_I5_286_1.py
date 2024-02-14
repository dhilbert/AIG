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
        A = np.random.randint(1, 4)
        B = pow(10, A)
        B_divs = get_divisor(B)[1:-1]
        C = np.random.choice(B_divs, 1)[0] + pow(10, np.random.choice([0, A], 1)[0])
        D = np.random.choice(B_divs, 1)[0]
        F = np.random.randint(1, D)
        G = np.random.randint(0, 4) if D < 10 else 0
        H = G * D + F
        if is_gcd(F, D) and F < 101 and C % 10 != 0 and is_gcd(C, B) == False and H < 301 :
            mode = np.random.randint(0, 2)
            if mode == 0 :
                a, b, c, d = C, B, H, D
            else :
                a, b, c, d = H, D, C, B

            I = get_gcd(a, d)
            J = get_gcd(c, b)
            a1 = a // I
            b1 = b // J
            c1 = c // J
            d1 = d // I
            K = b1 * d1
            L = a1 * c1
            if K < 301 and 1 < L < 301 and K // L < 10 and K % L != 0 and is_gcd(K%L, L) :
                if mode == 0 :
                    exp = '%s \\times %s' % (round(C/B, A), get_fraction(G, F, D))
                else :
                    exp = '%s \\times %s' % (get_fraction(G, F, D), round(C/B, A))

                if I != 1 and J != 1:
                    c1 = '= \\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
                         '\\times' \
                         '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
                         '' % (a1, a, b1, b, c1, c, d1, d)
                elif I != 1:
                    c1 = '= \\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' \
                         '\\times' \
                         '\\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
                         '' % (a1, a, b, c, d1, d)
                else:
                    c1 = '= \\frac {%s}{\\displaystyle \\underset{%s} {\\cancel{%s}}}' \
                         '\\times' \
                         '\\frac {\\displaystyle \\overset{%s} {\\cancel{%s}}}{%s}' \
                         '' % (a, b1, b, c1, c, d)
                break

    frac_1 = get_fraction(0, L, K)
    frac_2 = get_fraction(0, L, K, True)
    c2 = ' = %s' % (frac_2) if frac_1 != frac_2 else ''
    stem = '%s =' % (exp)
    answer = '%s' % (frac_2)
    comment = '\\require{cancel} \\\\' \
              '%s %s = %s%s' \
              '' % (exp, c1, frac_1, c2)
    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')