usernames = ['admin','Arjun','Balaji','Chandran','Dinesh']

if usernames:
  for username in usernames:
    if username is 'admin':
      print('Hello admin, would you like to see a status report?')
    else:
      print(f'Hello {username}, thank you for logging in again')
else:
  print('There are no users')