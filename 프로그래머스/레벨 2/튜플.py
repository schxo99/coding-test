def solution(s):
    dic = {}
    left, right = s.count("{"), s.count("}")
    for i in range(max(left, right)):
        s = s.replace('{', '').replace('}', '')
    s = list(map(int, s.split(',')))
    for i in s:
        if i in dic:
            dic[i]+=1
        else: dic[i] = 1
    aa = dict(sorted(dic.items(), key = lambda x:x[1], reverse = True))
    return list(aa.keys())
