def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    result = 0
    ch = []
    for i in range(len(cities)):
        a = cities[i].lower()
        if a in ch:
            result+=1
            ch.append(ch[ch.index(a)])
            ch.pop(ch.index(a))
        else:
            if len(ch) < cacheSize:
                ch.append(a)
            else:
                ch.pop(0)
                ch.append(a)
            result+=5
    return result
