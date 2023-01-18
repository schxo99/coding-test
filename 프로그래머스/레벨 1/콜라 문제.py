# a = 반환 갯수
# b = 주는 갯수
# n = 빈병갯수
def solution(a, b, n):
    hap = 0
    while True:
        if n < a: break
        else:
            na = n//a
            n = n%a
            hap += na*b
            n += na*b
            print(hap)
    return hap
