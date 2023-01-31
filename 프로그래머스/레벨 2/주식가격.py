def solution(prices):
    result = []
    for i in range(len(prices)):
        time = 0
        for k in range(i+1, len(prices)):
            time+=1
            if prices[i] > prices[k]:
                break
        result.append(time)      
    return result
