## 풀이 후 다른 사람을 코드에서 gcd() 확인. gcd()함수는 인자로 들어온 숫자들의 최대 공약수를 반환. 따라서 기약분수로 편하게 한줄 코딩이 가능하다. import math
def solution(a, b):
    for i in range(a, 1, -1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
    arr = []
    while True:
        c = b
        if b % 2 == 0:
            b //= 2
        if b % 5 == 0:
            b //= 5
        if c == b:
            break
    if b == 1:
        return 1
    else: return 2
