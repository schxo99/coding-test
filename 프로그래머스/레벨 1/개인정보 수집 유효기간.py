def solution(today, terms, privacies):
    result = []
    term = {}
    ty, tm, td = today.split('.')
    tdate = (((int(ty)-2000)*12)*28) + ((int(tm)-1)*28) + int(td)
    for i in range(len(terms)):
        a,b = terms[i].split()
        term[a] = b
    for i in range(len(privacies)): 
        date, m = privacies[i].split()
        yy, mm, dd = date.split('.')
        day = (((int(yy)-2000)*12)*28) + ((int(mm)-1)*28) + int(dd) + (int(term[m])*28)
        if day <= tdate:
            result.append(i+1)
    return result
