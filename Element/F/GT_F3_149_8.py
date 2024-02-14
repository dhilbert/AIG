import random
import fractions

def generate():
    while True:
        a1 = random.randint(1,9) #백의 자리 수
        a2 = random.randint(0,9) #십의 자리 수
        a3 = random.randint(0,9) #일의 자리 수

        b1 = random.randint(1,9) #백의 자리 수
        b2 = random.randint(0,9) #십의 자리 수
        b3 = random.randint(0,9) #일의 자리 수

        if a1+b1+1 > 10 and a2+b2+1 > 10 and a3+b3 > 10:
            break
        elif a1+b1 > 10 and a2+b2 > 10 and a3+b3 > 10:
            break
        else:
            continue
            
    stem = "\\begin{array}{&} &%d%d%d \\\\ +&%d%d%d \\\\ \\hline \\end{array}" % (a1,a2,a3,b1,b2,b3)
    rseult = int("%d%d%d" % (a1,a2,a3)) + int("%d%d%d" % (b1,b2,b3))
    answer = "%d" % (rseult)

    return stem, answer

if __name__ == '__main__':
    for i in range(0,10):
        stem, answer = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')