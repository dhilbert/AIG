import random

def generate():
    flag = random.randint(1,3)
    
    while True:

        A = random.randint(10,99)
        B = random.randint(10,99)
        C = random.randint(10,99)
        D = random.randint(100,999)
        E = random.randint(100,999)
        F = random.randint(100,999)
        G = random.randint(1000,5000)
        H = random.randint(1000,5000)
        I = random.randint(1000,5000)
        S1 = random.choice([A,D,G])
        S2 = random.choice([B,E,H])
        S3 = random.choice([C,F,I])
        
        # 두 수 덧셈
        if flag == 1:
            stem = """\\begin{array}{r}
            %d \\\\
            + \\phantom{0} \\phantom{0} %d  \\\\
            \\hline 
            \\end{array}
            """ % (S1,S2)
            answer = "%d" % (S1 + S2)
            break
        
        # 두 수 뺄셈
        if flag == 2:
            if S1 - S2 > 0:
                stem = """\\begin{array}{r}
                %d \\\\
                - \\phantom{0} \\phantom{0} %d  \\\\
                \\hline 
                \\end{array}
                """ % (S1,S2)
                answer = "%d" % (S1 - S2)
                break

        # 세 수 덧셈
        if flag == 3:
            stem = """\\begin{array}{r}
            %d \\\\
            \\phantom{0} \\phantom{0} %d  \\\\
            + \\phantom{0} \\phantom{0} %d  \\\\
            \\hline 
            \\end{array}
            """ % (S1, S2, S3)
            answer = "%d" % (S1+S2+S3)
            break

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')