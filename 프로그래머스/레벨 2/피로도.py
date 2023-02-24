answer = 0
def DFS(k, level, dungeons, ch):
    global answer
    answer = max(answer, level)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and ch[i] == 0:
            ch[i] = 1
            DFS(k - dungeons[i][1], level+1, dungeons, ch)
            ch[i] = 0
    
def solution(k, dungeons):
    ch = [0] * len(dungeons)
    level = 0
    DFS(k, level, dungeons, ch)
    return answer
