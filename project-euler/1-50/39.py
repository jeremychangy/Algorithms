def pythagorean(N):
    ans = []
    for x in range(N):
        y = x+1
        z = y+1
        while z <= N:
            while z * z < x * x + y * y:
                z = z + 1
            if z * z == x * x + y * y and z <= N:
                ans.append((x,y,z))
            y = y + 1
    return ans

def solve():
    m = {}
    p = pythagorean(500)
    for x,y,z in p:
        s = sum([x,y,z])
        if s not in m:
            m[s] = []
        m[s].append((x,y,z))
    ans = 0
    l = 0
    for k,v in m.items():
        if len(v) > l and k <= 1000:
            l = len(v)
            ans = k
    return ans

if __name__ == '__main__':
    ans = solve()
    print(ans)
