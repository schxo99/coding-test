#4차 성공!
#pop보단 슬라이싱하는게 더 효율적인듯.
#replace 함수보다 스택 활용하는게 더 효율적인듯
def solution(s):
    s = list(s)
    arr = []
    for i in range(len(s)):
        arr.append(s[i])

        if len(arr) >=2 and arr[-1] == ')' and arr[-2] == '(':
            del arr[-2:]
    if len(arr) >= 1:
        return False
    else:
         return True

#3차 시간초과 하나만 오류
# def solution(s):
#     s = list(s)
#     arr = []
#     for i in range(len(s)):
#         arr.append(s[i])

#         if len(arr) >=2 and arr[-1] == ')' and arr[-2] == '(':
#             arr.pop()
#             arr.pop()
#     if len(arr) >= 1:
#         return False
#     else:
#          return True
        
#2차 시간초과 오류
# def solution(s):
#     s = list(s)
#     arr = []
#     for i in range(len(s)):
#         arr.append(s[0])
#         del s[0]
#         if len(arr) >=2 and arr[-1] == ')' and arr[-2] == '(':
#             arr.pop()
#             arr.pop()
#     if len(arr) >= 1:
#         return False
#     else:
#          return True
        
#1차 시간초과 오류
# def solution(s):
#     for i in range(len(s)//2):
#         a = s.replace('()', '')
#         if a == s:
#             break
#         else:
#             s = a
#     if len(s) >= 1:
#         return False
#     else:
#         return True
