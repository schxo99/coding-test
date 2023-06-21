def solution(arr):
    x = len(arr[0])
    y = len(arr)
    if x == y: return arr
    if x > y:
        for i in range(x-y):
            arr.append([0]*(len(arr[0])))
    elif y > x:
        for i in range(len(arr)):
            for k in range(y-x):
                arr[i].append(0)
    return arr
