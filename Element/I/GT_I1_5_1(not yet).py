import random
import fractions

def get_lcm(a,b):
    gcd = fractions.gcd(a,b)
    if a == b:
        return a
    else:
        return a*b // gcd

def get_fraction():
    while True:
        A = random.randint(2,30)
        B = random.randint(2,30)

        gcd = fractions.gcd(A,B)
        if gcd != 1 and A < B and B%A != 0:
            break

    return A, B

def generate():
    while True:
        A, B = get_fraction()
        gcd = fractions.gcd(A,B)
        lcm = get_lcm(A,B)

        
        stem = "\\left(%d, %d\\right)\\rightarrow \\Box"%(A,B)
        answer = "%d"%(lcm)
        comment = "\\begin{array}{&}"
        divisor=[]
        '''
        if A%2 == 0 and B%2 == 0:
            comment = comment + "2 |&%d &%d \\\\ \\hline"%(A,B)
            A = A/2
            B = B/2
            divisor.append(2)
            if fractions.gcd(A,B) == 1:
                comment = comment + "&%d &%d \\end{array} \\Rightarrow "%(A,B)
                break
        elif A%3 == 0 and B%3 == 0:
            comment = comment + "3 |&%d &%d \\\\ \\hline"%(A,B)
            A = A/3
            B = B/3
            divisor.append(3)
            if fractions.gcd(A,B) == 1:
                comment = comment + "&%d &%d \\end{array} \\Rightarrow "%(A,B)
                break
        elif A%5 == 0 and B%5 == 0:
            comment = comment + "5 |&%d &%d \\\\ \\hline"%(A,B)
            A = A/5
            B = B/5
            divisor.append(5)
            if fractions.gcd(A,B) == 1:
                comment = comment + "&%d &%d \\end{array} \\Rightarrow "%(A,B)
                break
        elif A%7 == 0 and B%7 == 0:
            comment = comment + "7 |&%d &%d \\\\ \\hline"%(A,B)
            A = A/7
            B = B/7
            divisor.append(7)
            if fractions.gcd(A,B) == 1:
                comment = comment + "&%d &%d \\end{array} \\Rightarrow "%(A,B)
                break
        '''

        while True:
            for i in range(2,99):
                if A%i == 0 and B%i == 0:
                    if A >= 10 and B >= 10:
                        comment = comment + "%d\\begin{array}{&})%d &%d \\\\ \\hline \\end{array} \\\\ "%(i,A,B)
                        A = A/i
                        B = B/i
                        divisor.append(i)
                        break
                    elif (A >= 10 and B < 10) or (A < 10 and B >= 10):
                        comment = comment + "%d\\begin{array}{&})%d &\\phantom{0}%d \\\\ \\hline \\end{array} \\\\ "%(i,A,B)
                        A = A/i
                        B = B/i
                        divisor.append(i)
                        break
                    else:
                        comment = comment + "%d\\begin{array}{&})%d &\\phantom{0} \\phantom{0}%d \\\\ \\hline \\end{array} \\\\ "%(i,A,B)
                        A = A/i
                        B = B/i
                        divisor.append(i)
                        break
            
            if fractions.gcd(A,B) == 1:
                if A >= 10 and B >= 10:
                    comment = comment + "\\begin{array}{&}\\phantom{0} \\phantom{0}%d &%d \\end{array} \\end{array} \\Rightarrow "%(A,B)
                    break
                elif (A >= 10 and B < 10) or (A < 10 and B >= 10):
                    comment = comment + "\\begin{array}{&}\\phantom{0} \\phantom{0}%d &\\phantom{0}%d \\end{array} \\end{array} \\Rightarrow "%(A,B)
                    break
                else:
                    comment = comment + "\\begin{array}{&}\\phantom{0} \\phantom{0}%d &\\phantom{0} \\phantom{0}%d \\end{array} \\end{array} \\Rightarrow "%(A,B)
                    break
        break

    for i in range(0,len(divisor)):
        if i == len(divisor)-1:
            comment = comment + str(divisor[i]) + "\\times %d \\times %d = %d"%(A,B,lcm) 
        else:
            comment = comment + str(divisor[i]) + "\\times"

    return stem, answer, comment

if __name__ == '__main__':
    #for i in range(0,20):
        stem, answer, comment = generate()
        print(stem + '\\\\')
        print(answer + '\\\\')
        print(comment + '\\\\')