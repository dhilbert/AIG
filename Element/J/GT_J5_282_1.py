import numpy as np


def generate():
    while True :
        n1 = np.random.randint(1, 3)
        B = np.random.randint(pow(10, n1), pow(10, n1+1))
        C = np.random.randint(2, 10)
        A = B * C
        D = pow(10, n1)
        if A % 10 != 0 and B % 10 != 0 and (B > 100 and B % 5 == 0 or B % 2 == 0):
            break

    d1 = '%s' % (round(A/D, n1))
    d2 = '%s' % (round(B/D, n1))


    stem = '%s \\div %s = ' % (d1, C)
    answer = '%s' % (d2)
    comment = '%s \\div %s = %s \\rightarrow %s \\div %s = %s' % (A, C, B, d1, C, d2)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')