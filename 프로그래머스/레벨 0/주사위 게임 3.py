def solution(a, b, c, d):
    dic = {}
    li = [a,b,c,d]
    for i in li:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+= 1
    dic = list(dic.items())
    dic.sort(key = lambda x:x[1], reverse = True)
    print(dic)
    if len(dic) == 1:
        return 1111 * dic[0][0]
    elif len(dic) == 4:
        dic.sort(key = lambda x:x[0])
        return dic[0][0]
    elif len(dic) == 3:
        return dic[1][0] * dic[2][0]
    elif dic[0][1] == 3:
        return (10 * dic[0][0] + dic[1][0]) ** 2
    else:
        return (dic[0][0] + dic[1][0]) * abs(dic[0][0] - dic[1][0])
