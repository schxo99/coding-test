#효율성에서 터져버림
def solution(A,B):
    sum = 0
    for i in range(len(A)):
        a = min(A)
        b = max(B)
        sum+=a*b
        A.remove(a)
        B.remove(b)
    return sum
  
  #효율성 통과
  def solution(A,B):
    sum = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sum+= A[i] * B[i]
    return sum
