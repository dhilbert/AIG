import random

def generate():
    while True:
        A = random.randint(10,99)
        B = random.randint(10,99)
        D = random.randint(100,999)
        E = random.randint(100,999)
        S1 = random.choice([A,D])
        S2 = random.choice([B,E])

        stem = "%d \\times %d = " % (S1, S2)
        answer = "%d" % (S1*S2)
        if S1*S2 < 4000:
            break

    return stem, answer
if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')