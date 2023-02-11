def solution(numer1, denom1, numer2, denom2):
    s = (numer1 * denom2) + (numer2 * denom1)
    m = denom1 * denom2
    a = 2
    while True:
        if s % a == 0 and m % a == 0:
            s = s/a
            m = m/a
        else:
            a+=1
        if a > s or a > m:
            break
    return [s,m]
