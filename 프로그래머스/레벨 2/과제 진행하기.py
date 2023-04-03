def solution(plans):
    result, wait = [], []
    for i in range(len(plans)):
        name, start, use = plans[i]
        ti, mi = start.split(':')
        plans[i] = [int(ti) * 60 + int(mi), int(use), name]
    plans.sort(key = lambda x:x[0])
    now = plans[0][0]
    while True:
        if len(plans) > 1:
            if plans[0][0] + plans[0][1] <= plans[1][0]:
                result.append(plans[0][2])
                now = plans[0][0] + plans[0][1]
                plans.pop(0)
            elif plans[0][0] + plans[0][1] > plans[1][0]:
                wait.append([plans[0][0] + plans[0][1] - plans[1][0], plans[0][2]])
                now = plans[1][0]
                plans.pop(0)
        elif len(plans) == 1:
            result.append(plans[0][2])
            now = plans[0][1]
            plans.pop(0)
        while wait:
            if plans:
                if now + wait[-1][0] <= plans[0][0]:
                    result.append(wait[-1][1])
                    now += wait[-1][0]
                    wait.pop()
                elif now + wait[-1][0] > plans[0][0]:
                    wait[-1][0] = now + wait[-1][0] - plans[0][0]
                    now = plans[0][0]
                    break
            else:
                result.append(wait[-1][1])
                wait.pop()
        if plans == [] and wait == []:
            break
    return result

# now라는 변수를 통해서 잉여시간동안 다른 과목을 진행하는데 있어서 잘못 대입한것 같음..
# def solution(plans):
#     result, wait = [], []
#     for i in range(len(plans)):
#         name, start, use = plans[i]
#         ti, mi = start.split(":")
#         start  = int(ti) * 60 + int(mi)
#         plans[i] = [start, int(use), name]
#     plans.sort(key = lambda x:x[0])
#     now = plans[0][0]
#     while True:
#         if len(plans) > 1:
#             if now + plans[0][1] <= plans[1][0]:
#                 now += plans[0][1]
#                 result.append(plans[0][2])
#             else:
#                 now = plans[1][0]
#                 wait.append([plans[0][0] + plans[0][1] - plans[1][0], plans[0][2]])
#             plans.pop(0)
#         elif len(plans) == 1 and now == plans[0][0]:
#             result.append(plans[0][2])
#             break
#         if wait and now < plans[0][0]:
#             while True:
#                 if now + wait[-1][0] <= plans[0][0]:
#                     now += wait[-1][0]
#                     wait.pop()
#                 elif now + wait[-1][0] > plans[0][0]:
#                     wait[-1][0] = wait[-1][0] - (plans[0][0] - now)
#                     now = plans[0][0]
#                 if now == plans[0][0]:
#                     break
#         if plans == [] and wait == []:
#             break
#     if wait:
#         for i in range(1, len(wait)+1):
#             result.append(wait[-i][1])
#     return result
