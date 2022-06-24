N = 1000000

def check(n):
    s = set()
    while n > 0:
        s.add(n%10)
        n = n // 10
    return s

def solve():
    ans = -1
    for i in range(1,N):
        if check(i) == check(2*i) == check(3*i) == check(4*i) == check(5*i) == check(6*i):
            return i
    return ans

if __name__ == '__main__':
    ans = solve()
    print(ans)
