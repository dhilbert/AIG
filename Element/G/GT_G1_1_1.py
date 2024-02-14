import random

def generate():
    A = random.choice([2,3])
    B = random.randint(0,9)
    C = A*B
    
    stem = "{A} \\times {B} = ".format(A=A, B=B)
    answer = "{C}".format(C=C)

    return stem, answer

if __name__ == '__main__':
    for i in range(0,10):
        stem, answer = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')
        print("\n\n")