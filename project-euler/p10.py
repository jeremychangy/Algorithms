import p3 as p
if __name__ == "__main__":
  ans = 0
  for i in range(1,2000000):
    if p.isPrime(i):
      ans = ans + i
  print ans
