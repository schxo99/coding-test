## 이게 될줄 몰랐는데 잘 돌아간다.
from collections import deque
def solution(queue1, queue2):
    aa = len(queue1)
    hap = (sum(queue1) + sum(queue2)) // 2
    deque1, deque2 = max(queue1, queue2), min(queue1, queue2)
    deque1, deque2 = deque(deque1), deque(deque2)
    deque1hap, deque2hap, result = sum(deque1), sum(deque2), 0
    while deque1hap != deque2hap:
        if deque1hap > deque2hap:
            deque2hap += deque1[0]
            deque2.append(deque1[0])
            deque1hap -= deque1[0]
            deque1.popleft()
        else:
            deque1hap += deque2[0]
            deque1.append(deque2[0])
            deque2hap -= deque2[0]
            deque2.popleft()
        result+=1
        if result >= aa * 4:
            return -1
    return result
