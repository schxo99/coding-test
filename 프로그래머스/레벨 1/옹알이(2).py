def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    result = 0
    for i in range(len(babbling)):
        for k in word:
            if k in babbling[i]:
                babbling[i] = babbling[i].replace(k*2,'z')
                babbling[i] = babbling[i].replace(k, '0')
    for i in range(len(babbling)):
        if babbling[i].isdigit() == True:
            result +=1
    return result
