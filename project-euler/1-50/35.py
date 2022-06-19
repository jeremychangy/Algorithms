def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def rot(n):
    s = set()
    ss = str(n)
    for i in range(len(ss)):
        s.add(int(ss[i:] + ss[:i]))
    return list(s)

def solve():
    ans = 0
    P = set(primes(1000000))
    for p in P:
        R = rot(p)
        check = True
        for r in R:
            if r not in P:
                check = False
        if check:
            ans += 1
    return ans

if __name__ == '__main__':
    ans = solve()
    print(ans)
