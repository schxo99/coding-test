import heapq
def solution(n, works):
    result = 0
    for i in range(len(works)):
        works[i] = works[i]*-1
    heapq.heapify(works)
    for i in range(n):
        if len(works) == 0:
            break
        a = heapq.heappop(works)
        a+=1
        if a <0:
            heapq.heappush(works, a)
    for i in works:
        result+= i**2
    return result

# def solution(n, works):
#     result = 0
#     while n:
#         works.sort()
#         works[-1], n = works[-1]-1, n-1
#         if works[-1] == 0:
#             works.pop()
#         if len(works) == 0:
#             break
#     if works:
#         for i in works:
#             result += i **2
#         return result
#     return 0
