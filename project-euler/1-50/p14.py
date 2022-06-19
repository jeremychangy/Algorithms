def collatz(n):
  count = 0
  while n != 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3*n + 1
    count = count + 1
  return count

if __name__ == "__main__":
  n = 2
  m = -1
  for i in range(2,1000000):
    if collatz(i) > m:
      n = i
      m = collatz(i)
  print n
