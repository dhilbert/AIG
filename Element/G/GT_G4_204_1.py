import random

def generate():
    while True:
        A = random.randint(3,99)
        B = random.randint(2,9)
        if A%B!=0:
            break
    C = int(A/B)
    D = A - B*C

    stem = "%d \\div %d = " % (A,B)
    answer = "%d ⋯ %d" % (C,D)

    return stem, answer