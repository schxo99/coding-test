def solution(lottos, win_nums):
    low = 0
    answer = []
    for i in range(6):
        if lottos[i] in win_nums:
            low += 1
    b = lottos.count(0)
    high = low + b
    answer.append(high)
    answer.append(low)
    for k in range(2):
        if answer[k] == 6:
            answer[k]=1
        elif answer[k] == 5:
            answer[k]=2
        elif answer[k] == 4:
            answer[k]=3
        elif answer[k] == 3:
            answer[k]=4
        elif answer[k] == 2:
            answer[k]=5
        else :
            answer[k]=6
    return answer