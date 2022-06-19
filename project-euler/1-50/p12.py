import p3 as p
#(i,j)->(842161320,41041), 511 factors incorrect

if __name__ == "__main__":
  i = 1
  j = 2

  while len(p.factors(i)) < 500:
    i = i + j
    j = j + 1

  print i,j
  print len(p.factors(i))
