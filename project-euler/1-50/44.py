import math

N=10000

def P(n):
    return n*(3*n-1)//2

def pentagon(n):
    ans = []
    for i in range(1,n+1):
        ans.append(P(n))
    return ans

def P_inv(n):
    m = 1 + 24 * n
    s = math.isqrt(m)
    if s ** 2 == m:
        if (s + 1) % 6 == 0:
            return (s+1) // 6
    return -1

def solve():
    ans = 0
    for i in range(1,N):
        for j in range(i+1,N):
            a = abs(P(i)-P(j))
            b = P(i)+P(j)
            if P_inv(a) != -1 and P_inv(b) != -1:
                ans = a
    return ans


if __name__ == '__main__':
    ans = solve()
    print(ans)
