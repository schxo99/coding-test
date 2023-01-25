## 시간초과가 하나 남 ㅠㅠ -- ? 다시 돌리는 다 통과 됨
def solution(n):
    a = bin(n)[2:]
    a = list(map(int, a))
    a = a.count(1)
    b = n+1
    while True:
        c = bin(b)[2:]
        c = list(map(int, c))
        c = c.count(1)
        if a == c:
            break
        else:
            b+=1
    return b
