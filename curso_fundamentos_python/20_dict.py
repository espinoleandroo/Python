person = {
    'name': 'leandro',
    'last_name': 'Espino',
    'langs': ['java', 'python'],
    'age' : 26
}

print(person)

person['name'] = 'Leandro'
person['age'] -= 1
person['langs'].append('c++')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())
print('keys')
print(person.keys())
print('values')
print(person.values())
