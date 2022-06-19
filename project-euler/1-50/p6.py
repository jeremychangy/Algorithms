if __name__ == "__main__":
  sum_squares = sum(i ** 2 for i in range(1,101))
  square_sums = sum(range(1,101)) ** 2 
  print square_sums - sum_squares
