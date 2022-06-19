def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def factorize(n,P):
    f = set()
    for p in P:
        while n % p == 0:
            n = n // p
            f.add(p)
    return f

def solve():
    P = primes(10000)
    for i in range(1, 50000000):
        if i in set(P):
            continue
        if len(factorize(i,P)) == len(factorize(i+1,P)) == len(factorize(i+2,P)) == len(factorize(i+3,P)) == 4:
            print(i, factorize(i,P))
            print(i+1, factorize(i+1,P))
            print(i+2, factorize(i+2,P))
            print(i+3, factorize(i+3,P))
            return i

if __name__ == '__main__':
    # ans = 47761635
    print(solve())
