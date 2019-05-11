import p3 as p

def palindrome(n):
  return str(n) == str(n)[::-1]

if __name__ == "__main__":
  first = True
  for i in range(999*999, 99*99, -1):
    if not first:
      break
    if palindrome(i):
      f = p.factors(i)
      for (j,k) in f:
        if j < 100 or j > 1000:
          pass
        elif k < 100 or k > 1000:
          pass
        elif first:
          first = False
          print("%d %d %d" % (i,j,k))
