N = 1000000000

def ispandigital(n):
    v = []
    for i in range(len(str(n))):
        v.append(False)
    while n > 0:
        i = (n%10)-1
        if i >= 0 and i < len(v):
            v[i] = True
        n = n // 10
    check = True
    for i in v:
        check &= i
    return check

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def solve():
    P = primes(N)
    ans = []
    for p in P:
        if ispandigital(p):
            ans.append(p)
    return max(ans)

if __name__ == '__main__':
    ans = solve()
    print(ans)
