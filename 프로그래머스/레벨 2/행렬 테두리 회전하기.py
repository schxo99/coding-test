from collections import deque
def top_line(matrix, c_matrix, s1, s2, e1, e2, result):
    for i in range(s2, e2, 1):
        c_matrix.append(matrix[s1][i])
        matrix[s1][i] = 0
    matrix, c_matrix, result = right_line(matrix, c_matrix, s1, s2, e1, e2, result)
    return matrix, c_matrix, result

def right_line(matrix, c_matrix, s1, s2, e1, e2, result):
    for i in range(s1+1, e1, 1):
        c_matrix.append(matrix[i][e2-1])
        matrix[i][e2-1] = 0
    matrix, c_matrix, result = bottom_line(matrix, c_matrix, s1, s2, e1, e2, result)
    return matrix, c_matrix, result

def bottom_line(matrix, c_matrix, s1, s2, e1, e2, result):
    for i in range(e2-2, s2-1, -1):
        c_matrix.append(matrix[e1-1][i])
        matrix[e1-1][i] = 0
    matrix, c_matrix, result = left_line(matrix, c_matrix, s1, s2, e1, e2, result)
    return matrix, c_matrix, result

def left_line(matrix, c_matrix, s1, s2, e1, e2, result):
    for i in range(e1-2, s1, -1):
        c_matrix.append(matrix[i][s2])
        matrix[i][s2] = 0
    c_matrix, result = turn_matrix(c_matrix, result)
    return matrix, c_matrix, result

def turn_matrix(c_matrix, result):
    c_matrix.insert(0, c_matrix[-1])
    c_matrix.pop()
    result = findNum(c_matrix, result)
    return c_matrix, result

def findNum(c_matrix, result):
    result.append(min(c_matrix))
    return result

def return_matrix(matrix, c_matrix, s1, s2, e1, e2):
    index = 0
    c_matrix = deque(c_matrix) 
    for i in range(s2-1, e2, 1):
        num = c_matrix.popleft()
        matrix[s1-1][i] = num
    for i in range(s1, e1, 1):
        num = c_matrix.popleft()
        matrix[i][e2-1] = num
    for i in range(e2-2, s2-2, -1):
        num = c_matrix.popleft()
        matrix[e1-1][i] = num
    for i in range(e1-2, s1-1, -1):
        num = c_matrix.popleft()
        matrix[i][s2-1] = num
    return matrix
    
def solution(rows, columns, queries):
    result = []
    matrix = []
    num = 1
    for i in range(rows):
        row = []
        for k in range(columns):
            row.append(num)
            num+=1
        matrix.append(row)
    for s1, s2, e1, e2 in queries:
        c_matrix = []
        matrix, c_matrix, result = top_line(matrix, c_matrix, s1-1, s2-1, e1, e2, result)
        matrix = return_matrix(matrix, c_matrix, s1, s2, e1, e2)
    return result
