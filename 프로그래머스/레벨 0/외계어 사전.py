def solution(spell, dic):
    spell.sort()
    for i in range(len(dic)):
        a = sorted(list(dic[i]))
        if a == spell:
            return 1
    return 2
