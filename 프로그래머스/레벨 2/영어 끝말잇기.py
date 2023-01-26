import math
def solution(n, words):
    arr = []
    arr.append(words[0])
    for i in range(1, len(words)):
        if words[i] not in arr and arr[-1][-1] == words[i][0] and len(words[i]) > 1:
            arr.append(words[i])
            result = True
        else:
            result = False
            break
    if result == True and i+1 == len(words):
        return [0,0]
    else:
        who = (i + 1) % n
        if who == 0:
            who = n
        time = math.ceil((i+1) / n)
        return [who, time]
