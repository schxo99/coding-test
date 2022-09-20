text = 'lleoH'
anagram = [4,2,0,1,3]
sw = False
def solution(text, anagram, sw):
    arr = []
    em = []
    for i in text:
        arr.append(i)
    print(arr)
    if sw == True:
        for i in range(len(arr)):
            em.append('')
        for k in range(len(anagram)):
            em[anagram[k]] = arr[k]
    
    else:
        for i in range(len(arr)):
            em.append('')
        for k in range(len(anagram)):
            em[k] = arr[anagram[k]]
    
    em = ''.join((em))
    return(em)




solution(text, anagram, sw)