def sum(number):
  total = 0
  for i in range(number):
    total += i * i
  return total

print(sum(5))