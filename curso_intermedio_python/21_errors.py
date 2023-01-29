#print(0/0)

suma = lambda x,y : x+y
assert suma(2,2) == 4

print("hola 2")

x = 10
if x < 18:
    raise Exception('menor de edad')