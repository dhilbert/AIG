import random

def generate():
    A = random.randint(2,30)
    B = random.randint(A, 25*A)
    C = int(B/A)
    D = B - A*C

    stem = "\\frac {%d} {%d} = " % (B,A)
    if B % A == 0:
        answer = "%d" % C
    else:
        answer = "%d \\frac {%d} {%d}" % (C,D,A)

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')