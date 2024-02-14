import random

def generate():
    A = random.randint(1000,9999)
    B = random.randint(2,9)
    C = int(A/B)
    if A % B != 0:
        A = B*C
    
    stem = """\\require{enclose}
    \\begin{array}{r}
    %d \\enclose{longdiv}{%d} \\\\
    \\end{array}
    """ % (B,A)
    answer = "%d" % (int(A/B))

    return stem, answer
if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')