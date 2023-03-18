def solution(x):
    sumV = 0
    for i in str(x):
        sumV += int(i)
    return True if x % sumV == 0 else False
