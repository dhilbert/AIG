import random

def generate():
    A = random.randint(1000,9999)
    B = random.randint(2,9)
    C = A*B

    stem = """\\begin{array}{r} 
    %d \\\\
    \\times \\phantom{0} \\phantom{0} \\phantom{0} \\phantom{0} %d \\\\
    \\hline 
    \\end{array}
    """ % (A, B, )
    answer = "{C}".format(C=C)

    return stem, answer