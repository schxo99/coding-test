def solution(k, m, score):
    score.sort()
    arr = []
    sum = 0
    for i in range(len(score)//m):
        arr.append([])
        for _ in range(m):
            arr[i].append(score[-1])
            score.pop()
    for k in range(len(arr)):
        a = min(arr[k])
        sum+=a*m
    return sum
solution(3,	4,	[1, 2, 3, 1, 2, 3, 1])
# k = 최고등급 m = 상자에 들어갈 사과 개수 score = 사과