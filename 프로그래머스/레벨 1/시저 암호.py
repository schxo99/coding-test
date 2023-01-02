def solution(s, n):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].isalpha() == True and arr[i].isupper() == True:
            a = ord(arr[i])
            if a + n > 90:
                a= a + n - 26
            else:
                a+=n
            arr[i] = chr(a)
        elif arr[i].isalpha() == True and arr[i].islower() == True:
            a = ord(arr[i])
            if a + n > 122:
                a = a + n - 26
            else:
                a+=n
            arr[i] = chr(a)
    return ''.join(arr)
