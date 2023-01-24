#2월은 29일까지 있음
def solution(a,b):
    hap = 0
    zero = [4,6,9,11]
    one = [1,3,5,7,8,10,12]
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    for i in range(1, a, 1):
        if i in zero:
            hap+=30
        elif i in one:
            hap+=31
        elif i == 2:
            hap +=29
    hap = hap + b -1
    hap = hap % 7
    return week[hap]
