def solution(survey, choices):
    result = ''
    named = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    arr = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0,}
    for i in range(len(choices)):
        q = list(survey[i])
        choice = choices[i] - 4
        if choice < 0:
            arr[q[0]] += abs(choice)
        elif choice > 0:
            arr[q[1]] += abs(choice)
    for i in range(0, len(named), 2):
        if arr[named[i]] >= arr[named[i+1]]:
            result+=named[i]
        else:
            result+=named[i+1]
    return result
