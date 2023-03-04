#분으로 변경하여 계산
def solution(book_time):
    arr, result = [], 1
    for i in range(len(book_time)):
        start, end = book_time[i]
        start = (int(start[:2]) * 60) + int(start[-2:]) 
        end = ((int(end[:2]) * 60) + int(end[-2:])) + 10
        book_time[i] = [start, end]
    book_time.sort()
    arr.append(book_time[0][1])
    for i in range(1, len(book_time)):
        for k in range(len(arr)):
            if arr[k] <= book_time[i][0]:
                arr[k] = book_time[i][1]
                break
            if k == len(arr)-1:
                arr.append(book_time[i][1])
                result+=1
                break
    return result
