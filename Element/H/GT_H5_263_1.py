import random
import fractions
#H5_263_1 두 수의 최대 공약수로 약분하여라
def generate():
    while True:
        A = random.randint(2,100)
        B = random.randint(2,100)
        if A != B:
            gcd = fractions.gcd(A,B)
            if gcd > 1:
                if A < B:
                    stem = "\\frac {%d} {%d} = " % (A,B)
                    answer = "\\frac {%d} {%d}" % (A/gcd, B/gcd)
                    break
                else :
                    stem = "\\frac {%d} {%d} = " % (B,A)
                    answer = "\\frac {%d} {%d}" % (B/gcd, A/gcd)
                    break

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')