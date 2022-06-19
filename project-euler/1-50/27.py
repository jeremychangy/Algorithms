def f(n, a, b):
    return n * n + a * n + b

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def solve():
    m = 0
    am = 0
    bm = 0
    for b in range(-1000, 1001):
        for a in range(-999, 1000):
            n = 0
            while isprime(f(n, a, b)):
                n += 1
            if n > m:
                m = n
                am = a
                bm = b
    print(m, am, bm)
    return am * bm

if __name__ == '__main__':
    ans = solve()
    print(ans)
