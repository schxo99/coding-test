def solution(land):
    for i in range(0, len(land)-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    return max(land[-1])
        
    
##처음에 dfs문제인줄 알고 풀었다가 테스트코드만 통과하고 채점에서 오류.. 깊게 돌아가서 그런 것 같다.
# answer = 0
# def dfs(land, level, ch, hap):
#     global answer
#     if level == len(land):
#         answer = max(answer, hap)
#         return
#     elif level < len(land):
#         for k in range(len(land[0])):
#             if ch != k:
#                 dfs(land, level + 1, k, hap + land[level][k])          
    
# def solution(land):
#     level, hap = 0, 0
#     for i in range(len(land[0])):
#         dfs(land, level, i, hap)
#     return answer
