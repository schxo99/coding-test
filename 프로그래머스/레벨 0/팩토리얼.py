def solution(n):
    a = 1
    p = 1
    while True:
        if p == n:
            break
        elif p >= n:
            a-=1
            break
        a+=1
        p *= a
    return a
