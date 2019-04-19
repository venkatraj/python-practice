def is_unique(my_list):
  for number1 in my_list:
    found_count = 0
    for number2 in my_list:
      if number1 == number2:
        found_count += 1
    if found_count > 1:
      return 'Not unqiue'
  return 'Unique'  


numbers = [1,2,3,4,4,5,6,7,8,9]
result = is_unique(numbers)
print(result)

