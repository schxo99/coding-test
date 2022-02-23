def solution(numbers):
    full_numbers = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        full_numbers.remove(numbers[i])
        answer = sum(full_numbers)
    return answer