## 전에 풀었던 dp문제랑 유사한 제였지만, 공간복잡도에서 오류가 나는 것 같아 deque를 사용하여 불필요한 요소들을 삭제.
from collections import deque
def solution(n):
    if n < 3:
        return n
    arr=[1,2]
    arr = deque(arr)
    for i in range(2, n):
        arr.append(arr[0] + arr[1])
        arr.popleft()
    return arr[-1]%1000000007
