##예외 처리하는데 생각할게 많았다.
def solution(board):
    lineo, linex = 0, 0
    counto, countx = 0, 0
    for i in range(len(board)):
    #가로빙고
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][2] == "O":
                lineo+=1
            elif board[i][2] == 'X': linex+=1
    #세로빙고
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[2][i] == "O":
                lineo+=1
            elif board[2][i] == "X": linex+=1
    #대각빙고
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[2][2] == "O":
            lineo+=1
        elif board[2][2] == "X": linex += 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[2][0] == "O":
            lineo+=1
        elif board[2][0] == "X": linex += 1
    for i in board:
        for k in i:
            if k == "O":
                counto += 1
            elif k == "X":
                countx += 1
    print(lineo, linex, counto, countx)
    # 잘못된 것 판별하기
    if countx > counto:
        return 0
    if counto - countx > 1:
        return 0
    if lineo >= 1 and linex>=1:
        return 0
    if lineo >= 1 and countx >= counto:
        return 0
    if linex >= 1 and counto > countx:
        return 0
    return 1
