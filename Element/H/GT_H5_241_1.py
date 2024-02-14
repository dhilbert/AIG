import random
import fractions
#H5_247_1 다음 분수를 N으로 약분하여라
# origin = "\\frac {2} {4} ="
def generate():
    A = random.randint(2,7)
    print(A)
    while True:
        B = random.randint(1,40)
        C = random.randint(2,50)
        if B < C:
            if B%A==0 and C%A==0 and fractions.gcd(B/A, C/A) == 1:
                break
    
    a = fractions.Fraction(B,C)
    stem = "\\frac {%d} {%d} = " % (B, C)
    answer = "\\frac {%d} {%d}" % (a.numerator, a.denominator)

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')