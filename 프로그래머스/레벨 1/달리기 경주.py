# 딕셔너리를 활용한 풀이
def solution(players, callings):
    player_rank = {player : rank for rank, player in enumerate(players)}
    rank_player = {rank : player for rank, player in enumerate(players)}
    for name in callings:
        i = player_rank[name]
        player2 = rank_player[i-1]
        player_rank[player2], player_rank[name] = i, i-1
        rank_player[i], rank_player[i-1] = player2, name
    result = list(rank_player.values())
    return result

# for문을 사용해서 추월한 사람의 인덱스를 가지고 연산했는데 시간초과.
# def solution(players, callings):
#     for name in callings:
#         i = players.index(name)
#         players[i-1], players[i] = players[i], players[i-1]
#     return players
