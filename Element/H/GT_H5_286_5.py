import random
import fractions
#H5_286_5 분수 덧셈
def generate():
    denominator = 11 #분모의 범위
    numeator = 10 #분자의 범위
    while True:
        flag = random.randint(2,4)
        if flag == 2:
            #분모
            A = random.randint(2,denominator) 

            #분자
            B = random.randint(1,numeator)
            C = random.randint(1,numeator)

            if A > B and A > C and fractions.gcd(A,B)==1 and fractions.gcd(A,C)==1:
                stem = "\\frac {%d} {%d} + \\frac {%d} {%d} = " % (B,A,C,A)
                if (B+C)%A == 0:
                    answer = str(int((B+C)/A))
                elif B+C > A:
                    top = B+C
                    pre = 1
                    while True:
                        top = top - A
                        if  top > A:
                            pre += 1
                        else:
                            gcd = fractions.gcd(A,top)
                            if gcd == 1:
                                answer = "%d \\frac {%d} {%d}" % (pre,top,A)
                            else:
                                answer = "%d \\frac {%d} {%d}" % (pre,top/gcd,A/gcd)
                            break
                else:
                    gcd = fractions.gcd(A,B+C)
                    if gcd == 1:
                        answer = "\\frac {%d} {%d}" % (B+C,A)
                    else:
                        answer = "\\frac {%d} {%d}" % ((B+C)/gcd,A/gcd)
                break
        elif flag == 3:
            #분모
            A = random.randint(2,denominator) 

            #분자
            B = random.randint(1,numeator)
            C = random.randint(1,numeator)
            D = random.randint(1,numeator)

            if A > B and A > C and A > D and fractions.gcd(A,B)==1 and fractions.gcd(A,C)==1 and fractions.gcd(A,D)==1:
                stem = "\\frac {%d} {%d} + \\frac {%d} {%d} + \\frac {%d} {%d} =" % (B,A,C,A,D,A)
                if (B+C+D)%A == 0:
                    answer = str(int((B+C+D)/A))
                elif B+C+D > A:
                    top = B+C+D
                    pre = 1
                    while True:
                        top = top - A
                        if  top > A:
                            pre += 1
                        else:
                            gcd = fractions.gcd(A,top)
                            if gcd == 1:
                                answer = "%d \\frac {%d} {%d}" % (pre,top,A)
                            else:
                                answer = "%d \\frac {%d} {%d}" % (pre,top/gcd,A/gcd)
                            break
                else:
                    gcd = fractions.gcd(A,B+C+D)
                    if gcd == 1:
                        answer = "\\frac {%d} {%d}" % (B+C+D,A)
                    else:
                        answer = "\\frac {%d} {%d}" % ((B+C+D)/gcd,A/gcd)

                break
        else:
            #분모
            A = random.randint(2,denominator) 

            #분자
            B = random.randint(1,numeator)
            C = random.randint(1,numeator)
            D = random.randint(1,numeator)
            E = random.randint(1,numeator)

            if A > B and A > C and A > D and A > E and fractions.gcd(A,B)==1 and fractions.gcd(A,C)==1 and fractions.gcd(A,D)==1 and fractions.gcd(A,E)==1:
                stem = "\\frac {%d} {%d} + \\frac {%d} {%d} + \\frac {%d} {%d} + \\frac {%d} {%d} = " % (B,A,C,A,D,A,E,A)
                if (B+C+D+E)%A == 0:
                    answer = str(int((B+C+D+E)/A))
                elif B+C+D+E > A:
                    top = B+C+D+E
                    pre = 1
                    while True:
                        top = top - A
                        if  top > A:
                            pre += 1
                        else:
                            gcd = fractions.gcd(A,top)
                            if gcd == 1:
                                answer = "%d \\frac {%d} {%d}" % (pre,top,A)
                            else:
                                answer = "%d \\frac {%d} {%d}" % (pre,top/gcd,A/gcd)
                            break
                else:
                    gcd = fractions.gcd(A,B+C+D+E)
                    if gcd == 1:
                        answer = "\\frac {%d} {%d}" % (B+C+D+E,A)
                    else:
                        answer = "\\frac {%d} {%d}" % ((B+C+D+E)/gcd,A/gcd)
                break
    return stem, answer

if __name__ == '__main__':
    stem, answer = generate()
    print(stem.replace('\\\\', '\\') + '\\\\')
    print(answer.replace('\\\\', '\\') + '\\\\')