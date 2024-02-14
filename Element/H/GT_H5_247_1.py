import random
import fractions
#H5_247_1 다음 분수를 약분하여 기약분수로 나타내어라
# origin = "\\frac {2} {6} ="
def generate():
    
    A = random.randint(2,20)
    while True:
        B = random.randint(1,80)
        C = random.randint(2,80)
        if B != C and B < C:
            if B%A==0 and C%A==0:
                break
    
    a = fractions.Fraction(B,C)
    stem = "\\frac {%d} {%d} = " % (B, C)
    answer = "\\frac {%d} {%d}" % (a.numerator, a.denominator)

    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')