def solution(n):
    result = 0
    for i  in range(1, n+1):
        hap = 0
        for k in range(i, n+1):
            hap+=k
            if hap == n:
                result +=1
            elif hap > n:
                break
    return result
