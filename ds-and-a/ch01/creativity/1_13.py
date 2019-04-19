def reverse_order(my_list):
  reverse_list = []
  for item in my_list:
    reverse_list.insert(0, item)
  return reverse_list

original = [1,2,3,4,5]
print(reverse_order(original))
original.reverse()
print(original)