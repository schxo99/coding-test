def solution(arr):
    m = arr[-1]
    del arr[-1]
    a = True
    sum = m
    while True:
        for i in arr:
            if sum%i !=0:
                a = False
        if a == True:
            return sum
            break
        else:
            sum+=m
            a = True