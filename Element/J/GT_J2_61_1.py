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
        OP1 = np.random.choice(['-', '+'], 1)[0]
        OP2 = np.random.choice(['*', '//'], 1)[0]
        A, B = np.random.randint(1, 21, 2)
        AB = eval('%s %s %s' % (A, OP1, B))
        if AB > 0 :
            mode = np.random.randint(0, 2)
            exp_1 = '\\left( %s %s %s \\right)' % (A, OP1, B)
            if mode == 0 :
                C = np.random.randint(2, 11) if OP2 == '*' else np.random.choice(get_divisor(AB), 1)[0]

                c1 = '%s %s %s' % (exp_1, OP2, C)
                c2 = '%s %s %s' % (AB, OP2, C)
                D = eval(c2)
                if (OP2 == '//' and AB % C == 0 and C != 1) or (OP2 == '*' and D < 101) :
                    break
            else :
                C = np.random.randint(2, 11) if OP2 == '*' else AB * np.random.randint(2, 5)
                c1 = '%s %s %s' % (C, OP2, exp_1)
                c2 = '%s %s %s' % (C, OP2, AB)
                D = eval(c2)
                if (OP2 == '//' and AB % C == 0 and C != 1) or (OP2 == '*' and D < 101):
                    break

    c1 = c1.replace('//', '\div').replace('*', '\\times')
    c2 = c2.replace('//', '\div').replace('*', '\\times')
    stem = '%s =' % (c1)
    answer = '%s' % (D)
    comment = '%s = %s = %s' % (c1, c2, D)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')