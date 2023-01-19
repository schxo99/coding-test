def solution(s):
    arr = list(s)
    new = []
    result = []
    for i in range(len(arr)):
        if arr[i] not in new:
            new.append(arr[i])
            result.append(-1)
        else:
            result.append(1)
            for k in range(i-1,0,-1):
                if arr[i] == arr[k]:
                    break
                else:
                    result[-1]+=1
    return result
