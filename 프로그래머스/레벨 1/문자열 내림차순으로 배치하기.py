s = "Zbcdefg"
def solution(s):
    s = list(s)
    print(s)
    s.sort(reverse = True)
    print(s)
    answer = ''.join(s)
    print(answer)
    # return answer
solution(s)