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
                exp = '%s + %s' % (round(C/B, A), get_fraction(G, F, D))
                frac_1 = get_fraction(0, C, B)
                frac_2 = get_fraction(0, H, D)
                frac_3, n1, n2 = get_reduction(C, B)
                frac_4 = frac_2
                [frac_5, frac_6], [f1_n, f1_d, f2_n, f2_d] = get_frac_common(n1, n2, H, D)
            else :
                exp = '%s + %s' % (get_fraction(G, F, D), round(C/B, A))
                frac_1 = get_fraction(0, H, D)
                frac_2 = get_fraction(0, C, B)
                frac_3 = frac_1
                frac_4, n1, n2 = get_reduction(C, B)
                [frac_5, frac_6], [f1_n, f1_d, f2_n, f2_d] = get_frac_common(H, D, n1, n2)

            I = f1_n + f2_n
            if (mode == 0 and f1_d != B) or (mode == 1 and f2_d != B) and is_gcd(I, f1_d) and I < 301 and f1_d < 301 :
                frac_7 = get_fraction(0, I, f1_d)
                frac_8 = get_fraction(0, I, f1_d, True)
                if I // f1_d < 10 and I % f1_d != 0 and is_gcd(I%f1_d, f1_d) :
                    if C > 1 :
                        break


    c1 = '= %s + %s ' % (frac_3, frac_4) if frac_1 != frac_3 or frac_2 != frac_4 else ''
    c2 = '= %s + %s ' % (frac_5, frac_6)
    c3 = c2 if c1 != c2 else ''
    c4 = ' = %s' % (frac_8) if frac_7 != frac_8 else ''
    stem = '%s =' % (exp)
    answer = '%s' % (frac_8)
    comment = '%s = %s + %s %s%s = %s%s' \
              '' % (exp, frac_1, frac_2, c1, c3, frac_7, c4)
    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')