def solution(clothes):
    arr = []
    result = 1
    for i in range(len(clothes)):
        arr.append(clothes[i][1])
        clothes[i] = clothes[i][1]
    arr = list(set(arr))
    for k in range(len(arr)):
        a = clothes.count(arr[k]) + 1
        result = result * a
    result-=1
    return result
