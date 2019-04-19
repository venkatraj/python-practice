def original_scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor


my_list = [1,2,3]
original_scale(my_list, 5)
print(my_list)

def alternate_scale(data, factor):
  for val in data:
    val *= factor

alternate_scale(my_list, 5)
print(my_list)

# Won't work because val is not reference to the value in data list
