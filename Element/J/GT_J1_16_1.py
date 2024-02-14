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
                A // B < 5 and C // D < 5 and E //F < 5:
            BD = get_lcm(B, D)
            A1 = A * (BD // B)
            C1 = C * (BD // D)
            G = A1 + C1
            BDF = get_lcm(BD, F)
            G1 = G * (BDF // BD)
            E1 = E * (BDF // F)
            H = G1 + E1
            if is_gcd(G, BD) and A1 < 51 and C1 < 51 and is_gcd(H, BDF) and G1 < 51 and E1 < 51:
                break



    frac_1 = get_fraction(0, A, B, True)
    frac_2 = get_fraction(0, C, D, True)
    frac_3 = get_fraction(0, E, F, True)
    frac_4 = get_fraction(0, A, B)
    frac_5 = get_fraction(0, C, D)
    frac_6 = get_fraction(0, E, F)
    c1 = '= %s + %s + %s ' % (frac_4, frac_5, frac_6) if frac_1 != frac_4 or frac_2 != frac_5 or frac_3 != frac_6 else ''
    frac_7 = get_fraction(0, A1, BD)
    frac_8 = get_fraction(0, C1, BD)
    frac_9 = get_fraction(0, G, BD)
    frac_10 = get_fraction(0, G1, BDF)
    frac_11 = get_fraction(0, E1, BDF)
    c2 = ' = %s + %s' % (frac_10, frac_11) if frac_9 != frac_10 or frac_6 != frac_11 else ''
    frac_12 = get_fraction(0, H, BDF)
    frac_13 = get_fraction(0, H, BDF, True)
    c3 = ' = %s' % (frac_13) if frac_12 != frac_13 else ''


    stem = '%s + %s + %s =' % (frac_1, frac_2, frac_3)
    answer = '%s' % (frac_13)
    comment = '%s + %s + %s %s= %s + %s + %s = %s + %s%s = %s%s' \
              '' % (frac_1, frac_2, frac_3, c1, frac_7, frac_8, frac_6, frac_9, frac_6, c2, frac_12, c3)

    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')