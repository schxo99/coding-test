nums = [3,3,3,2,2,4]
def solution(nums):
    result = []
    n = len(nums)/2
    nums.sort()
    result.append(nums[0])
    for num in range(1, len(nums)):
        if len(result) == n: break
        elif result[-1] != nums[num]:
            result.append(nums[num])
            print(result)
    print(result)
    # answer = len(result)
    # return answer
solution(nums)