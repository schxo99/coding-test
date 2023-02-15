def solution(board):
    result = 0
    for i in range(len(board)):
        board[i].insert(0,0)
        board[i].append(0)
    board = [[0]*len(board[0])] + board + [[0]*len(board[0])]
    for i in range(1, len(board)-1):
        for j in range(1, len(board[0])-1):
            if board[i][j] == 1:
                if board[i+1][j] != 1: board[i+1][j] = 2
                if board[i-1][j] != 1: board[i-1][j] = 2
                if board[i][j+1] != 1: board[i][j+1] = 2
                if board[i][j-1] != 1: board[i][j-1] = 2
                if board[i-1][j-1] != 1: board[i-1][j-1] = 2
                if board[i-1][j+1] != 1: board[i-1][j+1] = 2
                if board[i+1][j-1] != 1: board[i+1][j-1] = 2
                if board[i+1][j+1] != 1: board[i+1][j+1] = 2
    board.pop(0)
    board.pop(-1)
    for i in range(len(board)):
        board[i].pop(0)
        board[i].pop()
        result+=board[i].count(0)
    return result
