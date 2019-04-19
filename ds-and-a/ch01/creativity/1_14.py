def is_product_odd(my_list):
  last_item = len(my_list)
  for item in range(last_item):
    if item < last_item - 1:
      result = my_list[item] * my_list[item+1]
      if result % 2 != 0:
        return my_list[item], my_list[item+1]


result = is_product_odd([1,2,3,4,5,6,7,8,9])
if result is not None:
  print("This sequence is odd: ", result)
else:
  print('There is not odd sequence')