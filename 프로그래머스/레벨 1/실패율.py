def solution(N, stages):
    stage = {}
    result = {}
    answer = []
    for i in range(1, N+2):
        stage[i] = stages.count(i)
    print(stage)
    
    for i in range(1, N+2):
        hap = 0
        for k in range(i, N+2):
            hap += stage[k]
        if hap == 0 or stage[i] == 0:
            stage[i] = 0
        else:
            stage[i] = stage[i]/hap
    del stage[N+1]
    result = sorted(stage.items(), key = lambda x:x[1], reverse = True)
    for i in range(len(result)):
        answer.append(result[i][0])
    return answer
  
  #람다함수 공부해야겠다.
