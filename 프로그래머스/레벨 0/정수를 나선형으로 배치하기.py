def right(result, x, y, ch, num):
    while y < len(result[0]) and result[x][y] == 0:
        result[x][y] = num
        num+=1
        y+=1
    return result, x+1, y-1, ch, num

def left(result, x, y, ch, num):
    while 0 <= y and result[x][y] == 0:
        result[x][y] = num
        y-=1
        num+=1
    return result, x-1, y+1, ch, num
    
def top(result, x, y, ch, num):
    while 0 <= x and result[x][y] == 0:
        result[x][y] = num
        num+=1
        x-=1
    return result, x+1, y+1, ch, num
        
def down(result, x, y, ch, num):
    while x < len(result) and result[x][y] == 0:
        result[x][y] = num
        x+=1
        num+=1
    return result, x-1, y-1, ch, num

def solution(n):
    if n == 1:
        return [[1]]
    result = [[0]*n for _ in range(n)]

    x, y = 0, 0
    ch, num = 0, 1
    while ch == 0:
        if result[x][y] != 0:
            ch = 1
        result, x, y, ch, num = right(result, x, y, ch, num)
        result, x, y, ch, num = down(result, x, y, ch, num)
        result, x, y, ch, num = left(result, x, y, ch, num)   
        result, x, y, ch, num = top(result, x, y, ch, num)
    return result
    
