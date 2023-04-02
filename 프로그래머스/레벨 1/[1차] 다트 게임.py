def solution(dartResult):
    dartResult = dartResult.replace('10', 'R')
    dartResult = list(dartResult)
    array = []
    answer = 0
    for i in dartResult:
        if i.isdigit() or i == 'R':
            if i.isdigit():
                array.append(int(i))
            elif i == 'R':
                array.append(10)
        elif i == 'D':
            array[-1] = array[-1]**2
        elif i == 'T':
            array[-1] = array[-1]**3
        elif i == '*':
            if len(array) >= 2:
                array[-1] = array[-1]*2
                array[-2] = array[-2]*2
            else: 
                array[-1] = array[-1]*2
        elif i == '#':
            array[-1] = array[-1]*-1
    answer = sum(array)
    return answer
