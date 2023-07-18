def solution(tickets):
    dic = {}
    for i, k in tickets:
        if i not in dic:
            dic[i] = []
        dic[i].append(k)
    for i in dic:
        dic[i].sort(reverse = True)
    
    answer = []
    def dfs(start):
        while start in dic and dic[start]:
            dfs(dic[start].pop())
        answer.append(start)
    dfs("ICN")
    answer.reverse()
    return answer
