toppings = []

while True:
  topping = input('Enter your topping choice (q to quit)')
  if topping == 'q':
    break
  print('We are adding your topping to pizza')
  toppings.append(topping)

print(toppings)
