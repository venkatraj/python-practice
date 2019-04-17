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

print("Sorry friends, Now I can invite only two people")
while True:
  friend = friends.pop()
  print(f'Sorry, {friend} I could not invite you to dinner this time')
  if (len(friends) == 2):
    break

for friend in friends:
  print(f'Hi {friend}, you are still invited to dinner')

while True:
  del friends[0]
  if (len(friends) == 0):
    break
    
print(friends)