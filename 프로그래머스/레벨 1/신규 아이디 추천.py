#거의 1년 동안 푼듯?
def solution(new_id):
    new_id = new_id.lower()
    new_list = list(new_id)
    for i in range(len(new_list)):
        if new_list[i] not in ['-', '_', '.'] and new_list[i].isdigit() == False and new_list[i].isalpha() == False:
            new_list[i] = ''
    new_id = ''.join(new_list)

    for i in range(len(new_list)):
        a = new_id.replace('..', '.')
        if a == new_id:
            break
        else:
            new_id = a
    new_list = list(new_id)
    if len(new_list)>=1 and new_list[0] == '.':
        del new_list[0]
    if len(new_list)>=1 and new_list[-1] == '.':
        new_list.pop()
    if new_list == []:
        new_list.append('a')
    if len(new_list) >= 16:
        new_list = new_list[:15]
    if new_list[-1] == '.':
        new_list.pop()
    for i in range(3):
        if len(new_list) <= 2:
            new_list.append(new_list[-1])
        else: break
    result = ''.join(new_list)
    return result
