def solution(picture, k):
    result = []
    for i in picture:
        line = ""
        for j in i:
            line += j * k
        for _ in range(k):
            result.append(line)
    return result
