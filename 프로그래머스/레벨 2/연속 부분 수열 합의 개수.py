def solution(elements):
    elements = elements*2
    arr = []
    for i in range(len(elements)//2):
        for k in range(len(elements)//2):
            a = sum(elements[i:i+k])
            arr.append(a)
    arr = set(arr)
    return len(arr)
