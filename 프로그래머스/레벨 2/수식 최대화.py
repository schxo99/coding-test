def mul(arr):
    while "*" in arr:
        i = arr.index("*")
        arr[i-1] = int(arr[i-1]) * int(arr[i+1])
        arr.pop(i)
        arr.pop(i)
    return arr

def plus(arr):
    while "+" in arr:
        i = arr.index("+")
        arr[i-1] = int(arr[i-1]) + int(arr[i+1])
        arr.pop(i)
        arr.pop(i)
    return arr

def sub(arr):
    while "-" in arr:
        i = arr.index("-")
        arr[i-1] = int(arr[i-1]) - int(arr[i+1])
        arr.pop(i)
        arr.pop(i)
    return arr

def solution(expression):
    arr, hap = [], ""
    for i in expression:
        if i.isdigit():
            hap+=i
        else:
            arr.append(hap)
            arr.append(i)
            hap = ""
    arr.append(hap)
    # * + - 경우
    result1 = abs(sub(plus(mul(arr[:])))[0])
    # * - + 경우
    result2 = abs(plus(sub(mul(arr[:])))[0])
    # + * - 경우
    result3 = abs(sub(mul(plus(arr[:])))[0])
    # + - * 경우
    result4 = abs(mul(sub(plus(arr[:])))[0])
    # - + * 경우
    result5 = abs(mul(plus(sub(arr[:])))[0])
    # - * + 경우
    result6 = abs(plus(mul(sub(arr[:])))[0])
    
    return max(result1, result2, result3, result4, result5, result6)
