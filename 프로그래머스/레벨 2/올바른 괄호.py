def solution(s):
    for i in range(len(s)):
        a = s.replace('()', '')
        if a == s:
            break
        else:
            s = a
    if len(s) >= 1:
        return False
    else:
        return True
