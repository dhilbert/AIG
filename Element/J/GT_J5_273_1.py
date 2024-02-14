import numpy as np


def generate():
    while True :
        n1 = np.random.randint(1, 4)
        A = np.random.randint(1, 1000)
        if A % 10 != 0 :
            B = pow(10, n1)
            C = round(A/B, n1)
            break

    stem = '%s \\div %s = ' % (A, B)
    answer = '%s' % (C)
    comment = '%s \\div %s = %s' % (A, B, C)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')