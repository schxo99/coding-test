def solution(a, b):
    a = list(a)
    b = list(b)
    result = 0
    for i in range(len(a)):
        if a == b:
            return result
        else:
            a.insert(0, a[-1])
            a.pop()
            result+=1
    return -1
