# 전에 푼 풀이는 skip의 중복된 알파벳오류가 아닌.. 인덱스 문제 였던 것 같다. 아마 index의 크기가 skip이 제거된 알파벳 보다 큰 경우 오류로 예상. 따라서 제거된 알파벳의 길이를 더 많이
#복붙했더니 통과되었다.
from string import ascii_lowercase
def solution(s, skip, index):
    result = ''
    alpha = list(ascii_lowercase)
    skip = list(skip)
    for i in skip:
        alpha.remove(i)
    alpha = alpha*4
    for i in range(len(s)):
        a = alpha.index(s[i])
        result+=alpha[a+index]
    return result

# 아마 skip에서 중복된 알파벳이 있을 때 오류나는 것 같다.
# from string import ascii_lowercase
# def solution(s, skip, index):
#     result = ''
#     alpha = list(ascii_lowercase)
#     skip = list(skip)
#     for i in skip:
#         if i in alpha:
#             alpha.remove(i)
#     for i in range(len(s)):
#         a = alpha.index(s[i])
#         if a + index >= len(alpha):
#             result+=alpha[a+index-len(alpha)]
#         else:
#             result+=alpha[a+index]
#     return result
