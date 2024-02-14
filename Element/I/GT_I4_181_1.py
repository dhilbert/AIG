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
        E = B * D
        F = A * C
        if is_gcd(A, B) and is_gcd(C, D) and is_gcd(E, F) and E < 301 and F < 301:
            G, H = np.random.randint(0, 4, 2)
            I = G * B + A
            J = H * D + C
            K = I * J
            if is_gcd(I, D) and is_gcd(J, B) and K < 301 and is_gcd(K, E) and K // E < 5 and K % E != 0 :
                break


    frac_1 = get_fraction(G, A, B)
    frac_2 = get_fraction(H, C, D)
    frac_3 = get_fraction(0, I, B)
    frac_4 = get_fraction(0, J, D)
    frac_5 = get_fraction(0, K, E)
    frac_6 = get_fraction(0, K, E, True)
    c1 = '= %s \\times %s' % (frac_3, frac_4) if frac_3 != frac_1 or frac_2 != frac_4 else ''
    c2 = '= \\frac {%s \\times %s}{%s \\times %s}' % (I, J, B, D)
    c3 = ' = %s' % (frac_6) if frac_5 != frac_6 else ''


    stem = '%s \\times %s = ' % (frac_1, frac_2)
    answer = '%s' % (frac_6)
    comment = '%s \\times %s %s %s = %s%s' \
              '' % (frac_1, frac_2, c1, c2, frac_5, c3)

    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')