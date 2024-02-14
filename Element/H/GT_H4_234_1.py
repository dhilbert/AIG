import random

def generate():
    A = random.randint(1,20)
    B = random.randint(2,30)
    C = random.randint(1,B-1)
    D = A*B + C

    stem = "%d \\frac {%d} {%d} =" % (A,C,B)
    answer = "\\frac {%d} {%d}" % (D,B)

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')