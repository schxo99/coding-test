from collections import deque
def solution(begin, target, words):
    qu = deque([[begin, 0]])
    visited = [False] * len(words)
    def bfs(qu, target, words):
        while qu:
            string = qu.popleft()
            if string[0] == target:
                return string[1]
            for i in range(len(words)):
                if visited[i] == False:
                    di = 0
                    for k in range(len(begin)):
                        if string[0][k] != words[i][k]:
                            di+=1
                        if di > 1:
                            break
                    if di < 2: 
                        qu.append([words[i], string[1]+1])
                        visited[i] = True
    answer = bfs(qu, target, words)
    return answer if answer else 0
