users = ['admin','Arjun','Balaji','Chandran','Dinesh']
new_users = ['Elango', 'Balaji', 'Fernandez', 'admin', 'Ganesh']
current_users = []

for user in users:
  current_users.append(user.lower())

for user in new_users:
  if user.lower() in current_users:
    print(f'Username {user} already take, Please enter new one')
  else:
    print(f'Username {user} is available')