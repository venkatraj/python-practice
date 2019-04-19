def minmax(data):
  min = data[0]
  max = data[0]
  for number in data:
    if number < min:
      min = number
    if number > max:
      max = number
  
  return min, max

min, max = minmax([1, 2, 3, 4, 5, 4, 3, 8, -2])
print('Min: ', min, 'Max: ', max)