if __name__ == "__main__":
  d = "0"
  for i in range(1,1000001):
    d = d + str(i)
  print int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
