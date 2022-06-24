def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def x(s,n,f):
    a = []
    for c in s:
        a.append(c)

    if type(n) == str:
        if f > 2:
            ans = []
            for i in range(2**f):
                k = 0
                for j in range(len(s)-1):
                    if s[j] == n:
                        if bin(i)[2:].zfill(f)[k] == '1':
                            a[j] = 'x'
                        k += 1
                #print(a, n, bin(i)[2:].zfill(f))
                ans.append(''.join(a))
                for i in range(len(s)-1):
                    a[i] = s[i]
            return ans
        else:
            for i in range(len(s)-1):
                if s[i] == n:
                    a[i] = 'x'
    else:
        a[n] = 'x'
    return [''.join(a)]

def calc(s):
    ans = []
    for i in range(len(s)-1):
        ans += x(s,i,0)
    m = {}
    for i in range(len(s)-1):
        if s[i] in m:
            m[s[i]] += 1
        else:
            m[s[i]] = 1
    for k,v in m.items():
        if v > 1:
            ans += x(s,k,v)
    return ans

def solve():
    P = primes(1001000)
    m = {}
    for i in range(len(P)):
        if len(str(P[i])) >= 2:
            P = P[i::]
            break

    for p in P:
        R = list(set(calc(list(str(p)))))
        for r in R:
            if str(r) in m:
                m[str(r)] += 1
            else:
                m[str(r)] = 1

    ans = []
    for k, v in m.items():
        if v >= 8:
            ans.append((k,v))

    return ans

if __name__ == '__main__':
    #print(calc(list('566663')))
    ans = solve()
    print(ans)
