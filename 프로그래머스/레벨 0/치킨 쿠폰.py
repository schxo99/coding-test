def solution(chicken):
    cup = chicken
    result = 0
    while True:
        result = result+(cup//10)
        cup = (cup % 10) + (cup // 10)
        if cup < 10:
            return result
