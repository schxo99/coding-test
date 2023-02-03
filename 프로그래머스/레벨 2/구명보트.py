#처음에는 deque를 사용하지 않고 작성했을 때 효율성 1번에서 실패가 떴다. deque를 사용하니 통과가 되었는데, popleft를 사용안할 시 인덱스에 접근해야하기 때문에 더 안좋다고 한다.
from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)
    hap, result = 0, 0
    for i in range(len(people)):
        hap = people[-1]
        people.pop()
        if hap + people[0] > limit:
            result+=1
        else:
            result+=1
            # people.pop(0)
            people.popleft()
        if len(people) == 1:
            result+=1
            break
        elif len(people) == 0:
            break
    return result
  
  #append(), pop(), appendleft(), append(), popleft(), extend(), extendleft(), insert(), remove(), reverse()
