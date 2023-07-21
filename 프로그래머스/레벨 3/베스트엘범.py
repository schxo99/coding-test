def solution(genres, plays):
    answer = []
    dic = {}
    for i, k in zip(genres, plays):
        if i not in dic:
            dic[i] = 0
        dic[i] += k
    li = list(dict(sorted(dic.items(), key = lambda x : x[1], reverse = True)).keys())
    for i in li:
        bb = {}
        for j,k in enumerate(genres):
            if i == k:
                bb[j] = plays[j]
        bb = list(dict(sorted(bb.items(), key = lambda x : (x[1], -x[0]))))
        for n in range(2):
            if bb:
                answer.append(bb.pop())
    return answer
