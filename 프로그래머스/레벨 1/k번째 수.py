def solution(array, commands):
    array_list, result = [], []
    for i in range(len(commands)):
        array_list.append(array[(commands[i][0]-1):commands[i][1]])
        array_list[i].sort()
    for j in range(len(commands)):
        a = commands[j][2]
        result.append(array_list[j][a-1])
    return result