def solution(s):
    zero = 0
    time = 0
    s = list(s)
    s = list(map(int, s))
    s.sort()   
    while True:
        for i in range(len(s)):
            if s[0] == 0:
                del s[0]
                zero+=1
            else: break
        s = bin(len(s))
        s = s[2:]
        s = list(map(int,s))
        s.sort()
        time+=1
        if s == [1]:
            break
    return [time, zero]
