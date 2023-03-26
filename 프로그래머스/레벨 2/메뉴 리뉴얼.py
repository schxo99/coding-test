#딕셔너리 get 공부하기.
import itertools
def solution(orders, course):
    result = []
    for i in course:
        dic = {}
        for k in orders:
            for j in itertools.combinations(list(k), i):
                order = list(j)
                order.sort()
                if "".join(order) not in dic:
                    dic["".join(order)] = 1
                else:
                    dic["".join(order)]+=1
        if dic:
            v = max(dic.values())
        if v and v > 1:
            for key, value in dic.items():
                if v == value:
                    result.append(key)
    result.sort()
    return result
    
#시킨사람마다 수를 부여 해서 구하려니 마지막에 다 섞여서 키값길이에 대한 음식 주문양을 구하기 어려움
# def solution(orders, course):
#     dic = {}
#     num = [0] * len(course)
#     result = []
#     for i in orders:
#         order = list(i)
#         for k in range(2, len(order)+1):
#             if k in course:
#                 for j in itertools.combinations(order, k):
#                     if "".join(j) not in dic:
#                         dic["".join(j)] = 1
#                     else: dic[("".join(j))]+=1
#     print(dic)
#     print(max(dic))
