import math

N = 10000
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def is_square(n):
    return n == int(math.isqrt(n) * math.isqrt(n))

def check(n):
    P = primes(N)
    if n in set(P):
        return True
    check = False
    for p in P:
        if p > n:
            return False
        else:
            if (n-p) % 2 == 0 and is_square((n-p)//2):
                return True
    return check

def solve():
    n = 9
    while check(n):
        n += 2
    return n

if __name__ == '__main__':
    ans = solve()
    print(ans)
