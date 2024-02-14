import numpy as np


def vertical_div(num2, num1, BP) :
    # step_1
    targets, muls = [], []
    ans = ''
    i = 0
    while True :
        if ans != '' and int(ans) == BP:
            break
        if i == 0 :
            target = int(str(num1)[i:len(str(num2))+i])
        elif i >= len(str(num1))-1 :
            target = int('%s0' % (mod))
        else :
            target = int('%s%s' % (mod, int(str(num1)[len(str(num2))+i-1])))
        div = target // num2
        mul = div * num2
        mod = target % num2
        i += 1
        targets.append(str(target))
        muls.append(str(mul))
        ans += str(div)
    targets.append('0')
    result = list(map(list, zip(muls, targets[1:])))
    return result


def generate():
    while True :
        A = np.random.randint(2, 21)
        B = np.random.randint(10, 201)
        C = A * B
        if C % 10 == 0 and B % 10 != 0 and int(str(C)[:len(str(A))]) > A and A % 10 != 0:
            n1 = 3 if C % 1000 == 0 else 2 if C % 100 == 0 else 1
            break

    B_text = str(B)
    B_text = '\\phantom{.}'.join(list(B_text[:len(B_text)-n1])) + '.' + '\\phantom{.}'.join(list(B_text[len(B_text)-n1:]))
    D = C // pow(10, n1)
    D_text = '\\phantom{.}'.join(list(str(D))) + '\\color{gray} {.' + '\\phantom{.}'.join(['0'] * n1) + '}'
    target_mode = vertical_div(A, C, B)
    result = []
    B_quotient_length = len(str(D // A))    # B의 자연수 부분 길이
    for i, (m, t) in enumerate(target_mode):
        b1 = '\\phantom{.}\\phantom{0}' * B_quotient_length
        b2 = '\\phantom{.}\\phantom{0}' * (B_quotient_length - 1)
        m_text = '\\phantom{.}'.join(m)
        t_text = '\\phantom{.}'.join(t)
        result.append('%s %s \\\\ \n\\hline \n%s %s \\\\' % (m_text, b1, t_text, b2))
        if B_quotient_length > 0:
            B_quotient_length -= 1
    result = '\n'.join(result)

    stem = '\\require{enclose}' \
           '\\begin{aligned}[t]' \
           '%s \\phantom{.} \\enclose{longdiv}{\\phantom{.} %s}' \
           '\\end{aligned}' % (A, D)
    comment = '\\require{enclose} \n' \
              '\\begin{aligned}[t]\n' \
              '%s \\\\ \n' \
              '%s \\phantom{.}\n' \
              '\\enclose{longdiv}{\\phantom{.}%s}\\\\ \n' \
              '%s' \
              '\\end{aligned}\n' % (B_text, A, D_text, result)
    answer = str(D/A)
    return stem, answer, comment
    
if __name__ == '__main__':
    stem, answer, comment = generate()
    print(stem + '\\\\')
    print(answer + '\\\\')
    print(comment + '\\\\')