import random
import fractions
#두 수의 최대 공약수를 구하고 약분하여라
def generate():
    while True:
        A = random.randint(2,99)
        B = random.randint(2,99)
        if A != B:
            gcd = fractions.gcd(A,B)
            if gcd > 1:
                if A < B:
                    stem = "\\left(%d,%d\\right) \\phantom{0} \\rightarrow \\phantom{0} \\Box \\phantom{0} \\phantom{0} \\frac {%d} {%d} =" % (A,B,A,B)
                    answer = "%d, \\frac {%d} {%d}" % (gcd, A/gcd, B/gcd)
                    break
                else :
                    stem = "\\left(%d,%d\\right) \\phantom{0} \\rightarrow \\phantom{0} \\Box \\phantom{0} \\phantom{0} \\frac {%d} {%d} =" % (B,A,B,A)
                    answer = "%d, \\frac {%d} {%d}" % (gcd, B/gcd, A/gcd)
                    break

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')