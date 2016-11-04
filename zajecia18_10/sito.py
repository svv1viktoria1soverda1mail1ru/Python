def sito(n):
    L = [0] + n * [1]
    p = 2
    q = p * p
    while q <= n:
        if L[p] == 1:
            i = q
            while i <= n:
                L[i] = 0
                i = i + p
        p = p + 1
        q = p * p
    M = []
    for i in range(1, n+1):
        if L[i] == 1:
            M.append(i)
    return M

print sito(81)
