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
        A, C, E = np.random.randint(1, 51, 3)
        B, D, F = np.random.choice(np.arange(2, 21), 3, False)
        if is_gcd(A, B) and is_gcd(C, D) and is_gcd(E, F) and A != B and C != D and E != F and \
                A // B < 5 and C // D < 5 and E //F < 5 :

            BDF = get_lcm(get_lcm(B, D), F)
            A1 = A * (BDF // B)
            C1 = C * (BDF // D)
            E1 = E * (BDF // F)
            OP1, OP2 = np.random.choice(['-', '+'], 2, False)
            G = eval('%s %s %s' % (A1, OP1, C1))
            H = eval('%s %s %s' % (G, OP2, E1))
            if BDF < 51 and 0 < G < 51 and 0 < H < 51 and H // BDF < 10 and H % BDF and is_gcd(H%BDF, BDF) and max(A1, C1, E1) < 101 :
                break

    frac_1 = get_fraction(0, A, B, True)
    frac_2 = get_fraction(0, C, D, True)
    frac_3 = get_fraction(0, E, F, True)
    frac_4 = get_fraction(0, A, B)
    frac_5 = get_fraction(0, C, D)
    frac_6 = get_fraction(0, E, F)
    c1 = '= %s %s %s %s %s ' % (frac_4, OP1, frac_5, OP2, frac_6) if frac_1 != frac_4 or frac_2 != frac_5 or frac_3 != frac_6 else ''
    frac_7 = get_fraction(0, A1, BDF)
    frac_8 = get_fraction(0, C1, BDF)
    frac_9 = get_fraction(0, E1, BDF)
    frac_10 = get_fraction(0, H, BDF)
    frac_11 = get_fraction(0, H, BDF, True)
    c2 = ' = %s' % (frac_11) if frac_10 != frac_11 else ''

    stem = '%s %s %s %s %s = ' % (frac_1, OP1, frac_2, OP2, frac_3)
    answer = '%s' % (frac_11)
    comment = '%s %s %s %s %s %s= %s %s %s %s %s = %s%s' % (frac_1, OP1, frac_2, OP2, frac_3, c1, frac_7, OP1, frac_8, OP2, frac_9, frac_10, c2)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')