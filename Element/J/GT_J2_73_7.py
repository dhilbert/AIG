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
        OP1, OP2 = np.random.choice(['+', '-'], 2)
        OP3 = np.random.choice(['*', '//'], 1)[0]
        A, B, C, D = np.random.randint(2, 21, 4)
        E = eval('%d %s %d' % (A, OP1, B))
        F = eval('%d %s %d' % (C, OP2, D))
        if E > 1 and F > 1 :
            G = int(eval('%d %s %d' % (E, OP3, F)))
            if (OP3 == '//' and E > F and F in get_divisor(E)) :
                break
            elif OP3 == '*' and G < 101 :
                break


    OP3 = '\\times' if OP3 == '*' else '\\div'

    stem = '\\left( %s %s %s \\right) %s \\left( %s %s %s \\right) =' % (A, OP1, B, OP3, C, OP2, D)
    answer = '%s' % (G)
    comment = '\\left( %s %s %s \\right) %s \\left( %s %s %s \\right) = %s %s %s = %s' \
              '' % (A, OP1, B, OP3, C, OP2, D, E, OP3, F, G)


    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')