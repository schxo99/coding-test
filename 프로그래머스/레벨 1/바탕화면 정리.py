def solution(wallpaper):
    sx, sy, fx, fy = 50, 50, 0, 0
    for i in range(len(wallpaper)):
        for k in range(len(wallpaper[0])):
            if wallpaper[i][k] == '#':
                sx = min(sx, i)
                sy = min(sy, k)
                fx = max(fx, i+1)
                fy = max(fy, k+1)
    return [sx,sy,fx,fy]
