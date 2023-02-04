#전에 풀이에 사용했던 deque를 사용했다. 처음에 오류가 있었으나 조건절 순서를 수정하여 통과~
from collections import deque
def solution(priorities, location):
    t = priorities[location]
    priorities[location] = 0
    priorities = deque(priorities)
    result = 0
    while True:
        if priorities[0] == 0:
            if t >= max(priorities):
                result+=1
                return result
                break
            else:
                priorities.append(priorities[0])
                priorities.popleft()
        else:
            if priorities[0] >= max(priorities) and priorities[0] >= t:
                priorities.popleft()
                result+=1
            elif priorities[0] <= max(priorities) or priorities[0] <= t:
                priorities.append(priorities[0])
                priorities.popleft()
