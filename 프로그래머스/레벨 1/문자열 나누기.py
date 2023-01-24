def solution(s):
    result = 0
    s = list(s)
    a,b = 1,0
    while len(s) >= 2:
        if s[0] == s[1]:
            a+=1
            del s[1]
        elif s[0] != s[1]: 
            b+=1
            del s[1]
        if a == b:
            result+=1
            a = 1
            b = 0
            del s[0]
    if len(s) == 1:
        result+=1
    return result
  
  ###############1 레벨 다풀었다...  2레벨 도전
