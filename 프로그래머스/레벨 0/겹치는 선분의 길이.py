## 최소 지점부터 최고 지점까지 겹치는 부분이 있으면 1씩 더해가면서 탐색.. 
def solution(lines):
    lines.sort()
    s = lines[0][0]
    m = 0
    result = 0
    for i in lines:
        if m <= i[1]:
            m = i[1]
    for i in range(s, m-s):
        ch = 0
        if lines[0][0] <= i and lines[0][1] > i:
            ch +=1
        if lines[1][0] <= i and lines[1][1] > i:
            ch +=1
        if lines[2][0] <= i and lines [2][1] > i:
            ch +=1
        if ch >= 2:
            result+=1
        ch = 0
    return result

##값을 연산해서 겹치면 값을 구하는 식의 풀이 2개 런타임
# def solution(lines):
#     lines.sort()
#     result = 0
#     print(lines)
#     if lines[0][1] > lines[1][0]:
#         result += abs(lines[1][0] - lines[0][1])
#     if lines[1][1] > lines[2][0]:
#         result += abs(lines[2][0] - lines[1][1])
#     if lines[0][1] >lines[2][0]:
#         if lines[0][1] > lines[1][0]:
#             result += abs(lines[2][0] - lines[0][1]) - abs(lines[1][0] - lines[0][1])
#         else: result += abs(lines[2][0] - lines[0][1])
#     return result
