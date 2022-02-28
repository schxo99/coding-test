def solution():
    arr = [1,1,3,3,0,1,1]
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    print(answer)
    # return answer
solution()