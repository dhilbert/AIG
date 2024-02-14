import numpy as np


def generate():
    while True :
        n1 = np.random.randint(1, 4)
        n2 = 2
        A = np.random.randint(1, pow(10, n1))
        B = np.random.randint(10, pow(10, n2))
        if A % 10 != 0 and B % 10 != 0 and 10 < B < 100 :
            if B < 10 :
                C = A * B
                D = ''
                E = C
            else :
                B1, B2 = list(str(B))
                C = A * int(B2)
                D = A * int(B1)
                E = A * B

            i, j = np.random.choice([0, 1], 2)
            n1, n2 = n1 + i, n2 + j
            n3 = n1 + n2
            A_text = '0.' + '\\phantom{.}'.join(list(str(A))) if i == 0 else '0.0\\phantom{.}' + '\\phantom{.}'.join(
                list(str(A)))
            B_text = '0.' + '\\phantom{.}'.join(list(str(B))) if j == 0 else '0.0\\phantom{.}' + '\\phantom{.}'.join(
                list(str(B)))
            if 0 < n3 < 6 and C % 10 != 0 and len(A_text) > len(B_text) :
                break

    C = '\\phantom{.}'.join(list(str(C)))
    D = '\\phantom{.}'.join(list(str(D))) if D != '' else ''
    E = ['0'] * (n3-len(str(E))) + list(str(E))
    E = '0.'+'\\phantom{.}'.join(E)

    stem = '\\begin{aligned}[t]' \
           '%s \\\\' \
           '\\times \\phantom{0} \\phantom{0} %s \\\\' \
           '\\hline' \
           '\\end{aligned}' % (A_text, B_text)
    answer = '%s' % (E.replace('\\phantom{.}', ''))
    comment = '\\begin{aligned}[t]' \
              '%s \\\\' \
              '\\times \\phantom{0} \\phantom{0} %s \\\\' \
              '\\hline' \
              '%s \\\\' \
              '%s \\phantom{.} \\phantom{0}\\\\' \
              '\\hline %s \\end{aligned}' \
              '' % (A_text, B_text, C, D, E)



    return stem, answer, comment


if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')