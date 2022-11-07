def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2)
    r_answer = list(answer)
    r_answer.reverse()
    r_answer=''.join(r_answer)
    result = answer+'0'+r_answer
    return result
    