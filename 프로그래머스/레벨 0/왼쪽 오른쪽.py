def solution(str_list):
    result = []
    if "l" not in str_list and "r" not in str_list:
        return []
    for i, k in enumerate(str_list):
        if k == "l":
            return str_list[:i]
        if k == "r":
            return str_list[i+1:]
