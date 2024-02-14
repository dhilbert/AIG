import random

def generate():
    while True:
        A = random.randint(10,99)
        B = random.randint(10,99)
        C = A*B
        if C<6000:
            break

    stem = """\\begin{array}{r} 
    %d \\\\
    \\times \\phantom{0} \\phantom{0} %d \\\\
    \\hline 
    \\end{array}
    """ % (A,B,)

    answer = "%d" % C

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')
