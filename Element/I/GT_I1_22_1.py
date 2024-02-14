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


def generate():
    while True:
        A = np.random.randint(2, 11)
        B = np.random.randint(1, A)
        C = np.random.randint(2, 10)
        if is_gcd(A, B) :
            D = A * C
            E = B * C
            if D < 51 and E < 51 :
                break

    stem = '\\frac {%s}{%s} = \\frac {\\left( \\quad \\right)}{%s}' % (B, A, D)
    answer = '%s' % (E)
    comment = '\\frac {%s}{%s} = \\frac {%s \\times %s}{%s \\times %s} = \\frac {%s}{%s}' % (B, A, B, C, A, C, E, D)

    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')