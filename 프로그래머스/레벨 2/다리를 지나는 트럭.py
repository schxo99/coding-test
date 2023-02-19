## 역시 sum은 비효율적이라 무게를 계산하는 코드 추가해서 통과!
from collections import deque
def solution(bridge_length, weight, truck_weights):
    arr = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time, sum_weight = 0, 0
    while True:
        sum_weight -= arr[0]
        arr.popleft()
        time+=1
        if len(truck_weights) >= 1:
            if sum_weight + truck_weights[0] <= weight:
                arr.append(truck_weights[0])
                sum_weight += truck_weights[0]
                truck_weights.popleft()
            else:
                arr.append(0)
        else:
            if sum_weight == 0:
                break
    return time

## 수정 후에는 하나가 시간초과.
# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     arr = deque([0] * bridge_length)
#     truck_weights = deque(truck_weights)
#     time = 0
#     while True:
#         arr.popleft()
#         time+=1
#         if len(truck_weights) >= 1:
#             if sum(arr) + truck_weights[0] <= weight:
#                 arr.append(truck_weights[0])
#                 truck_weights.popleft()
#             else:
#                 arr.append(0)
#         else:
#             if sum(arr) == 0:
#                 break
#     return time

##조건절의 순서때문에 런타임 오류가 났다...
# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     arr = deque([0] * bridge_length)
#     truck_weights = deque(truck_weights)
#     time = 0
#     while True:
#         if len(truck_weights) >= 1:
#             if sum(arr) + truck_weights[0] <= weight:
#                 arr.append(truck_weights[0])
#                 arr.popleft()
#                 truck_weights.popleft()
#             else:
#                 arr.popleft()
#                 arr.append(0)
#         else:
#             if sum(arr) == 0:
#                 break
#             else: 
#                 arr.popleft()
#                 arr.append(0)
#         time+=1
#     return time
