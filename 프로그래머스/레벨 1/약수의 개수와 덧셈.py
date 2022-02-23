def solution(left, right):
    answer, numbers, result = 0, [], 0
    for i in range(left, right+1):
        numbers.append(i)
    for k in range(len(numbers)):
        for j in range(1, numbers[k]+1):
            if numbers[k]%j == 0:
                result+=1
        if result%2 == 0:
            answer+=numbers[k]
        else :
            answer-=numbers[k]
        result =0
    return answer