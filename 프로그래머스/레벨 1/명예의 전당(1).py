def solution(k, score):
    arr = []
    result = []
    for i in range(len(score)):
        if len(arr) < k:
            arr.append(score[i])
        else:
            if arr[-1] <= score[i]:
                arr[-1] = score[i]
        arr.sort(reverse = True)
        result.append(arr[-1])
    return result
