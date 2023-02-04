def solution(s):
    result = 0
    a = s
    if len(s) == 0 or len(s)%2 ==1:
        return 0
    for i in range(len(s)-1):
        for k in range(len(s)//2):
            a = a.replace('{}', '').replace('[]','').replace('()','')
        if a == '':
            result+=1
        s = (s+s[0])[1:]
        a = s
    return result
