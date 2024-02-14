import random

def generate():
    k = random.randint(1,9)
    B = random.randint(2,9)
    A = k*B
    C = int(A/B)

    stem = "%d \\div %d = " % (A,B)
    answer = "%d" % C

    return stem, answer