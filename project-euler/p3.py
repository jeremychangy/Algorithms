def factors(n):
  f = []
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      f.append((i, n/i))
      #f.append(n/i)
  return f

def isPrime(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False
  else:
    for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
        return False
  return True

if __name__ == "__main__":
  n = 600851475143
  ans = 0
  f = factors(n)
  for i in f:
    if isPrime(i) and ans < i:
     ans = i
  print ans
