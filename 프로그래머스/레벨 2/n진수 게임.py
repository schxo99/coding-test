def fa(num, n):
    hap = ""
    char = "0123456789ABCDEF"
    while True:
        num, mod = divmod(num, n)
        hap+=char[mod]
        if num == 0: break
    hap = list(hap)
    hap.reverse()
    hap = ''.join(hap)
    return hap

def solution(n, t, m, p):
    num, answer, result = 0, "", ""
    while num <= t*m:
        answer += fa(num, n)
        num+=1
    for i in range(p-1, len(answer), m):
        if len(result)>=t:
            break
        result+=answer[i]
    return result
        
    
#n = 진법
#t = 미리 구할 숫자의 갯수
#m = 게임에 참가하는 인원
#p = 튜브의 순서
