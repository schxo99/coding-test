def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer

#배열 다 구하니 시간초과
# def solution(n, left, right):
#     ch = 0
#     result = ''
#     string = ''
#     for i in range(1, n+1):
#         string = str(i)*i
#         for k in range(i+1, n+1):
#             string += str(k)
#         result+=str(string)
#     # print(list(result))
#     result = result[left:right+1]
#     return list(map(int, result))
