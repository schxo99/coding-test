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

##다른사람의 풀이
# 간단하고 가독성이 좋은 풀이인 것 같다.
# def solution(s):
#     a, b = 0, 0
#     while s != '1':
#         a += 1
#         num = s.count('1')
#         b += len(s) - num
#         s = bin(num)[2:]
#     return [a, b]
