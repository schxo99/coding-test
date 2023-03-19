# 어렵진 않았지만 예외처리를 오래 생각했다. 벽에 맞고 튕기는 경우를 펵을 기준점으로 대칭이동 시켜 풀이를 하였고, 쳐야하는 공과 치는 공의 위치에 따라 칠 수 없는 경우가 있는걸 생각하는데 오래걸렸다. 
def solution(m, n, startX, startY, balls):
    result = []
    for i in balls:
        answer = []
        if startX == i[0] and startY > i[1] or startX != i[0]:
            answer.append((startX - i[0])**2 + (startY - (i[1] + (n - i[1])*2))**2)
        if startX == i[0] and startY < i[1] or startX != i[0]:
            answer.append((startX - i[0])**2 + (startY - (i[1]*-1))**2)
        if startY == i[1] and startX < i[0] or startY != i[1]:
            answer.append((startX - (i[0]*-1))**2 + (startY - i[1])**2)
        if startY == i[1] and startX > i[0] or startY != i[1]:
            answer.append((startX - (i[0] + (m - i[0])*2))**2 + (startY - i[1])**2)
        result.append(min(answer))
    return result
