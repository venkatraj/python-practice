import random

def my_shuffle(data):
  result = []
  while True:
    random_number = random.randint(min(data), max(data))
    if random_number not in result:
        result.append(random_number)        
    if len(result) == len(data):  
      return result

new_list = my_shuffle(list(range(1,11)))
print(new_list)