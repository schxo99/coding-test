#arr를 전역변수로 선언하고 실행 하니 채점에서 3개가 런타임 오류.. 리스트 깊이 문제인 것 같아 sys
import sys
sys.setrecursionlimit(10**6)
arr = []
def bottom(index, num, n, id1, id2):
    if arr[id1][id2] != 0:
        return
    for i in range(n - index):
        arr[id1][id2] = num
        num+=1
        id1+=1
    right(index+1, num, n, id1-1, id2+1)
    
def right(index, num, n, id1, id2):
    if arr[id1][id2] != 0:
        return
    for i in range(n - index):
        arr[id1][id2] = num
        num+=1
        id2+=1
    top(index+1, num, n, id1-1, id2-2)
    
def top(index, num, n, id1, id2):
    if arr[id1][id2] != 0:
        return
    for i in range(n - index):
        arr[id1][id2] = num
        num+=1
        id1 -= 1
        id2 -= 1
    bottom(index+1, num, n, id1+2, id2+1)
    
def solution(n):
    if n == 1:
        return [1]
    global arr
    index, num, id1, id2 = 0, 1, 0, 0
    for i in range(1, n+1):
        arr.append([0]*i)
    bottom(index, num, n, id1, id2)
    return sum(arr, []) 

# 인덱스에서 오류가 난 것 같음
# def top(arr, index, num, n, id1, id2):
#     if index == n:
#         return arr
#     for i in range(n-index):
#         arr[id1][id2] = num
#         if i == n-index-1:
#             break
#         id1 -= 1
#         id2 -= 1
#         num+=1
#     print("top", arr, id1, id2)
#     bottom(arr, index+1, num, n, id1, id2)
    
# def bottom(arr, index, num, n, id1, id2):
#     if index == n:
#         return arr
#     for i in range(n-index):
#         arr[id1][id2] = num
#         id1+=1
#         num+=1
#     print("bottom", arr, id1, id2)
#     right(arr, index, num, n, id1, id2)
    
# def right(arr, index, num, n, id1, id2):
#     if index == n:
#         return arr
#     for i in range(n-index):
#         arr[id1][id2] = num
#         id2+=1
#         num+=1
#     print("right", arr, id1, id2)
#     top(arr, index, num, n, id1, id2)
    
# def solution(n):
#     arr, index, num, id1, id2 = [], 1, 1, 0, 0
#     for i in range(1, n+1):
#         arr.append([0]*i)
#     print(bottom(arr, index, num, n, id1, id2))
