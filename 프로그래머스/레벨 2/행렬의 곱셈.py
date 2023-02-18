def solution(arr1, arr2):
    result, lv, hap = [], [], 0
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr2)):
                hap += arr1[i][j] * arr2[j][k]
            lv.append(hap)
            hap = 0
        result.append(lv)
        lv = []
    return result
