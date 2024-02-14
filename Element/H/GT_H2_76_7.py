import random

def generate():
    while True:
        A = random.randint(10,99)
        B = random.randint(10,99)
        D = random.randint(100,999)
        E = random.randint(100,999)
        S1 = random.choice([A,D])
        S2 = random.choice([B,E])

        stem = """\\begin{array}{r} 
        %d \\\\
        \\times \\phantom{0} \\phantom{0} %d \\\\
        \\hline 
        \\end{array}
        """ % (S1, S2)
        answer = "%d" % (S1*S2)
        if S1*S2 < 4000:
            break

    return stem, answer