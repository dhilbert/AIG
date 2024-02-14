import numpy as np


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


def get_gcd(num1, num2):
    num1, num2 = sorted([num1, num2])
    gcd = 1
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break
    return gcd


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


def get_lcm(num1, num2):
    return num1 * num2 // get_gcd(num1, num2)


def generate():
    while True :
        OP1, OP2 = np.random.choice(['-', '+'], 2)
        B, D = np.random.choice(np.arange(2, 11), 2, False)
        A = np.random.randint(1, B)
        C = np.random.randint(1, D)
        BD = get_lcm(B, D)
        if is_gcd(A, B) and is_gcd(C, D) and BD != 1:
            A1 = A * (BD // B)
            C1 = C * (BD // D)
            E = eval('%s %s %s' % (A1, OP2, C1))
            F = np.random.randint(1, 5)
            G = eval('%s %s %s' % (F * BD, OP1, E))
            if 0 < E < 51 and 0 < G < 51:
                break

    frac_1 = get_fraction(0, A, B, True)
    frac_2 = get_fraction(0, C, D, True)
    frac_3 = get_fraction(0, A1, BD)
    frac_4 = get_fraction(0, C1, BD)
    frac_5 = get_fraction(0, E, BD)
    frac_6 = '\\frac {%s}{%s}' % (F*BD, BD)
    frac_7 = get_fraction(0, G, BD)
    frac_8 = get_fraction(0, G, BD, True)
    c1 = ' = %s' % (frac_8) if frac_7 != frac_8 else ''
    stem = '%s %s \\left( %s %s %s \\right) = ' % (F, OP1, frac_1, OP2, frac_2)
    answer = '%s' % (frac_8)
    comment = '%s %s \\left( %s %s %s \\right) = %s %s \\left( %s %s %s \\right) = %s %s %s = %s %s %s = %s%s' \
              '' % (F, OP1, frac_1, OP2, frac_2, F, OP1, frac_3, OP2, frac_4, F, OP1, frac_5, frac_6, OP1, frac_5, frac_7, c1)



    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')