##공식화? 해서 풀이
def solution(num, total):
    arr = []
    if total % num == 0:
        a = total // num
        b = a - ((num-1)/2)
        for i in range(num):
            arr.append(b+i)
    else:
        a = total // num
        b = a - ((num//2) - 1)
        for i in range(num):
            arr.append(b+i)
    return arr
##기존에는 전체 탐색해서 맞으면 중지하는 코드.. 마지막 2개가 런타임 오류 남
# def solution(num, total):
#     for i in range(-5, total+1):
#         hap = 0
#         arr = []
#         for k in range(i, i+num):
#             hap += k
#             arr.append(k)
#         # print(hap, arr)
#         if hap == total:
#             return arr
