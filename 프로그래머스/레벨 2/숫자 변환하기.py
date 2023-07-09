from collections import deque
def solution(x, y, n):
    arr = deque([[x, 0]])
    visited = set()
    while arr:
        num, index = arr.popleft()
        if num == y:
            return index
        if num not in visited and num < y:
            visited.add(num)
            arr.append([num+n, index+1])
            arr.append([num*2, index+1])
            arr.append([num*3, index+1])
    return -1
        
