for element in range(1, 21):
    print(element)

print("--- " * 10)
my_list = [23,45,67,89]
for element in my_list:
    print(element)

print("--- " * 10)
my_tuple = ("23","45","67","89")
for element in my_tuple:
    print(element)

print("--- " * 10)
person = {
    'name': 'leandro',
    'last_name': 'Espino',
    'langs': ['java', 'python'],
    'age' : 26
}
for element in person:
    print("key => ", element)
    print("val => ", person[element])

for key, val in person.items():
    print(key, " => ", val)

print("--- " * 10)
people = [
    {
        'id': 1,
        'name': 'Leandro',
        'last_name': 'Espino',
        'age' : 26
    },
    {
        'id': 2,
        'name': 'Itzel',
        'last_name': 'Ruiz',
        'age' : 26
    },
]

for person in people:
    print(person['id'], " => ", person)
    for key, val in person.items():
        print(key, " => ", val)
