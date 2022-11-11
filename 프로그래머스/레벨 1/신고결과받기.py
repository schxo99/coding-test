import collections
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)
    
    for i in report:
        a,b = i.split(' ')
        reportHash[a].add(b)
        stoped[b]+=1
    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user]>=k:
                mail+=1
        answer.append(mail)
    return answer