siva = {
  'first_name': 'Sivakumar',
  'last_name': 'Muthiyalu',
  'age': 29,
  'city': 'Chennai'
}

for k,v in siva.items():
  k = k.replace('_', ' ').title()
  print(f'{k} is {v}')