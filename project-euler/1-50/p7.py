import p3 as p

if __name__ == "__main__":
  i = 0
  j = 1
  while i != 10001:
    if p.isPrime(j):
      i = i + 1
    j = j + 1
  print j - 1
