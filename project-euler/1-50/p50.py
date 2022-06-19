import p3 as p

if __name__ == "__main__":
  n = 1000000
  primes = [2,3,5,7,11,13]
  i = 14
  while i < n:
    if p.isPrime(i):
      primes.append(i)
    i = i + 1

  i = 0
  for j in range(3,len(primes)):
    i = i + primes[j]

  print i
