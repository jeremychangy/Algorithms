def ispandigital(n):
    v = [False, False, False, False, False, False, False, False, False]
    for c in str(n):
        i = int(c)-1
        if i >= 0 and i < 9:
            v[i] = True
    check = True
    for i in v:
        check &= i
    return check

def solve():
    n = 1
    ans = []
    while n < 100000:
        l = []
        for i in range(1,10):
            l.append(str(n*i))
            c = int(''.join(l))
            if c > 1000000000:
                continue
            if ispandigital(c):
                ans.append(c)
        n += 1
    return max(ans)

if __name__ == '__main__':
    ans = solve()
    print(ans)
