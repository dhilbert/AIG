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
        n = np.random.randint(0, 2)

        s1, s3 = np.random.randint(1, 21, 2)
        s2 = pow(10, n)
        s4 = np.random.randint(2, 21)

        if is_gcd(s3, s4) and s1%s2 != 0:
            #d1 = round(s1 / s2, n)
            d1 = s1 / s2
            f1 = get_fraction(0, s3, s4, True)
             
            if np.random.randint(0, 2) == 0 :
                A, B, c, d = s1, s2, s3, s4
                stem = '%s %s %s =' % (d1, OP1, f1)

            else :
                A, B, c, d = s3, s4, s1, s2
                stem = '%s %s %s =' % (f1, OP1, d1)
            C, D = [c, d] if OP1 == '\\times' else [d, c]
            AD = get_gcd(A, D)
            A1 = A // AD
            D1 = D // AD
            BC = get_gcd(B, C)
            B1 = B // BC
            C1 = C // BC

            E = A1 * C1
            F = B1 * D1

            if AD != 1 or BC != 1 and is_gcd(E, F) and 0 < E < 51 and 1 < F < 51 :
                break

    A_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (A1, A) if AD != 1 else '%s' % (A)
    B_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (B1, B) if BC != 1 else '%s' % (B)
    C_text = '\\displaystyle \\overset{%s} {\\cancel{%s}}' % (C1, C) if BC != 1 else '%s' % (C)
    D_text = '\\displaystyle \\underset{%s} {\\cancel{%s}}' % (D1, D) if AD != 1 else '%s' % (D)

    f2 = get_fraction(0, A, B)
    f3 = get_fraction(0, c, d)
    f4 = get_fraction(0, E, F)
    f5 = get_fraction(0, E, F, True)
    c1 = ' = %s' % (f5) if f4 != f5 else ''
    answer = '%s' % (f5)
    comment = '\\require{cancel}' \
              '%s %s %s %s = \\frac {%s}{%s} \\times \\frac {%s}{%s} = %s%s' \
              '' % (stem, f2, OP1, f3, A_text, B_text, C_text, D_text, f4, c1)






    return stem, answer, comment


if __name__ == '__main__':
    for i in range(0,10):
        stem, answer, comment = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')
        print(comment + '\\\\')