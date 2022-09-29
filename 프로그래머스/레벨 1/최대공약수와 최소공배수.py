n = 3
m = 12

def solution(n, m):
    m_arr = []
    n_arr = []
    result = []
    for i in range(1, n+1):
        if n%i == 0:
            n_arr.append(i)
    
    for k in range(1, m+1):
        if m%k == 0:
            m_arr.append(k)
    answer = 0
    for j in range(len(n_arr)):
        if n_arr[j] in m_arr:
            if answer < n_arr[j]:
                answer = n_arr[j]
    result.append(answer)
    n_arr = []
    m_arr = []
    answer = 0
    mul = n*m
    for l in range(1, mul+1):
        if mul%(n*l) == 0:
            n_arr.append(n*l)
    for b in range(1, mul+1):
        if mul%(m*b) == 0:
            m_arr.append(m*b)
    for m in range(len(n_arr)):
        if n_arr[m] in m_arr:
            answer = n_arr[m]
            break
    print(result)
solution(n,m)