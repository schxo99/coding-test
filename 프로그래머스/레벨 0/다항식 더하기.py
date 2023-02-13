##반례에 대해 생각보다 까다로웠다.
def solution(string):
    alpha, digit = [], []
    string = string.split()
    for i in string:
        if 'x' in i:
            if i == 'x':
                alpha.append(1)
            else:
                if i[0] != '0':
                    alpha.append(int(i[:-1]))
        elif i.isdigit():
            digit.append(int(i))
    alpha = sum(alpha)
    digit = sum(digit)
    print(alpha, digit)
    if digit == 0:
        if alpha == 1:
            return 'x'
        else:
            return str(alpha)+'x'
    elif alpha == 0:
        return str(digit)
    else: 
        if alpha == 1:
            return 'x' + ' + '+str(digit)
        else:
            return str(alpha)+'x'+' + '+str(digit)
## 런타임이 절반정도
# def solution(polynomial):
#     arr = polynomial.split()
#     a = arr.count('+')
#     digit, alpha = 0,0
#     for i in range(a):
#         arr.remove('+')
#     for i in arr:
#         if i.isdigit():
#             digit+=int(i)
#         else:
#             if i == 'x':
#                 alpha+=1
#             else:
#                 alpha+=int(i[:1])
#     if digit == 0:
#         return str(alpha)+'x'
#     elif alpha == 0:
#         return str(digit)
#     else:
#         return str(alpha)+'x'+' + '+str(digit)
