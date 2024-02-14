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


def generate():
    while True :
        OP1 = np.random.choice(['+', '-'], 1)[0]
        OP2 = np.random.choice(['\\times', '\\div'], 1)[0]
        A = np.random.randint(1, 21)
        if OP2== '\\div' :
            n = np.random.randint(2, 6)
            C = np.random.randint(2, 11)
            B = C * n
            D = eval('%s %s %s' % (A, OP1, n))
            if 0 < D < 51 :
                break
        else :
            B, C = np.random.randint(2, 11, 2)
            n = B * C
            D = eval('%s %s %s' % (A, OP1, n))
            if 0 < D < 51 :
                break

    stem = '%s %s %s %s %s =' % (A, OP1, B, OP2, C)
    answer = '%s' % (D)
    comment = '%s %s %s %s %s = %s %s %s = %s' % (A, OP1, B, OP2, C, A, OP1, n, D)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')