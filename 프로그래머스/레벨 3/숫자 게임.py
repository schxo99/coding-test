def solution(a, b):
    result = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[-1] < b[-1]:
            result+=1
            b.pop()
        a.pop()
    return result
