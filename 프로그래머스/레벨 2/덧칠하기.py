# 매우 간단한 문제.
def solution(n, m, section):
    a,result = 0, 0
    for i in section:
        if a < i: 
            a = i + m - 1
            result+=1
    return result
#처음에 너무 복잡하게 생각했다..
# def solution(n, m, section):
#     arr = [1] * n
#     # print(arr)
#     result = 0
#     for i in section:
#         arr[i-1] = 0
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             result+=1
#             for k in range(m):
#                 if arr.index(arr[k]) <= len(arr):
#                     arr[k] = 1
#                 else: break
#     return result
