def solution(number):
    sum = 0
    result = 0
    for i in range(len(number)):
        for k in  range(i+1, len(number)):
            for j in range(k+1, len(number)):
                sum = number[i]+number[k]+number[j]
                if sum == 0:
                    result+=1
                sum = 0
    print(result)
solution([-2, 3, 0, 2, -5])