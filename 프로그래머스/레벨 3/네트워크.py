def solution(n, computers):
    visited = []
    answer = 0
    def dfs(i):
        for k in range(n):
            if computers[i][k] == 1 and k not in visited:
                visited.append(k)
                dfs(k)
    
    for i in range(n):
        if i not in visited:
            visited.append(i)
            answer +=1
            dfs(i)
    return answer
