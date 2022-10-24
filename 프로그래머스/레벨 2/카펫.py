def solution(brown, yellow):
    arr, result = [], []
    if yellow == 1:
        return [3,3]
    for i in range(1, yellow):
        if yellow % i == 0:
            arr.append([i, int(yellow/i)])
    for i in range(len(arr)):
        if (arr[i][0]*2)+(arr[i][1]*2) + 4 == brown:
            result.append(arr[i][0]+2)
            result.append(arr[i][1]+2)
            result.sort(reverse=True)
            return result