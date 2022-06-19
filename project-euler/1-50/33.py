from fractions import Fraction as f

def simplify(n,d):
    a = n%10
    b = d%10
    x = n//10
    y = d//10
    if a == b:
        return (x,y)
    if a == y:
        return (x,b)
    if x == b:
        return (a,y)
    if x == y:
        return (a,b)
    return (n,d)

def solve():
    l = []
    for j in range(10,100):
        for i in range(10,j):
            if i == j or (i%10 == 0 and j%10 == 0):
                continue
            x,y = simplify(i,j)
            if y == 0 or ((x == i) and (y == j)):
                continue
            if f(i,j) == f(x,y):
                l.append((i,j))
    return l

if __name__ == '__main__':
    ans = solve()
    print(ans)
