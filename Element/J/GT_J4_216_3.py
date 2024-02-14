#code by 강효준
import random
import fractions

denominator = 15 #분모의 범위
numerator = 20 #분자의 범위

#가분수를 대분수로 고치는 함수
def impro2lage(n,d):
    if n%d == 0:
        answer = str(int(n/d))
    elif n > d:
        pre = 1
        while True:
            n = n - d
            if n > d:
                pre += 1
            else:
                gcd = fractions.gcd(d,n)
                if gcd == 1:
                    answer = "%d \\frac {%d} {%d}" % (pre,n,d)
                else:
                    answer = "%d \\frac {%d} {%d}" % (pre,n/gcd,d/gcd)
                break
    else:
        gcd = fractions.gcd(n,d)
        if gcd == 1:
            answer = "\\frac {%d} {%d}" % (n,d)
        else:
            answer = "\\frac {%d} {%d}" % (n/gcd,d/gcd)

    return answer

#분수 만드는 함수
def make_fractioin():
    while True:
        n = random.randint(1,numerator)
        d = random.randint(2,denominator)
        if fractions.gcd(d,n) == 1 and n < d:
            string, frac = "\\frac {%d}{%d}"%(n,d), fractions.Fraction(n,d)
            break
    return string, frac

def generate():
    while True:
        mode = random.randint(0,3)
        A, a = make_fractioin()
        B, b = make_fractioin()

        an = a.numerator
        ad = a.denominator
        bn = b.numerator
        bd = b.numerator

        if A != B:
            if mode == 0:
                stem = A + "\\div" + "\\left( \\phantom{0}\\phantom{0} \\right)" + "=" + B
                result = 1/b * a
                answer = impro2lage(result.numerator, result.denominator)

                if result.numerator < result.denominator:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\div" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\times" + "\\frac {%d}{%d}"%(b.denominator,b.numerator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator)
                else:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\div" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\times" + "\\frac {%d}{%d}"%(b.denominator,b.numerator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator) \
                            + "=" + answer
                break
            elif mode == 1:
                stem = "\\left( \\phantom{0}\\phantom{0} \\right)" + "\\div" + A + "=" + B
                result = b * a
                answer = impro2lage(result.numerator, result.denominator)

                if result.numerator < result.denominator:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) + "\\times" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator)
                else:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) + "\\times" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator) \
                            + "=" + answer
                break
            elif mode == 2:
                stem = B + "=" + A + "\\div" + "\\left( \\phantom{0}\\phantom{0} \\right)"
                result = 1/b * a
                answer = impro2lage(result.numerator, result.denominator)

                if result.numerator < result.denominator:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\div" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\times" + "\\frac {%d}{%d}"%(b.denominator,b.numerator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator)
                else:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\div" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) + "\\times" + "\\frac {%d}{%d}"%(b.denominator,b.numerator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator) \
                            + "=" + answer
                break
            else:
                stem = B + "=" + "\\left( \\phantom{0}\\phantom{0} \\right)" + "\\div" + A
                result = b * a
                answer = impro2lage(result.numerator, result.denominator)
                
                if result.numerator < result.denominator:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) + "\\times" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator)
                else:
                    comment = "\\left( \\phantom{0}\\phantom{0} \\right)" \
                            + "=" + "\\frac {%d}{%d}"%(b.numerator,b.denominator) + "\\times" + "\\frac {%d}{%d}"%(a.numerator,a.denominator) \
                            + "=" + "\\frac {%d}{%d}"%(result.numerator,result.denominator) \
                            + "=" + answer
                break

    return stem, answer, comment

if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')