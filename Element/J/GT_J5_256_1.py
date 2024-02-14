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
        OP = '+' #np.random.choice(['+', '-'], 1)[0]
        A = np.random.randint(1, 100)
        B = np.random.randint(1, 100)
        if OP == '-' :
            B, A = sorted([A, B])
        C = eval('%s %s %s' % (A, OP, B))
        if A % 10 != 0 and B % 10 != 0 and C % 10 != 0:
            break

    d1 = '%s' % (round(A/10, 1))
    d2 = '%s' % (round(B/10, 1))
    d3 = '%s' % (round(C/10, 1))

    stem = '%s %s %s =' % (d1, OP, d2)
    answer = '%s' % (d3)
    comment = '%s %s %s = %s' % (d1, OP, d2, d3)

    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')