result = [0, 0]
def check(arr):
    first = arr[0][0]
    s_result = [0,0]
    for i in arr:
        for k in i:
            if first != k:
                return False
    result[first] += 1
    
def re(arr):
    global result
    x, y = len(arr[0]), len(arr)
    a = check(arr)
    if a == False:
        re([arr[i][:len(arr[i])//2] for i in range(len(arr)//2)])
        re([arr[i][len(arr[i])//2:] for i in range(len(arr)//2)])
        re([arr[i][:len(arr[i])//2] for i in range(len(arr)//2, len(arr), 1)])
        re([arr[i][len(arr[i])//2:] for i in range(len(arr)//2, len(arr), 1)])
def solution(arr):
    re(arr)
    return result
