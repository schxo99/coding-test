def solution(arr, queries):
    result = []
    for a, b, c in queries:
        index = -1
        for i in range(len(arr)):
            if a<=i and i<=b and c < arr[i]:
                if index == -1:
                    index = arr[i]
                elif index > arr[i]:
                    index = arr[i]
        result.append(index)
    return result
                
