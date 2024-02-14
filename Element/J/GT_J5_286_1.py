import numpy as np


def generate():
    while True :
        A = np.random.randint(10, 1000)
        B = np.random.randint(10, 100)
        if A % 10 != 0 and B % 10 != 0 :
            B1, B2 = list(str(B))
            n1 = np.random.randint(0, 2) if A < 100 else np.random.randint(0, 3)
            n2 = np.random.randint(0, 2)
            n3 = n1 + n2
            C = A * int(B2)
            D = A * int(B1)
            F = A * B
            if C < 1000 and D < 1000 and n3 > 0 and F < 10000 and C % 10 != 0 :
                break

    AP1 = '.' if n1 == 2 else '\\phantom{.}'
    AP2 = '.' if n1 == 1 else '\\phantom{.}'

    A_text = '%s'.join(list(str(A)))
    A_text = A_text % (AP2) if A < 100 else A_text % (AP1, AP2)

    BP = '\\phantom{.}' if n2 == 0 else '.'
    B_text = '%s%s%s' % (B1, BP, B2)

    C = '\\phantom{.}'.join(list(str(C)))
    D = '\\phantom{.}'.join(list(str(D)))

    F = '\\phantom{.}'.join(list(str(F)[:-n3])) + '.' + '\\phantom{.}'.join(list(str(F)[-n3:]))

    stem = '\\begin{aligned}[t]' \
           '%s \\\\' \
           '\\times \\phantom{0} \\phantom{0} %s \\\\' \
           '\\hline' \
           '\\end{aligned}' % (A_text, B_text)
    answer = '%s' % (F.replace('\\phantom{.}', ''))
    comment = '\\begin{aligned}[t]' \
              '%s \\\\' \
              '\\times \\phantom{0} \\phantom{0} %s \\\\' \
              '\\hline' \
              '%s\\\\' \
              '%s\\phantom{.}\\phantom{0}\\\\' \
              '\\hline' \
              '%s' \
              '\\end{aligned}' \
              '' % (A_text, B_text, C, D, F)



    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')