def evens():
  a = 1
  b = 1
  ans = 0

  while a < 4000000:
    if a % 2 == 0:
      ans += a
    a,b = b,a + b

  return ans

if __name__ == "__main__":
  print(evens())
