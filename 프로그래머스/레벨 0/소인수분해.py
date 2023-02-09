# set 사용 시 정렬이 지켜지지 않는다. 정렬을 필요로 한다면, set 사용 후 정렬!
def solution(n):
    a = 2
    arr = []
    while True:
        if n % a == 0:
            arr.append(a)
            n = n//a
        else: a+=1
        if n == 1:
            break
    arr = list(set(arr))
    arr.sort()
    return arr
