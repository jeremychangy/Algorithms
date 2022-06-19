def calc(n):
    s = 0
    for c in str(n):
        s += int(c) ** 5
    return s == n

def solve():
    s = 0
    for i in range(10, 5 * 9**5):
        if calc(i):
            print(i)
            s += i
    return s

if __name__ == '__main__':
    ans = solve()
    print(ans)
