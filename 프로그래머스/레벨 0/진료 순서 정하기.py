def solution(emergency):
    arr = len(emergency)*[0]
    for i in range(len(emergency)):
        arr[emergency.index(max(emergency))] = i+1
        emergency[emergency.index(max(emergency))] = 0
    return arr
