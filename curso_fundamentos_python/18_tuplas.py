numeros = (1, 2, 3, 5)
strings = ("nico", "zule", "santi")

print(numeros)
print(type(numeros))


print("0 => ", numeros[0])
print("-1 => ", numeros[-1])


print(strings)
print(strings.index("zule"))
print(strings.count("nico"))

print(type(strings))
my_list = list(strings)
print(type(my_list))

my_tuple = tuple(my_list)
print(type(my_tuple))
