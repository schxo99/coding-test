def solution(s):
    s = s.lower()
    s = list(s)
    if s[0].isalpha() == True:
        s[0] = s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i].isalpha() == True:
            s[i] = s[i].upper()
    result = ''.join(s)
    return result
  
# def solution(s):
#     s = s.lower()
#     arr = s.split(' ')
#     for i in range(len(arr)):
#         a = list(arr[i])
#         if a[0].isalpha() == True:
#             a[0] = a[0].upper()
#         arr[i] = ''.join(a)
#     result = ' '.join(arr)
#     print(arr)
#     return result
# ======> 공백이 연속으로 오는 경우 오류가 나는 것 같다.
