def solution(dots):
    if ((dots[0][1] - dots[1][1])/(dots[0][0] - dots[1][0])) == ((dots[2][1] - dots[3][1])/(dots[2][0]-dots[3][0])):
        return 1
    elif ((dots[0][1] - dots[2][1])/(dots[0][0] - dots[2][0])) == ((dots[1][1] - dots[3][1])/(dots[1][0]-dots[3][0])):
        return 1
    elif ((dots[3][1] - dots[0][1])/(dots[3][0] - dots[0][0])) == ((dots[2][1] - dots[1][1])/(dots[2][0]-dots[1][0])):
        return 1
    else: return 0

 ## 런타임 2개
# def solution(dots):
#     dots.sort()
#     a = abs((dots[0][1] - dots[2][1])) / abs((dots[0][0] - dots[2][0]))
#     b = abs((dots[1][1] - dots[3][1])) / abs((dots[1][0] - dots[3][0]))
#     print(a)
#     print(b)
#     if a == b:
#         return 1
#     else: return 0
