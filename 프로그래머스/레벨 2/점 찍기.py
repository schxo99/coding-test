#원의 방정식 공식을 활용하여 풀었다.
def solution(k, d):
    result = 0
    for i in range(0, d+1, k):
        y = int((d**2 - i**2)**0.5)
        if y % k != 0:
            y-=1
        result += y//k+1
    return result

# 시간 초과 아마 이중 반복문으로 인하여 효율성이 떨어지는 것 같다.
# def solution(k, d):
#     result = 0
#     for i in range(0, d+1, k):
#         for j in range(0, d+1, k):
#             if (((0-i)**2) + ((0-j)**2))**0.5 <= d:
#                 result+=1
#             else: break
#     return result
