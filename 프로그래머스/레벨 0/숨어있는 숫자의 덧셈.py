def solution(my_string):
    my_string+='A'
    result = 0
    hap = ''
    my_string = list(my_string)
    for i in my_string:
        if i.isdigit():
            hap += str(i)
        elif len(hap) >= 1: 
            result += int(hap)
            hap = ''
    return result
