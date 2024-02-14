import random

def generate():
    A = random.randint(11,89)
    B = random.randint(100,999)
    C = random.randint(1000,9999)
    flag = random.randint(1,3)

    if flag == 1:
        q = int(B/A)
        r = B - A*q

        stem = """\\require{enclose}
        \\begin{array}{r}
        %d \\enclose{longdiv}{%d} \\\\
        \\end{array}
        """ % (A,B)
        if r == 0:
            answer = "%d" % q
        else:
            answer = "%d ⋯ %d" % (q,r)

    if flag == 2:
        q = int(C/A)
        r = C - A*q

        stem = """\\require{enclose}
        \\begin{array}{r}
        %d \\enclose{longdiv}{%d} \\\\
        \\end{array}
        """ % (A,C)
        if r == 0:
            answer = "%d" % q
        else:
            answer = "%d ⋯ %d" % (q,r)

    if flag == 3:
        q = int(C/B)
        r = C - B*q

        stem = """\\require{enclose}
        \\begin{array}{r}
        %d \\enclose{longdiv}{%d} \\\\
        \\end{array}
        """ % (B,C)
        if r == 0:
            answer = "%d" % q
        else:
            answer = "%d ⋯ %d" % (q,r)

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')