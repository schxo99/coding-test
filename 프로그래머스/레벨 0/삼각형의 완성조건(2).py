def solution(sides):
    a = sum(sides)
    b, c, result = 1, 0, 0
    while True:
        if b < a and sides[0] < b + sides[1] and sides[1] < b + sides[0]:
            result+=1
        b+=1
        c+=1
        if c > a:
            break
    return result
