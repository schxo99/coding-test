#생각보다 어려워서 3일동안 고민하면서 풀었다.
## deque를 사용해서 풀수도 있을 것 같아서 풀이.
from collections import deque
def solution(numlist, n):
    result = []
    numlist = deque(sorted(numlist, reverse = True))
    while len(numlist) > 1:
        if abs(numlist[0] - n) <= abs(numlist[1] - n) and abs(numlist[0] - n) <= abs(numlist[-1] - n):
            if abs(numlist[0] - n) == abs(numlist[-1] - n):
                result.append(numlist[-1])
                numlist.pop()
            else:
                result.append(numlist[0])
                numlist.popleft()
        else:
            numlist.append(numlist[0])
            numlist.popleft()
    result.append(numlist[0])
    return result

## 처음 풀이 1개가 오류. 
# def solution(numlist, n):
#     numlist.sort(reverse = True)
#     result, i = [], 0
#     while True:
#         if len(numlist) <= 1: 
#             result.append(numlist[0])
#             break
#         elif len(numlist) >= 2:
#             if abs(numlist[i] - n) >= abs(numlist[i+1] - n):
#                 if i == len(numlist)-2:
#                     result.append(numlist[i+1])
#                     numlist.pop(i+1)
#                 else: i+=1
#             elif abs(numlist[i] - n) < abs(numlist[i+1] - n):
#                 if i >= 1 and abs(numlist[i-1] - n) == abs(numlist[i] - n):
#                     result.append(numlist[i-1])
#                     numlist.pop(i-1)
#                 else:
#                     result.append(numlist[i])
#                     numlist.pop(i)
#                 i = 0
#         if i >= len(numlist) -1:
#             i = 0
#     return result
