def solution(s):
    if len(s)%2 ==1:
        a = int(len(s)/2)
        return s[a]
    if len(s)%2 == 0:
        a = int(len(s)/2)
        bb = s[a-1]+s[a]
        return bb
