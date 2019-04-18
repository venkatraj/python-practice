while True:
  age = input('Enter your age (q to quit) ')
  if age == 'q' or not age.isdigit():
    break
  age = int(age)
  if age < 3:
    print('The ticket is free')
  elif age >=3 and age <=12:
    print('The ticket costs $10')
  elif age > 12:
    print('The ticket costs $15')
