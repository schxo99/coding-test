def solution(triangle):
    for i in range(len(triangle)-1):
        arr = triangle.pop()
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                triangle[-1][k] += arr[k]
            elif arr[k] <= arr[k+1]:
                triangle[-1][k] += arr[k+1]
    return triangle[0][0]
