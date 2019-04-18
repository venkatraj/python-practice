def is_multiple(n, m):
  for i in range(n):
    if m*i == n:
      return True
  return False

result = is_multiple(10, 3)
print(result)