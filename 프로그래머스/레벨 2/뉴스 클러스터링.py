#이제 deque를 처음부터 사용하여 좀 더 효율성 높히는데 익숙고, 이번 문제는 예외처리에서 고생
from collections import deque
def solution(str1, str2):
    arr1, arr2 = [], []
    str1 = str1.upper()
    str2 = str2.upper()
    str1, str2 = deque(str1), deque(str2)
    same = 0
    print(str1, str2)
    for i in range(len(str1)-1):
        if (str1[0] + str1[1]).isalpha() == True:
            arr1.append(str1[0]+str1[1])
            str1.popleft()
        else:
            str1.popleft()
    for i in range(len(str2)-1):
        if (str2[0] + str2[1]).isalpha() == True:
            arr2.append(str2[0]+str2[1])
            str2.popleft()
        else:
            str2.popleft()
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            arr2.remove(arr1[i])
            same+=1
    if len(arr1) + len(arr2) == 0:
        return 65536        
    if same == 0:
        return 0
    else:
        return int((same/(len(arr1)+len(arr2))) * 65536)
