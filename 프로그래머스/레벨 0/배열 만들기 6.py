def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk and stk[-1] == arr[i]:
            stk.pop()
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
        i+=1
    if len(stk) == 0:
        return [-1]
    else:
        return stk
