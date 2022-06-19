def dexpand(n,d):
    seq = []
    m = {}
    i = 0
    while n != 0:
        while n < d:
            n *= 10
        r = n % d
        if r in m:
            return seq[m[r]::]
        else:
            seq.append(n//d)
        n = r
        m[n] = i
        i = i + 1
    return []

def solve():
    ans = 0
    m = 0
    for d in range(1, 1000):
        l = len(dexpand(1,d))
        if l > m:
            m = l
            ans = d
    return ans

if __name__ == '__main__':
    ans = solve()
    print(ans)
