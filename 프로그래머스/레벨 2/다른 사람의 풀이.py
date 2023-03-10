def solution(n):
    arr = ["1", "2", "4"]
    hap = ""
    result = ""
    while n > 0:
        n-=1
        hap = str(arr[(n % 3)]) + hap
        n = n//3
    return hap
