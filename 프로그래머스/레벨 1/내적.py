def solution(a,b):
    answer =0
    for i in range(len(a)):
        sum = a[i]*b[i]
        answer+=sum
    return answer