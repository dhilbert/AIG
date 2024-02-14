import random

def generate():
    flag = random.randint(1,8)

    if flag == 1:
        # 세자리 X 두자리
        A = random.randint(10,99) * 10
        B = random.randint(1,9) * 10
        C = A*B

        stem = "%d \\times %d =" % (A,B)
        answer = "%d" % C

    if flag == 2:
        # 네자리 X 두자리
        A = random.randint(100,400) * 10
        B = random.randint(1,9) * 10
        C = A*B

        stem = "%d \\times %d =" % (A,B)
        answer = "%d" % C

    if flag == 3:
        # 세자리 X 세자리
        A = random.randint(10,40) * 10
        B = random.randint(1,9) * 100
        C = A*B

        stem = "%d \\times %d =" % (A,B)
        answer = "%d" % C

    if flag == 4:
        # 세자리 X 네자리
        A = random.randint(10,40) * 10
        B = random.randint(1,9) * 1000
        C = A*B

        stem = "%d \\times %d =" % (A,B)
        answer = "%d" % C

    if flag == 5:
        # 두자리 X 두자리
        A = random.randint(10,99)
        B = random.randint(1,9) * 10
        C = A*B

        stem = "%d \\times %d =" % (A,B)
        answer = "%d" % C

    if flag == 6:
        # 세자리 / 두자리
        while True:
            A = random.randint(10,99) * 10
            B = random.randint(1,9) * 10
            C = int(A/B)
            if A % B != 0:
                A = B*C
                break

        stem = "%d \\div %d =" % (A,B)
        answer = "%d" % C

    if flag == 7:
        # 네자리 / 두자리
        while True:
            A = random.randint(10,99) * 100
            B = random.randint(1,9) * 10
            C = int(A/B)
            if A % B != 0:
                A = B*C
                break

        stem = "%d \\div %d =" % (A,B)
        answer = "%d" % C

    if flag == 8:
        # 네자리 / 세자리
        while True:
            A = random.randint(10,99) * 100
            B = random.randint(1,5) * 100
            C = int(A/B)
            if A % B != 0:
                A = B*C
                break

        stem = "%d \\div %d =" % (A,B)
        answer = "%d" % C

    return stem, answer


if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')