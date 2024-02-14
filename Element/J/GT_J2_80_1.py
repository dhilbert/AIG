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


def generate():
    while True :
        A = np.random.randint(1, 100)
        B = np.random.randint(2, 100)
        AB = get_gcd(A, B)
        if AB != 1 :
            A1 = A // AB
            B1 = B // AB
            if A1 < 51 and B1 < 51 and A1 // B1 < 5 and A1 % B1 != 0 :
                break

    frac_1 = get_fraction(0, A1, B1)
    frac_2 = get_fraction(0, A1, B1, True)

    c1 = ' = %s' % (frac_2) if frac_1 != frac_2 else ''
    stem = '\\frac {%s}{%s} = ' % (A, B)
    answer = '%s' % (frac_2)
    comment = '\\frac {%s}{%s} = \\frac {%s \\div %s}{%s \\div %s} = %s%s' % (A, B, A, AB, B, AB, frac_1, c1)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')