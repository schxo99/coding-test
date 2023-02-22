## divmod 함수는 n/k의 몫과 나머지를 구해서 각각의 변수에 대입해준다.
## 지금까지 n이하의 수를 반복문돌려서 소수를 판별했지만 제곱수를 이용하면 더 빠르게 구할 수 있는 것을 알게되었다. 루트 n이하의 소수로 나누어 떨어지지 않는다면 소수이다.
def solution(n, k):
    answer = 0
    result = ''
    while True:
        n, b = divmod(n,k)
        result+=str(b)
        if n < k:
            result+= str(n)
            break
    result = list(result)
    result.reverse()
    result = ''.join(result)
    result = result.split("0")
    for i in range(len(result)):
        if result[i] == "" or result[i] == "1":
            pass
        else:
            if result[i] == '2':
                answer +=1
            else:
                a = int(result[i])
                for j in range(2, int(a**0.5)+2):
                    if a % j == 0:
                        break
                    if j == int(a**0.5)+1:
                        answer+=1
    return answer
