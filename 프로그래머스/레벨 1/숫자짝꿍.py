# 기존 풀이 => 숫자가 너무 큰 경우는 시간초과 부여
# def solution(X, Y):
#     xarr, yarr, result = [],[], []
#     for i in range(len(X)):
#         xarr.append(X[i])
#     for i in range(len(Y)):
#         yarr.append(Y[i])
#     for k in xarr:
#         if k in yarr:
#             result.append(k)
#             yarr.remove(k)
#     if len(result) == 0:
#         print('-1')
#     elif sum(map(int,result)) == 0:
#         print('0')
#     else:
#         result.sort(reverse = True)
#         # result = map(str, result)
#         answer = ''.join(result)
#         print(answer)
# solution(X,Y)

# 숫자는 0~9로 이루어져있으니 숫자 수를 세서 작은 것을 넣음

def solution(X,Y):
    x = list(X)
    y = list(Y)
    xarr, yarr = [],[]
    result = ''
    for i in range(10):
        xarr.append(x.count(str(i)))
        yarr.append(y.count(str(i)))
    for k in range(len(xarr)):
        if xarr[k] >= yarr[k]:
            result+= str(k)*yarr[k]
        else:
            result+= str(k)*xarr[k]
    result = list(result)
    result.sort(reverse = True)
    if len(result) == 0:
        answer = '-1'
    elif sum(map(int, result)) == 0:
        answer = '0'
    else:
        answer = ''.join(result)
    return answer

solution(X,Y)