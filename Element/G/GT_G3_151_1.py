import random

def generate():
    while True:
        A = random.randint(10,99)
        B = random.randint(10,99)
        C = A*B
        if C<1000:
            break

    stem = """\\begin{array}{r} 
    %d \\\\
    \\times \\phantom{0} \\phantom{0} %d \\\\
    \\hline 
    \\end{array}
    """ % (A, B, )
    answer = "{C}".format(C=C)

    return stem, answer