import numpy as np


def generate():
    while True :
        n1 = np.random.randint(1, 5)
        n2 = np.random.randint(1, 5)
        A = np.random.randint(1, 100)
        if A % 10 != 0 :
            B = pow(10, n2)
            C = pow(10, n1)
            n3 = -n1 + n2
            D = pow(10, n3)
            break

    d1 = '%s' % (round(A/C, n1))

    stem = '%s \\times %s = ' % (d1, B)
    answer = '%s' % (round(A * D, -n3))
    comment = '%s \\times %s = %s' % (d1, B, round(A * D, -n3))


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')