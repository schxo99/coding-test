# 변수 선언 시 그 변수를 다른 변수에 할당하면 같은 주소 값을 사용하기에 변수 하나를 수정하면 다른 변수도 같이 수정된다.. 기초적인 지식인데 잊고 있었다.. 리스트로 값을 붙혀넣거나 
#copy를 사용하면 된다. 너무 1차원적인 풀이
def solution(dirs):
    dirs = list(dirs)
    load = []
    move = [0,0]
    for i in dirs:
        street = []
        if i == "U":
            if move[1]+1 <= 5:
                street.append(move)
                move = move[:]
                move[1]+=1
                street.append(move)
                street.sort()
                if street not in load:
                    load.append(street)
                
        elif i == "D":
            if move[1]-1 >= -5:
                street.append(move)
                move = move[:]
                move[1]-=1
                street.append(move)
                street.sort()
                if street not in load:
                    load.append(street)
            
        elif i == "R":
            if move[0]+1 <= 5:
                street.append(move)
                move = move[:]
                move[0]+=1
                street.append(move)
                street.sort()
                if street not in load:
                    load.append(street)
            
        elif i == "L":
            if move[0]-1 >= -5:
                street.append(move)
                move = move[:]
                move[0]-=1
                street.append(move)
                street.sort()
                if street not in load:
                    load.append(street)
    return len(load)
