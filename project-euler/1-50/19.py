from datetime import date, timedelta

def cheap():
    ans = 0
    start = date(1901, 1, 1)
    end = date(2000, 12, 31)
    for d in range(int((end - start).days)):
        if (start + timedelta(d)).weekday() == 6 and (start + timedelta(d)).day == 1:
            ans += 1
    return ans

def fine():
    c = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = 0
    ans = 0

    for i in range(1901, 2001):
        for j in range(len(c)):
            d = c[j]
            if c[j] == 28:
                if (i % 100 == 0 and i % 400) or (i % 4 == 0):
                    d += 1
            for k in range(d):
                if a == 6 and k == 0:
                    ans += 1
                a = (a + 1) % 7

    # dont count 1/1/2001
    return ans - 1

if __name__ == '__main__':
    print(cheap())
    print(fine())
