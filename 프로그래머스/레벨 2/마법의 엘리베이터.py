def solution(arr):
    arr = list(map(int, (list(str(arr)))))
    result = 0
    while arr:
        num = arr.pop()
        if num < 5:
            result += num
        elif num > 5:
            if arr:
                arr[-1] += 1
            else:
                arr.append(1)
            result += 10 - num
        else:
            if arr:
                if arr[-1] >= 5:
                    result += 10-num
                    arr[-1] += 1
                else:
                    result += num
            else: result += num
    return result
