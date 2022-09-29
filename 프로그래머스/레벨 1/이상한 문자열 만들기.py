s = "try hello world"
# def solution(s):
#     s=s.lower()
#     s=s.split()
#     arr=[]
#     for i in range(len(s)):
#         arr.append('')
#         arr[i] = list(s[i])
#     for j in range(len(arr)):
#         for k in range(len(arr[j])):
#             if k %2 == 0:
#                 arr[j][k] = arr[j][k].upper()
#         arr[j] = ''.join(arr[j])
#     result = ' '.join(arr)
#     print(result)
# solution(s)


# a = [1,'a','b','c',4]
# a[1:3] = []
def solution(s):
    result = ''
    s = s.lower()
    s = list(s.split(' '))
    for i in s:
        for k in range(len(i)):
            if k%2 == 0:
                result+=i[k].upper()
            else:
                result+=i[k]
        result+=' '
    print(result)

solution(s)