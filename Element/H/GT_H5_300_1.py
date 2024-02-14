import random
import fractions
#H5_299_1 분수의 덧셈과 뺄셈 종합

denominator = 11 #분모의 범위
numeator = 10 #분자의 범위

def make_fractioin(d):
    flag = random.randint(0,2)

    #자연수
    if flag == 0:
        a = random.randint(1,9)
        return str(a), int(fractions.Fraction(a*d,d))
    #분수
    elif flag == 1:
        while True:
            n = random.randint(1,numeator)
            if d > n and fractions.gcd(d,n) == 1:
                return "\\frac {%d} {%d}" % (n,d), fractions.Fraction(n,d)
                break
    #대분수        
    else:
        pre = random.randint(1,9)
        while True:
            n = random.randint(1,numeator)
            if d > n and fractions.gcd(d,n) == 1:
                return "%d \\frac {%d} {%d}" % (pre,n,d), fractions.Fraction(pre*d+n,d)
                break

#가분수를 대분수로 바꾸는 함수
def impro2lage(result,d):
    if result%d == 0:
        answer = str(int(result/d))
    elif result > d:
        pre = 1
        while True:
            result = result - d
            if result > d:
                pre += 1
            else:
                gcd = fractions.gcd(d,result)
                if gcd == 1:
                    answer = "%d \\frac {%d} {%d}" % (pre,result,d)
                else:
                    answer = "%d \\frac {%d} {%d}" % (pre,result/gcd,d/gcd)
                break
    else:
        gcd = fractions.gcd(result,d)
        if gcd == 1:
            answer = "\\frac {%d} {%d}" % (result,d)
        else:
            answer = "\\frac {%d} {%d}" % (result/gcd,d/gcd)

    return answer

def generate():
    op_flag = random.randint(0,3)
    d = random.randint(2,15)
    while True:
        A, a1 = make_fractioin(d)
        B, a2 = make_fractioin(d)
        C, a3 = make_fractioin(d)

        if (type(a1) and type(a2) and type(a3)) is int:
            continue
        else:
            if op_flag == 0:
                stem = A + "+" + B + "+" + C +  "= "
                result = a1 + a2 + a3
                answer = impro2lage(result.numerator,result.denominator)
                break
            elif op_flag == 1:
                stem = A + "+" + B + "-" + C + "= "
                result = a1 + a2 - a3
                if a2 < a3 and result > 0:
                    answer = impro2lage(result.numerator,result.denominator)
                    break
            elif op_flag == 2:
                stem = A + "-" + B + "+" + C + "= "
                result = a1 - a2 + a3
                if a1 > a2 and result > 0:
                    answer = impro2lage(result.numerator,result.denominator)
                    break
            else:
                stem = A + "-" + B + "-" + C + "= "
                result = a1 - a2 - a3
                if result > 0:
                    answer = impro2lage(result.numerator,result.denominator)
                    break

    return stem, answer

if __name__ == '__main__':
    stem, answer= generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')