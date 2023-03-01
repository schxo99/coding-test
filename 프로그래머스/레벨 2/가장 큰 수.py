#예제에서 주어지는 가장 큰 수가 4자리기에 str형식의 요소들을 다 4자리 이상으로 만들고 정렬 후 result 반환
def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    result = ''
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 4
    numbers.sort(reverse = True)
    for i in range(len(numbers)):
        result += numbers[i][:len(numbers[i])//4]
    return result
    
# def solution(numbers):
#     result = ''
#     char = list(map(str, numbers))
#     char.sort(reverse = True)
#     for _ in range(len(char)):
#         if len(char) >= 2:
#             if char[0] + char[1] >= char[1] + char[0]:
#                 result += char[0]
#                 char.pop(0)
#             else:
#                 result+= char[1]
#                 char.pop(1)
#         else:
#             result+= char[0]
#             break
#     return result
