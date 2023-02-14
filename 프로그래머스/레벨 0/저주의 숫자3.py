def solution(n):
    add = 0
    for i in range(1, n+1):
        if '3' in str(i) or i % 3 == 0:
            add += 1
            while True:
                if '3' in str(n + add) or (n+add) % 3 == 0:
                    add+=1
                else: break
    return n + add
