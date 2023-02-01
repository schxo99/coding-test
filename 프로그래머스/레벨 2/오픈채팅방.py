#기존 아이디를 닉네임으로 replace로 변환하려 했으나 효율성이 안좋아보임
# def solution(record):
#     arr = []
#     name = {}
#     for i in range(len(record)):
#         user = record[i].split()
#         if user[0] == 'Enter' or user[0] == 'Change':
#             name[user[1]] = user[2]
#             if user[0] == 'Enter':
#                 arr.append(user[1]+'님이 들어왔습니다.')
#         elif user[0] == 'Leave': 
#             arr.append(user[1]+'님이 나갔습니다.')


def solution(record):
    arr = []
    name = {}
    for i in range(len(record)):
        user = record[i].split()
        if user[0] == "Enter" or user[0] == "Change":
            name[user[1]] = user[2]
    for k in range(len(record)):
        user = record[k].split()
        if user[0] == "Enter":
            arr.append(name[user[1]]+"님이 들어왔습니다.")
        elif user[0] == "Leave":
            arr.append(name[user[1]]+"님이 나갔습니다.")
    return arr      
