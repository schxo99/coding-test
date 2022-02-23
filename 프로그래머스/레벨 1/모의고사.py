def solution(answers):
    score,answer = [0, 0, 0],[]
    student_answers = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    for j in range(3):
        student_answers[j]=student_answers[j]*(int(len(answers)/len(student_answers[j]))+1)
    for k in range(3):
        for i in range(len(answers)):
            if student_answers[k][i] == answers[i]:
                score[k]+=1
    max_score = max(score)
    for n in range(3):
        if max_score == score[n]:
            answer.append(n+1)
    answer.sort()
    return answer