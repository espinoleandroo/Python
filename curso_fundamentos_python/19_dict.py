my_dict = {}
print(type(my_dict))

my_dict = {
    'name' : 'Leandro',
    'last_name': 'Espino',
    "age": 26
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['last_name'])
print(my_dict.get("age"))

print('name' in my_dict)
print("nombre" in my_dict)