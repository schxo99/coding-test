#딕셔너리 사용해서 푸는 문제 같은데 이렇게도 풀 수 있을 것 같아 해봤다.
def solution(want, number, discount):
    arr, result = [], 0
    for i in range(len(want)):
        for k in range(number[i]):
            arr.append(want[i])
    arr.sort()
    for i in range(len(discount)-9):
        day = sorted(discount[i:i+10])
        if arr in day or arr == day:
            result+=1
    return result
        
# def solution(want, number, discount):
#     items = {}
#     for i in range(len(want)):
#         items[want[i]] = number[i]
#     # print(items)
#     for i in range(len(discount)):
#         print(discount[i])
#바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개
#치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나
