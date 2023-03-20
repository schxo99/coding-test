def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
            
    return n - len(_lost)
