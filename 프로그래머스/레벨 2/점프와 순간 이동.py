def solution(n):
    result = 0
    while True:
        if n == 1:
             break
        if n % 2 == 0:
            n = n/2
        elif n % 2 == 1:
            result+=1
            n = n - 1
    return result+1
