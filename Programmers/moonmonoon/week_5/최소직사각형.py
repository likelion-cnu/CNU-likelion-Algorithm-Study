def solution(sizes):
    answer = 0
    for s in sizes:
        if s[0] < s[1]:
            temp = s[0]
            s[0] = s[1]
            s[1] = temp

    a = [a[0] for a in sizes]
    b = [b[1] for b in sizes]

    answer = max(a) * max(b)
    return answer
