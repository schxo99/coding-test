# 효율성 문제
# def solution(n):
#     result = 0
#     answer=0
#     for i in range(2, n+1):
#         for k in range(1, i+1):
#             if i%k == 0:
#                 result+=1
#             if result > 2:
#                 result = 0
#                 break
#         if result == 2:
#             answer+=1
#         result = 0
#     return answer

#에라토스테네스의 체 개념 사용 but 시간 초과
# def solution(n):
#     arr = [2]
#     ch = 0
#     if n == 2:
#         return 1
#     else:
#         for i in range(2, n+1):
#             for k in range(len(arr)):
#                 if i % arr[k] == 0:
#                     ch = 1
#                     break
#             if ch == 0:
#                 arr.append(i)
#             else:
#                 ch = 0
#     return len(arr)

#에라토스테네스 다른 접근 but 시간초과
# def solution(n):
#     answer = 1
#     ch = 0
#     arr = list(range(2, n+1))
#     if n == 2:
#         return 1
#     else:
#         for i in range(1, len(arr)):
#             for k in range(i-1):
#                 if arr[i] % arr[k] == 0:
#                     ch = 1
#                     break
#             if ch == 0:
#                 answer+=1
#             else:
#                 ch = 0
#     return answer

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
