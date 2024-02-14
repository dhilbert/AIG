import random

def generate():
    while True:
        A = random.randint(100,999)
        B = random.randint(100,999)
        C = A*B
        if C<500000:
            break

    stem = """\\begin{array}{r} 
    %d \\\\
    \\times \\phantom{0} \\phantom{0} %d \\\\
    \\hline 
    \\end{array}
    """ % (A,B,)

    answer = "%d" % C

    return stem, answer