N=1001
def create_array(n):
    return [[0 for x in range(n)] for y in range(n)]

def spiral(n):
    a = create_array(n)
    curr = [n//2, n//2]
    a[curr[0]][curr[1]] = 1
    b = 2

    for i in range(1, n):
        # right
        if (i-1) % 2 == 0:
            for j in range(i):
                curr[1] += 1
                a[curr[0]][curr[1]] = b
                b += 1

        # down
        if (i-1) % 2 == 0:
            for j in range(i):
                curr[0] += 1
                a[curr[0]][curr[1]] = b
                b += 1

        # left
        if (i-1) % 2 == 1:
            for j in range(i):
                curr[1] -= 1
                a[curr[0]][curr[1]] = b
                b += 1

        # up
        if (i-1) % 2 == 1:
            for j in range(i):
                curr[0] -= 1
                a[curr[0]][curr[1]] = b
                b += 1
    for i in range(1, n):
        a[0][i] = b
        b += 1

    return a

def ans(a, n):
    ans = 0
    for i in range(n):
        ans += a[i][i]
    for i in range(n):
        ans += a[len(a)-i-1][i]
    return ans-1

if __name__ == '__main__':
    a = spiral(N)

    #print(*a, sep='\n')
    print(ans(a, N))
