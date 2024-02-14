import random

def generate():
    A = random.randint(2,9)
    B = random.randint(10,99)
    C = int(B/A)

    stem = """\\require{enclose}
    \\begin{array}{r}
    %d \\enclose{longdiv} {%d} \\\\
    \\end{array}
    """ % (A,B,)
    if B%A == 0:
        answer = "%d" % C
    else:
        D = B - A*C
        answer = "%d ⋯ %d" % (C,D)

    return stem, answer

if __name__ == '__main__':
    for i in range(0,10):
        stem, answer = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')
        print("\n\n")