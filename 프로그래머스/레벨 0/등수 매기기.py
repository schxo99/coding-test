def solution(score):
    result = [0] * len(score)
    for i in range(len(score)):
        score[i] = sum(score[i])/2
    rank = 1
    human = 0
    for _ in range(len(score)):
        count = score.count(max(score))
        point = max(score)
        rank = rank + human
        human = 0
        for _ in range(count):
            i = score.index(point)
            result[i] = rank
            score[score.index(point)] = -1
            human +=1
        if 0 not in result:
            return result
    return result
