from collections import deque
def solution(order):
    arr, tr, result = [], [], 0
    for i in range(len(order)):
        arr.append(i+1)
    arr, tr, order = deque(arr), deque(tr), deque(order)
    while True:
        if len(arr) > 0 and arr[0] == order[0]:
            arr.popleft()
            order.popleft()
            result+=1
        elif len(tr) > 0 and tr[-1] == order[0]:
            tr.pop()
            order.popleft()
            result+=1
        else:
            tr.append(arr[0])
            arr.popleft()
        if len(order) == 0:
            break
        if len(arr) == 0 and tr[-1] != order[0]:
            break
    return result
   
# 조건잘못줘서 오류
# from collections import deque
# def solution(order):
#     arr, tr, result = [], [], 0
#     for i in range(len(order)):
#         arr.append(i+1)
#     arr, tr, order = deque(arr), deque(tr), deque(order)
#     while True:
#         if arr[0] == order[0] or tr[-1] == order[0]:
#             if arr[0] == order[0]:
#                 arr.popleft()
#             else:
#                 tr.pop()
#             order.popleft()
#             result+=1
#         else:
#             tr.append(arr[0])
#             arr.popleft()
#         if len(arr) == 0 and tr[-1] != order[0]:
#             break
#     return result
            
