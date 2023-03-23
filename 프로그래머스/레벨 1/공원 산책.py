def solution(park, routes):
    for i in range(len(park)):
        park[i] = list(park[i])
        if "S" in park[i]:
            start = [i, park[i].index("S")]
    for i in routes:
        dr, ds = i.split()
        ds = int(ds)
        if dr == "S" and start[0] + ds <= len(park)-1:
            for k in range(1, ds+1):
                if park[start[0]+k][start[1]] == "X":
                    break
                if k == ds:
                    start[0] = start[0] + ds
        elif dr == "N" and start[0] - ds >= 0:
            for k in range(1, ds+1):
                if park[start[0]-k][start[1]] == "X":
                    break
                if k == ds:
                    start[0] = start[0] - ds
        elif dr == "E" and start[1] + ds <= len(park[0])-1:
            for k in range(1, ds+1):
                if park[start[0]][start[1]+k] == "X":
                    break
                if k == ds:
                    start[1] = start[1] + ds
        elif dr == "W" and start[1] - ds >= 0:
            for k in range(1, ds+1):
                if park[start[0]][start[1] - k] == "X":
                    break
                if k == ds:
                    start[1] = start[1] - ds
    return start
