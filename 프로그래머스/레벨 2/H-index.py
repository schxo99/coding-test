##이건 어려운것보다 문제가 이해안됐다...
def solution(citations):
    citations.sort()
    a = len(citations)
    for i in range(len(citations)):
        if citations[i] >= a-i:
            return a-i
    return 0

# def solution(citations):
#     hap = 0
#     i = len(citations)
#     while True:
#         for k in citations:
#             if k >= i:
#                 hap+=1
#         if hap == i:
#             return i
#         else:
#             i-=1
#             hap = 0

# def solution(citations):
#     hap = 0
#     i = 1
#     while True:
#         for k in citations:
#             if k >= i:
#                 hap+=1
#         if hap == i:
#             return i
#         else: 
#             i+=1
#             hap = 0
            
# def solution(citations):
#     citations.sort(reverse = True)
#     for i in citations:
#         hap = 0
#         for k in citations:
#             if k >= i:
#                 hap+=1
#         if hap == i:
#             return i
    
# def solution(citations):
#     citations.sort(reverse = True)
#     for i in citations:
#         u = 0
#         l = 0
#         for k in citations:
#             if i >= k:
#                 u +=1
#             if i <= k:
#                 l+=1
#         if i == u and i == l:
#             return i
