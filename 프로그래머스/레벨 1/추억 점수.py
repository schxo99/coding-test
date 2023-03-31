def solution(name, yearning, photo):
    result = []
    for i in photo:
        hap = 0
        for k in i:
            if k in name:
                hap += yearning[name.index(k)]
        result.append(hap)
    return result
