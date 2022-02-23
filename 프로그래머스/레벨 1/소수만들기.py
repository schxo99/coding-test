def func(sumv):
    for i in range(2, int(sumv / 2)):
        if sumv % i == 0:
            return False
    return True

def solution(nums):
    result = 0
    sumv = 0
    for i in range(len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                sumv = nums[i] + nums[j] + nums[k]
                if func(sumv):
                    result += 1
    return result