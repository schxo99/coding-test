def solution(babbling):
    string = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for k in string:
            babbling[i] = babbling[i].replace(k, '1')
    result = 0
    for i in babbling:
        if i.isdigit() == True:
            result+=1
    return result
