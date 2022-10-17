def solution(s):
    a = list(map(int, s.split()))
    a.sort()
    b = int(a[0])
    c = int(a[-1])
    result = []
    if b<=c:
        result.append(b)
        result.append(c)
        result = map(str, result)
        answer =  ' '.join(result)
        # return answer
        print(answer)
    else:
        result.append(c)
        result.append(b)
        result = map(str, result)
        answer= ' '.join(result)
        # return answer
        print(answer)
solution("1 2 3 4")