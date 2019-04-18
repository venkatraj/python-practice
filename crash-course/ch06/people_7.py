siva = {
  'first_name': 'Sivakumar',
  'last_name': 'Muthiyalu',
  'age': 29,
  'city': 'Chennai'
}

venkat = {
  'first_name': 'Venkatraj',
  'last_name': 'Nagarajan',
  'age': 45,
  'city': 'Salem'
}

saravanan = {
  'first_name': 'Saravanan',
  'last_name': 'VAP',
  'age': 45,
  'city': 'Salem'
}

people = {
  'siva': siva,
  'venkat': venkat,
  'saravanan': saravanan
}

for person,details in people.items():
  print(f'{person.title()} Details: ')
  for k,v in details.items():
    k = k.replace('_', ' ').title()
    print(f'{k} is {v}')
  print('')