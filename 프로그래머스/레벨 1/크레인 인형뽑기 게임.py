1년 동안 푼 문제 성공! 문제 이해를 잘못 했었다..
# def solution(board, moves):
#     newboard = []
#     result = []
#     c = 0
#     for i in range(len(board)):
#         c+= sum(board[i])
#     if c == 0:
#         return 0
#     else:
#         for i in range(len(board)):
#             newboard.append([])
#         for i in range(len(board)):
#             for k in range(len(board)):
#                 if board[i][k] != 0:
#                     newboard[k].append(board[i][k])
#         for i in moves:
#             i-=1
#             if len(newboard[i]) == 0:
#                 a=0
#             else:
#                 result.append(newboard[i][0])
#                 del newboard[i][0]
#         answer = []
#         answer.append(result[0])
#         del result[0]
#         b = 0
#         for i in result:
#             if answer[-1] == i:
#                 del answer[-1]
#                 b+=2
#             else:
#                 answer.append(i)
#         return b

def solution(board, moves):
    arr = []
    result = 0
    for i in range(len(moves)):
        moves[i] = moves[i]-1
    for i in range(len(moves)):
        for k in range(len(board)):
            if board[k][moves[i]] != 0:
                arr.append(board[k][moves[i]])
                board[k][moves[i]] = 0
                break
        if len(arr) >=2 and arr[-1] == arr[-2]:
            arr.pop()
            arr.pop()
            result+=2
    return result
