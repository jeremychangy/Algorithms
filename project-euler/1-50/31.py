c = [1, 2, 5, 10, 20, 50, 100, 200]

def solve(e, n):
    if e == 0:
        return 1
    if e < 0:
        return 0
    if e >= 1 and n <= 0:
        return 0
    return solve(e, n-1) + solve(e - c[n-1], n)

if __name__ == '__main__':
    ans = solve(200, len(c))
    print(ans)
