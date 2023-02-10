##생각보다 푸는데 오래걸렸다.. 0레벨도 다 풀어봐야겠다.

def solution(array):
    arr = list(set(array))
    dic = {}
    for i in arr:
        dic[i] = array.count(i)
    aa = list(dic.values())
    bb = list(dic.keys())
    if aa.count(max(aa)) > 1:
        return -1
    else: return bb[aa.index(max(aa))]
