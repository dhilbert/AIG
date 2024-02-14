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
    while True:
        A, B = np.random.choice(np.arange(1, 21), 2, False)
        C = np.random.randint(2, 21)
        frac_1 = get_fraction(0, A, C, True)
        frac_2 = get_fraction(0, B, C, True)
        if is_gcd(A, C) and is_gcd(B, C) and frac_1 != frac_2 :
            I1 = A // C
            I2 = B // C
            I = I1 + I2
            A1 = A % C
            B1 = B % C
            D = A + B
            D1 = A1 + B1
            if A1 != 0 and B1 != 0 and is_gcd(D, C):
                break

    frac_5 = get_fraction(0, D1, C)
    frac_6 = get_fraction(0, D1, C, True)
    frac_7 = get_fraction(0, D, C)
    frac_8 = get_fraction(0, D, C, True)

    if I1 != 0 and I2 != 0 :
        c1 = '\\left( %s + %s \\right) + \\frac {%s + %s}{%s}' % (I1, I2, A1, B1, C)
        c2 = '%s + %s' % (I, frac_5)
        c3 = ' = %s + %s' % (I, frac_6) if frac_5 != frac_6 else ''
        c4 = ' = %s' % (frac_8)
    elif I1 != 0 :
        c1 = '%s + \\frac {%s + %s}{%s}' % (I1, A1, B1, C)
        c2 = '%s + %s' % (I, frac_5)
        c3 = ' = %s + %s' % (I, frac_6) if frac_5 != frac_6 else ''
        c4 = ' = %s' % (frac_8)
    elif I2 != 0 :
        c1 = '%s + \\frac {%s + %s}{%s}' % (I2, A1, B1, C)
        c2 = '%s + %s' % (I, frac_5)
        c3 = ' = %s + %s' % (I, frac_6) if frac_5 != frac_6 else ''
        c4 = ' = %s' % (frac_8)
    else :
        c1 = '\\frac {%s + %s}{%s}' % (A1, B1, C)
        c2 = '%s' % (frac_7)
        c3 = ' = %s' % (frac_8) if frac_7 != frac_8 else ''
        c4 = ''

    stem = '%s + %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_8)
    comment = '%s + %s = %s = %s%s%s' % (frac_1, frac_2, c1, c2, c3, c4)

    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')