from collections import deque
def solution(maps):
    ch = [[False] * len(maps[0]) for _ in range(len(maps))]
    i1 = [-1,1,0,0]
    i2 = [0,0,1,-1]
    ch[0][0] = True
    di = deque([[0, 0, 1]])
    while di:
        a = di.popleft()
        for i in range(4):
            if 0<=a[0]+i1[i]<len(maps) and 0<=a[1]+i2[i]<len(maps[0]) and ch[a[0]+i1[i]][a[1]+i2[i]] == False and maps[a[0]+i1[i]][a[1]+i2[i]]==1:
                if a[0]+i1[i] == len(maps)-1 and a[1]+i2[i] == len(maps[0])-1:
                    return a[2]+1
                ch[a[0]+i1[i] ][a[1]+i2[i]] = True
                di.append([a[0]+i1[i], a[1]+i2[i], a[2]+1])
    return -1
