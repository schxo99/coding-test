def solution(gems):
    first = 1
    last = len(gems)
    answer = []
    for i in range(len(gems)):
        if gems[-1] in gems[:-2]:
            del gems[-1]
            last-=1

        else:
            break
    for i in range(len(gems)):
        if gems[0] in gems[1:]:
            del gems[0]
            first+=1
        else:
            break
    
    answer.append(first)
    answer.append(last)
    return answer
