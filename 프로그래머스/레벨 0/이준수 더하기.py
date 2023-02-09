def solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2, 2)
    c = a+b
    result = bin(c)
    return result[2:]
