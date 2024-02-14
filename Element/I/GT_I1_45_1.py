import numpy as np


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


def generate():
    while True :
        A = np.random.randint(2, 10)
        B, C = np.random.choice(np.arange(2, 10), 2, False) * np.reshape([A, A], -1)
        if B % C != 0 and C % B != 0 :
            D = np.random.randint(1, B)
            E = np.random.randint(1, C)
            if get_gcd(B, D) == 1 and get_gcd(C, E) == 1 :
                F = get_lcm(B, C)
                G = D * (F // B)
                H = E * (F // C)
                I = G + H
                J = I % F
                if F < 101 and I < 101 and (I==F or get_gcd(J, F) == 1) and I // F < 2 :
                    K, L = np.random.randint(0, 5, 2)
                    break

    frac_1 = get_fraction(K, D, B)
    frac_2 = get_fraction(L, E, C)
    frac_3 = get_fraction(K, G, F)
    frac_4 = get_fraction(L, H, F)
    frac_5 = get_fraction(K+L, I, F)
    frac_6 = get_fraction(K+L, I, F, True)
    c1 = '' if K + L == 0 else '%s ' % (K+L)
    c2 = '' if frac_5 == frac_6 else ' = %s' % (frac_6)
    stem = '%s + %s =' % (frac_1, frac_2)
    answer = '%s' % (frac_6)
    comment = '%s + %s = %s + %s = %s\\frac {%s + %s}{%s} = %s%s' \
              '' % (frac_1, frac_2, frac_3, frac_4, c1, G, H, F, frac_5, c2)

    return stem, answer, comment