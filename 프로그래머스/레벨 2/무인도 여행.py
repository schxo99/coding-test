from collections import deque
def solution(maps):
    result = []
    arr = deque([])
    ch = set()
    point = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    for i, j in enumerate(maps):
        for k, l in enumerate(j):
            if visited[i][k] == False and l != "X":
                arr.append([i, k])
                result.append(0)
                while arr:
                    n, m = arr.popleft()
                    visited[n][m] = True
                    result[-1] += int(maps[n][m])
                    for i1, i2 in point:
                        if 0 <= n + i1 < len(maps) and 0 <= m+i2<len(maps[0]) and visited[n+i1][m+i2] == False and maps[n+i1][m+i2] != "X":
                            if (n+i1,m+i2) not in ch:
                                ch.add((n+i1, m+i2))
                                arr.append([n+i1, m+i2])
    if len(result) == 0:
        return [-1]
    else: return sorted(result)
                    
            
