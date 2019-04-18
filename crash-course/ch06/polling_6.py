favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

persons = ['siva', 'phil', 'venkat', 'edward']

for person in persons:
  participated_persons = list(favorite_languages.keys())
  if person in participated_persons:
    print(f'Hi {person.title()}, Thank you for reponding')
  else:
    print(f'Hi {person.title()}, Please take my favorite language poll')