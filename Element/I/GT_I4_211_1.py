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


def generate():
    while True :
        B, D = np.random.choice(np.arange(2, 10), 2, False)
        A = np.random.randint(1, B)
        C = np.random.randint(1, D)
        E, F = np.random.randint(0, 4, 2)
        G = E * B + A
        H = F * D + C
        I = G * D
        J = B * H
        if is_gcd(A, B) and is_gcd(C, D) and is_gcd(I, J) and I < 301 and J < 301 and I // J < 10 and I % J != 0:

            break

    frac_1 = get_fraction(E, A, B)
    frac_2 = get_fraction(F, C, D)
    frac_3 = get_fraction(0, G, B)
    frac_4 = get_fraction(0, H, D)
    frac_5 = get_fraction(0, D, H)
    frac_6 = get_fraction(0, I, J)
    frac_7 = get_fraction(0, I, J, True)

    c1 = '= %s \\div %s ' % (frac_3, frac_4) if frac_1 != frac_3 or frac_2 != frac_4 else ''
    c2 = ' = %s' % (frac_7) if frac_6 != frac_7 else ''

    stem = '%s \\div %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_7)
    comment = '%s \\div %s %s= %s \\times %s = %s%s' % (frac_1, frac_2, c1, frac_3, frac_5, frac_6, c2)


    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')