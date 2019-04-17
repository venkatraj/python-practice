friends = ['Saravanan', 'Jeevamani', 'Manohar Raja', 'Ravishankar']
for friend in friends:
  print(f'Hi {friend}, I would like to invite you to dinner')

print(f'I heard, {friends[-1]} could not make it to dinner!')
friends[-1] = 'Ramlal'
for friend in friends:
  print(f'Hi {friend}, I would like to invite you to dinner')

print('Wow! I have found a big dinner table!!')
friends.insert(0, 'Sivakumar M')
friends.insert(3, 'VJ Sivakumar')
friends.append('Govindarajan')
for friend in friends:
  print(f'Hi {friend}, I would like to invite you to dinner')
