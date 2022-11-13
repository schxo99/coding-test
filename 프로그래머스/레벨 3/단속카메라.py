# def solution(routes):
#     answer = 0
#     carArr = []
#     for i in range(len(routes)):
#         carArr.append([])
#         for k in range(abs(abs(routes[i][0])- abs(routes[i][1]))+1):
#             carArr[i].append(routes[i][0]+k)
#     print(carArr)
#     return answer
# solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
# #result = 2

# def solution(routes):
#     answer = 0
#     carArr = []
#     for i in range(len(routes)):
#         # carArr.append([])
#         for k in range(abs(abs(routes[i][0])- abs(routes[i][1]))+1):
#             carArr.append(routes[i][0]+k)
#     print(carArr)
#     a = list(set(carArr))
#     print(a)
    
#     print(s1)

#     return answer
# solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])

# def solution(routes):
#     answer = 1
#     routes.sort(key = lambda x: x[1])
#     point = routes[0][1]
#     for i in range(1, len(routes)):
#         if routes[i][0] > point:
#             point = routes[i][1]
#             answer+=1
#     return ansswer

a = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
a.sort(key = lambda x: x[1])
print(a)