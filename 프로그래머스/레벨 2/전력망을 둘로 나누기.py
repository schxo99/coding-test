from collections import deque
def solution(n, wires):
    result = n
    for i in range(len(wires)):
        test = deque(wires[::])
        ch_left, ch_right = set(), set()
        ch_left.add(test[i][0])
        ch_right.add(test[i][1])
        while test:
            if test[0][0] in ch_left and test[0][1] in ch_right:
                pass
            elif test[0][0] in ch_left or test[0][1] in ch_left:
                ch_left.add(test[0][0])
                ch_left.add(test[0][1])
            elif test[0][0] in ch_right or test[0][1] in ch_right:
                ch_right.add(test[0][0])
                ch_right.add(test[0][1])
            else:
                test.append(test[0])
            test.popleft()
        result = min(result, abs(len(ch_left) - len(ch_right)))
    return result
