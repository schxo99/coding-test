def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort(reverse = True)
    print(sizes)
    a = 0
    for i in range(len(sizes)):
        if sizes[i][0] >= a:
            a = sizes[i][0]
    b = 0
    for i in range(len(sizes)):
        if sizes[i][1] >= b:
            b = sizes[i][1]
    return a*b
