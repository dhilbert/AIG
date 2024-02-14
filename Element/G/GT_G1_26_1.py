import random

def generate():
    A = random.choice([6,7])
    B = random.randint(0,9)
    C = A*B
    
    stem = "{A} \\times {B} = ".format(A=A, B=B)
    answer = "{C}".format(C=C)

    return stem, answer