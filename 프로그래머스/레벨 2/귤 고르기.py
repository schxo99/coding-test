def solution(k, tangerine):
    tangerine.sort(reverse = True)
    settangerine = list(set(tangerine))
    arr = {}
    for i in settangerine:
        arr[i] = 0
    for i in tangerine:
        arr[i] += 1
    value = list(arr.values())
    value = sorted(value, reverse = True)
    for i in range(len(value)):
        k-=value[i]
        if k <= 0:
            return i+1
            break
