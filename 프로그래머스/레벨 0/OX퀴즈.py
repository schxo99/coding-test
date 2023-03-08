def solution(quiz):
    result = []
    for i in range(len(quiz)):
        a,c = quiz[i].split('=')
        a = list(a.split(' '))
        if a[1] == '-':
            answer = int(a[0]) - int(a[2])
            if answer == int(c):
                result.append('O')
            else: result.append("X")
        else:
            answer = int(a[0]) + int(a[2])
            if answer == int(c):
                result.append("O")
            else: result.append("X")
    return result
