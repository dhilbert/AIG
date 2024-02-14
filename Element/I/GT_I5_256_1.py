import numpy as np


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



def generate():
    while True :
        A = np.random.randint(1, 5)
        B = pow(10, A)
        C = np.random.randint(1, pow(10, A))
        D = get_gcd(B, C)
        B1 = B // D
        C1 = C // D
        if C % 10 != 0 :
            break

    frac_1 = get_fraction(0, C, B)
    frac_2 = get_fraction(0, C1, B1)
    c1 = ' = %s' % (frac_2) if frac_1 != frac_2 else ''

    stem = '%s =' % (round(C/B, A))
    answer = '%s' % (frac_2)
    comment = '%s = %s%s' % (round(C/B, A), frac_1, c1)


    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')