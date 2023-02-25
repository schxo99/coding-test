## 첫 dfs문제 스스로 풀이를 해봤는데 전역변수에서 조금 어려움을 겪었다.
result = 0
def dfs(numbers, target, level, num):
    global result
    if level == len(numbers):
        if num == target:
            result+=1
        return 
    elif level < len(numbers):
        dfs(numbers, target, level+1, num+numbers[level])
        dfs(numbers, target, level+1, num-numbers[level])

def solution(numbers, target):
    level, num = 0, 0
    dfs(numbers, target, level, num)
    return result
