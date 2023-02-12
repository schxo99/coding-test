def solution(balls, share):
    s, m, a= 1, 1, 1
    for i in range(1, balls+1):
        s *= i
    for k in range(1, share+1):
        m *= k
    for j in range(1, (balls - share)+1):
        a *= j
    return s/(m*a)
