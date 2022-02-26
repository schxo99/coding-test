price = 3
money = 20
count = 4
# result = 10
def solution(price, money, count):
    sum = 0
    for i in range(count+1):
        sum+=price*i
    if money <= sum:
        result = sum-money
        return result
    else:
        return 0
solution(price, money, count)
