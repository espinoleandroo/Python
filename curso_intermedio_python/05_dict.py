import random

dict = {}

for i in range (1,5):
    dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range (1,5)}
print(dict_v2)


countries = ["mex","col","arg"]
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

names = ["leandro", "itzel"]
ages = [26, 26]

print(list(zip(names,ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)