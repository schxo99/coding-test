def solution(numbers):
    sum_array, answer, sum = [],[], 0
    for i in range(len(numbers)-1):
        for k in range(i+1, len(numbers)):
            sum = numbers[i]+numbers[k]
            sum_array.append(sum)
    sum_array.sort()
    for j in sum_array:
        if j not in answer:
            answer.append(j)
    return answer