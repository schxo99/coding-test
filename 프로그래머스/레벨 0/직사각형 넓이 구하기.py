def solution(dots):
    dots.sort()
    a = abs(dots[0][1] - dots[1][1])
    b = abs(dots[0][0] - dots[2][0])
    return a * b
