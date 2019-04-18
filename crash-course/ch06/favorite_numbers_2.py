favorite_numbers = {}

try:
  while True:
    name = input('Enter your name (q to quit)')
    if name == 'q':
      break
    favorite_number = input('Enter your favorite number (q to quit)')
    if favorite_number == 'q':
      break
    if favorite_number.isdigit():
      favorite_numbers[name] = favorite_number
except:
  pass      

for k,v in favorite_numbers.items():
  print(f'{k}\'s favorite number is {v}')
