## 문제 이해는 했는데 while 조건을 잘못 작성하여 오래 걸렸다..
from string import ascii_uppercase
from collections import deque
def solution(msg):
    dic, result, num, string, k = {}, [], 27, '', 0
    for i in range(len(ascii_uppercase)):
        dic[ascii_uppercase[i]] = i+1
    msg = deque(list(msg))
    while True:
        if string == '' or string in dic and len(msg) > 0:
            string += msg[0]
            msg.popleft()
        else:
            if string in dic:
                result.append(dic[string])
                if len(msg) == 0: break
            else:
                dic[string] = num
                num+=1
                if string == '':
                    break
                else:
                    result.append(dic[string[:-1]])
                    string = string[-1]
    return result
