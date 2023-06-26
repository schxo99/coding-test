def solution(rank, attendance):
    arr = []
    for i in zip(rank, attendance):
        if i [1] == True:
            arr.append(list(i))
    arr.sort(key = lambda x:x[0])
    return (rank.index(arr[0][0]) * 10000) + (rank.index(arr[1][0]) * 100) + rank.index(arr[2][0])
