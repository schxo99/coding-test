def solution(number, k):
    stack = []
    for i in number:
        if k > 0:
            while stack and stack[-1] < i:
                stack.pop()
                k -= 1
                if not stack or k <= 0:
                    break
        stack.append(i)
    if k > 0:
        return number[:len(number)-k]
    else:
        return ''.join(stack)
            
# import itertools
# def solution(number, k):
#     result = []
#     for i in itertools.permutations(list(number), len(number)-k):
#         result.append("".join(i))
#     return max(result)

# 시간초과
# def ma(number, k):
#     index = 0
#     while True:
#         test = number[:]
#         test.pop(index)
#         if ''.join(test) > ''.join(number):
#             return test
#         else: index+=1
        
# def solution(number, k):
#     lv = 0
#     number = list(number)
#     while lv < k:
#         number = ma(number, k)
#         lv+=1
#     return ''.join(number)
    
# 시간 초과       
# def solution(number, k):
#     number = list(number)
#     ch, i = 0, 0
#     while ch < k:
#         test = number[:]
#         test.pop(i)
#         if ''.join(number) < ''.join(test):
#             ch += 1
#             i, number = 0, test
#         else:
#             if i == len(number)-1:
#                 i = 0
#             else: i+=1
#     return ''.join(number)
