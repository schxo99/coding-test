from itertools import permutations
def solution(numbers):
    arr = []
    result = 0
    numbers = list(numbers)
    for i in range(len(numbers)):
        for i  in permutations(numbers, i+1):
            if int(''.join(i)) not in arr and int(''.join(i)) != 0 and int(''.join(i)) != 1:
                arr.append(int("".join(i)))
    for i in range(len(arr)):
        if arr[i] <= 3:
            result+=1
        else:
            TF = True
            for k in range(2, arr[i]):
                if arr[i] % k ==0:
                    TF = False
                    break
            if TF == True:
                result+=1
    return result
