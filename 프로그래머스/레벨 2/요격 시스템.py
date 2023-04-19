from collections import deque
def solution(targets):
    result = 0
    targets.sort()
    targets = deque(targets)
    while targets:
        num = targets[0][1]
        hap = 0
        for i in targets:
            if num > i[0]:
                if num > i[1]:
                    num = i[1]
                hap += 1
            else:
                break
        for _ in range(hap):      
            targets.popleft()
        result+=1
    return result
