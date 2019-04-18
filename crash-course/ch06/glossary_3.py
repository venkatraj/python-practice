glossary = {
  'lists': 'A python list is a collection of data and is mutable',
  'string': 'A python string is a sequence of alphabets and is immutable',
  'tuple': 'A python tuple is a collection of data and is immutable',
  'dictionary': 'A python dictionary is a key value pair data set'
}

for k,v in glossary.items():
  print(f'{k.title()}: {v}')