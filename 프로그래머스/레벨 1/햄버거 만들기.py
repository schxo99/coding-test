def solution(ingredient):
    arr = []
    result = 0
    for i in range(len(ingredient)):
        arr.append(ingredient[i])
        if len(arr)>= 4:
            if arr[-4:] == [1,2,3,1]:
                arr.pop()
                arr.pop()
                arr.pop()
                arr.pop()
                result+=1
    return result
    
solution([2, 1, 1, 2, 3, 1, 2, 3, 1])