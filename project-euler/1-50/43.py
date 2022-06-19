a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def pandigitals(n, p, v):
    if len(n) == 10:
        p.append(n)
    for i in range(10):
        if not v[i]:
            v[i] = True
            pandigitals(n + str(a[i]), p, v)
            v[i] = False
    return

def solve(p):
    primes = [2, 3, 5, 7, 11, 13, 17]
    ans = []
    for pp in p:
        v = [False, False, False, False, False, False, False]
        for i in range(len(primes)):
            if int(pp[i+1:i+4]) % primes[i] == 0:
                v[i] = True
        check = True
        for i in range(len(v)):
            check &= v[i]
        if check:
            ans.append(pp)
    return ans

if __name__ == '__main__':
    p = []
    v = [False, False, False, False, False, False, False, False, False, False]
    pandigitals('', p, v)
    ans = solve(p)
    s = 0
    for i in ans:
        s += int(i)
    print(s)
