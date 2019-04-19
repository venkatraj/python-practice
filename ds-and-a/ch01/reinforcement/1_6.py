def sum(number):
  total = 0
  for i in range(number):
    if i % 2 != 0:
      total += i * i
  return total

print(sum(10))