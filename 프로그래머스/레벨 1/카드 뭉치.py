def solution(cards1, cards2, goal):
    cards1.append('ㅁ')
    cards2.append('ㅁ')
    for i in goal:
        if i == cards1[0]:
            cards1.pop(0)       
        elif i == cards2[0]:
            cards2.pop(0)
        else: return "No"
    return "Yes"
