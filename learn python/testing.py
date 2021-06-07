def multiple(m, n):
   a = range(n, (m * n) + 1, n)
   print(*a)

m = 3
n = 5
multiple(m, n)
