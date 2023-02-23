#동적 계획법의 bottom-up방식을 사용했다. 
def solution(n):
    if n == 1:
        return 1
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1] % 1234567
