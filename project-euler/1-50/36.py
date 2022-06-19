def ispalindrome(n):
    return str(n) == str(n)[::-1]

def base2(n):
    b = 0
    i = 1
    while n > 0:
        if n % 2 != 0:
            b += 1 * i
        i = i * 10
        n = n // 2
    return b

def solve():
    l = []
    for i in range(1000000):
        if ispalindrome(i) and ispalindrome(base2(i)):
            l.append(i)
    return sum(l)

if __name__ == '__main__':
    ans = solve()
    print(ans)
