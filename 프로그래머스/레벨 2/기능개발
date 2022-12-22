def solution(progresses, speeds):
    arr = []
    while True:
        hap = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        for k in range(len(progresses)):
            if progresses[0] >= 100:
                del progresses[0]
                del speeds[0]
                hap+=1
            else: break
        if hap > 0:
            arr.append(hap)
        if progresses == []:
            break
    return arr
    
