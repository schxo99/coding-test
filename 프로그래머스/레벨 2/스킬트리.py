def solution(skill, skill_trees):
    aa = list(skill)
    result = 0
    for i in range(len(skill_trees)):
        test = list(skill_trees[i])
        bb = list(skill)
        for k in test:
            if k in aa and k == bb[0]:
                bb.pop(0)
            elif k in aa and k!= bb[0]:
                break  
            if k == test[-1]:
                result+=1
    return result
