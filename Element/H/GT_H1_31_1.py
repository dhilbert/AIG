import random

def generate():
    D = random.randint(1,10)
    if D < 8:
        while True:
            A = random.randint(100,999)
            B = random.randint(10,99)
            C = A*B
            if C < 30000:
                break
    else:
        A = random.randint(100,999)
        B = random.randint(10,99)
        C = A*B


    stem = """\\begin{array}{r} 
    %d \\\\
    \\times \\phantom{0} \\phantom{0} %d \\\\
    \\hline 
    \\end{array}
    """ % (A,B,)

    answer = "%d" % C

    return stem, answer