# del, 슬라이싱 보다 pop이 더 효율적이고, 기존에는 리스트에 추가해서 비교했는데 바로 비교후 동작하게 하니 통과되었다.
def solution(s):
    arr = []
    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        elif arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])
    if len(arr) == 0:
        return 1
    else: return 0
            

# 효율성 시간 초과..
# def solution(s):
#     arr = []
#     s = list(s)
#     for i in range(len(s)):
#         arr.append(s[0])
#         s.pop(0)
#         if len(arr) >= 2 and arr[-2] == arr[-1]:
#             arr.pop()
#             arr.pop()
#     if len(arr) == 0: 
#         return 1
#     else: return 0

# 테스트는 다 돌아가나 효율성 시간 초과..
# def solution(s):
#     arr = []
#     s = list(s)
#     for i in range(len(s)):
#         arr.append(s[0])
#         s = s[1:]
#         if len(arr) >= 2 and arr[-2] == arr[-1]:
#             arr = arr[:-2]
#     if len(arr) == 0: 
#         return 1
#     else: return 0

# 시간초과.. 첫 번째 보다는 잘나옴...
# def solution(s):
#     i = 0
#     result = 1
#     while True:
#         a = s
#         if s[i]*2 in s:
#             s = s.replace(s[i]*2, '')
#             i = 0
#         else:
#             i+=1
#         if len(s) == 0:
#             break
#         if a == s and i == len(s):
#             result = 0
#             break
#     return result
            
# 시간 초과...
# def solution(s):
#     i = 0
#     s = list(s)
#     while True:
#         if s[i] == s[i+1]:
#             del s[i]
#             del s[i]
#             i = 0
#         else: 
#             i+=1
#         if i == len(s) - 1:
#             return 0
#             break
#         if len(s) == 0:
#             return 1
#             break
