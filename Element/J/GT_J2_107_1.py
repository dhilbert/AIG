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
        OP1, OP3 = np.random.choice(['*', '//'], 2)
        OP2 = np.random.choice(['-', '+'], 1)[0]

        B = np.random.randint(2, 11)
        A = np.random.randint(2, 11) if OP1 == '*' else B * np.random.randint(2, 5)
        D = np.random.randint(2, 11)
        C = np.random.randint(2, 11) if OP2 == '*' else D * np.random.randint(2, 5)
        if B != D or A != C :
            E = eval('%s %s %s' % (A, OP1, B))
            F = eval('%s %s %s' % (C, OP3, D))
            G = eval('%s %s %s' % (E, OP2, F))
            if E < 51 and F < 51 and G < 51 and G >= 0:
                break

    OP1 = '\\times' if OP1 == '*' else '\\div'
    OP3 = '\\times' if OP3== '*' else '\\div'

    stem = '%s %s %s %s %s %s %s =' % (A, OP1, B, OP2, C, OP3, D)
    answer = '%s' % (G)
    comment ='%s %s %s %s %s %s %s = %s %s %s = %s' % (A, OP1, B, OP2, C, OP3, D, E, OP2, F, G)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')