def solution(numbers):
    result = []
    for i in numbers:
        bit = list("0" + bin(i)[2:])
        index = "".join(bit).rfind("0")
        bit[index] = "1"
        if i % 2 == 1:
            bit[index+1] = "0"
        result.append(int("".join(bit), 2))
    return result

# 3개 오류
# def changeBit(num):
#     bit = ""
#     while num > 0:
#         num, mod = divmod(num, 2)
#         bit += str(mod)
#     bit = list(bit)
#     return bit

# def solution(numbers):
#     result = []
#     for i in numbers:
#         bit = changeBit(i)
#         if bit[0] == "0":
#             bit[0] = "1"
#         elif bit[0] == "1":
#             bit.append("0")
#             for i in range(len(bit)):
#                 if bit[i] == "0":
#                     bit[i] = "1"
#                     bit[i-1] = "0"
#                     break
#         bit.reverse()
#         bit = ''.join(bit)
#         result.append(int(bit, 2))
#     return result
