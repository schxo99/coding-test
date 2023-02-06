# 처음에는 min()을 사용해서 최솟값을 확인하고, 반복문에서 계속 sort()를 하여 정렬했는데, 절반이 시간초과가 나타나 heapq를 사용. heapify, heappop, heappush 사용
import heapq
def solution(s, k):
    result = 0
    heapq.heapify(s)
    if s[0] >= k:
        return result
    while s[0] < k:
        if len(s) <= 1:
            return -1
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        heapq.heappush(s, a + (b*2))
        result+=1
    return result
    
#비스무리하게 시간초과
# from collections import deque
# def solution(scoville, k):
#     result = 0
#     food = deque(scoville)
#     if min(food) < k:
#         while True:
#             food = deque(sorted(food))
#             a = food[0]
#             food.popleft()
#             food[0] = (food[0]*2) + a
#             result+=1
#             if min(food) >= k:
#                 break
#     return result
    # print(scoville, k)

# 절반이 시간초과.
# def solution(scoville, K):
#     result=0
#     if min(scoville) < K:
#         while True:
#             scoville.sort()
#             a = min(scoville)
#             scoville.remove(a)
#             b = min(scoville)
#             scoville.remove(b)
#             scoville.append((b*2) + a)
#             result+=1
#             if min(scoville)>=K:
#                 break
#     else: return 0
#     return result
