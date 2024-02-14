import random
import fractions

def get_lcm(a,b):
    gcd = fractions.gcd(a,b)
    if a == b:
        return a
    else:
        return a*b // gcd

def generate():
    divisor = []
    while True:
        A = random.randint(2,15)
        B = random.randint(2,15)
        C = random.randint(2,15)

        if A != B and B != C and C != A:
            break

    gcd1 = fractions.gcd(A,B)
    gcd2 = fractions.gcd(B,C)
    gcd3 = fractions.gcd(A,C)
    lcm = get_lcm(get_lcm(A,B),C)

    stem = "\\left(%d, %d, %d\\right)\\rightarrow \\Box"%(A,B,C)
    answer = str(lcm)
    comment = "\\begin{array}{&}"

    if gcd1 == 1 and gcd2 == 1 and gcd3 == 1:
        #comment = "$%d,%d,%d$의 공약수가 1뿐이므로 최소공배수는 세수의 곱인 $%d \\times %d \\times %d = %d$입니다."%(A,B,C,A,B,C,lcm)
        comment = ""
    else:
        while True:
            gcd1 = fractions.gcd(A,B)
            gcd2 = fractions.gcd(B,C)
            gcd3 = fractions.gcd(A,C)
            for i in range(2,99):
                if A%i == 0 and B%i == 0 and C%i == 0:
                    divisor.append(i)
                    if A >=10 and B >= 10 and C >= 10:
                        comment += "%d \\begin{array}{&})%d &%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B >= 10 and C >= 10) or (A >= 10 and B < 10 and C >= 10) or (A >= 10 and B >= 10 and C < 10):
                        if A < 10 or B < 10:
                            comment += "%d \\begin{array}{&})%d &%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                        else:
                            comment += "%d \\begin{array}{&})%d &%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B < 10 and C >= 10) or (A >= 10 and B < 10 and C < 10) or (A < 10 and B >= 10 and C < 10):
                        comment += "%d \\begin{array}{&})%d &%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    else:
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\phantom{0} \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    A = A/i
                    B = B/i
                    C = C/i
                    break

                elif A%i == 0 and B%i == 0 and C%i != 0:
                    divisor.append(i)
                    if A >=10 and B >= 10 and C >= 10:
                        comment += "%d \\begin{array}{&})%d &%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B >= 10 and C >= 10) or (A >= 10 and B < 10 and C >= 10) or (A >= 10 and B >= 10 and C < 10):
                        if A < 10 or B < 10:
                            comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                        else:
                            comment += "%d \\begin{array}{&})%d &%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B < 10 and C >= 10) or (A >= 10 and B < 10 and C < 10) or (A < 10 and B >= 10 and C < 10):
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    else:
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\phantom{0} \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    A = A/i
                    B = B/i
                    break
                
                elif A%i != 0 and B%i == 0 and C%i == 0:
                    divisor.append(i)
                    if A >=10 and B >= 10 and C >= 10:
                        comment += "%d \\begin{array}{&})%d &%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B >= 10 and C >= 10) or (A >= 10 and B < 10 and C >= 10) or (A >= 10 and B >= 10 and C < 10):
                        if A < 10 or B < 10:
                            comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                        else:
                            comment += "%d \\begin{array}{&})%d &%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B < 10 and C >= 10) or (A >= 10 and B < 10 and C < 10) or (A < 10 and B >= 10 and C < 10):
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    else:
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\phantom{0} \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    B = B/i
                    C = C/i
                    break

                elif A%i == 0 and B%i != 0 and C%i ==0:
                    divisor.append(i)
                    if A >=10 and B >= 10 and C >= 10:
                        comment += "%d \\begin{array}{&})%d &%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B >= 10 and C >= 10) or (A >= 10 and B < 10 and C >= 10) or (A >= 10 and B >= 10 and C < 10):
                        if A < 10 or B < 10:
                            comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                        else:
                            comment += "%d \\begin{array}{&})%d &%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    elif (A < 10 and B < 10 and C >= 10) or (A >= 10 and B < 10 and C < 10) or (A < 10 and B >= 10 and C < 10):
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    else:
                        comment += "%d \\begin{array}{&})%d &\\phantom{0}%d &\\phantom{0}%d \\phantom{0} \\\\ \\hline \\end{array} \\\\"%(i,A,B,C)
                    A = A/i
                    C = C/i
                    break

            if gcd1 == 1 and gcd2 == 1 and gcd3 == 1:
                if A >=10 and B >= 10 and C >= 10:
                        comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &%d &%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                        break
                elif (A < 10 and B >= 10 and C >= 10) or (A >= 10 and B < 10 and C >= 10) or (A >= 10 and B >= 10 and C < 10):
                    if A < 10:
                        comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &\\phantom{0}%d &%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                        break
                    elif B < 10:
                        comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &%d &%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                        break
                    else:
                        comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &%d &\\phantom{0}%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                        break
                elif (A < 10 and B < 10 and C >= 10) or (A >= 10 and B < 10 and C < 10) or (A < 10 and B >= 10 and C < 10):
                    comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &\\phantom{0}%d &\\phantom{0}%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                    break
                else:
                    comment += "\\phantom{0} \\phantom{0} \\begin{array}{&}%d &\\phantom{0}%d &\\phantom{0}%d \\end{array} \\end{array} \\Rightarrow"%(A,B,C)
                    break   

        for i in range(0,len(divisor)):
            if i == len(divisor)-1:
                comment = comment + str(divisor[i]) + "\\times %d \\times %d \\times %d = %d"%(A,B,C,lcm) 
            else:
                comment = comment + str(divisor[i]) + "\\times"

    return stem, answer, comment

if __name__ == '__main__':
    for i in range(0,10):
        stem, answer, comment = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')
        print(comment + '\\\\')