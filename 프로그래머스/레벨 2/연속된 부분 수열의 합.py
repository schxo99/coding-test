# 47.1%
# def solution(sequence, k):
#     result, test = [0,0], [0,0]
#     if sequence[0] == k:
#         return [0,0]
#     for index, num in enumerate(sequence):
#         hap = num
#         if hap == k:
#             return [index,index]
#         for i in range(index+1, len(sequence)):
#             hap += sequence[i]
#             if hap == k:
#                 test = [index, i]
#                 if result == [0,0] or result[1] - result[0] > test[1] - test[0]:
#                     result = test[::]
#             elif hap > k:
#                 break
#     return result

# 52%
# def solution(arr, k):
#     result, test = [0, 0], [0, 0]
#     hap_arr = [arr[0]]
#     if arr[0] == k:
#         return [0,0]
#     for i in range(1, len(arr), 1):
#         hap_arr.append(hap_arr[-1] + arr[i])
#     for index, arr_num in enumerate(hap_arr):
#         num = arr_num
#         i = 0
#         while num > k:
#             num -= arr[i]
#             i+=1
#         if num == k:
#             test = [i, index]
#             if result == [0,0] or result[1] - result[0] > test[1] - test[0]:
#                 result = test[::]
#     return result

def solution(arr, k):
    result, test = [0,0], [0,0]
    hap = 0
    if arr[0] == k:
        return result
    for index, num in enumerate(arr):
        hap += num
        while hap > k:
            hap -= arr[test[0]]
            test[0]+=1
        if hap == k:
            test[1] = index
            if result == [0,0] or result[1] - result[0] > test[1] - test[0]:
                result = test[::]
    return result
