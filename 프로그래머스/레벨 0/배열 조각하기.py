def solution(arr, query):
    for j, i in enumerate(query):
        if j % 2 == 0:
            arr = arr[:i+1]    
        else:
            arr = arr[i:]
    return arr
