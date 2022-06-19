import math
def T(n):
    return n * (n+1) / 2
def P(n):
    return n * (3*n-1) / 2
def H(n):
    return n * (2*n-1)

def solve():
    i = 1
    p = set()
    h = set()
    while True:
        if T(i) in p and T(i) in h and i != 285:
            return i
        p.add(P(i))
        h.add(H(i))
        i += 1

if __name__ == '__main__':
    ans = solve()
    print(ans)
    print(T(ans))
