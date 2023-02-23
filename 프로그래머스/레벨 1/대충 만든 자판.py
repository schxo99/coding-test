def solution(keymap, targets):
    result = []
    for i in range(len(targets)):
        ck = 0
        for j in range(len(targets[i])):
            arr = []
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    arr.append(keymap[k].index(targets[i][j]))
                else: pass
            if len(arr) == 0:
                ck = -1
                break
            else: 
                ck += min(arr) + 1
        result.append(ck)
    return result
