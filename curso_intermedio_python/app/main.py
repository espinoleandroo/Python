import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Mexico',
        'Population':500
    },
    {
        'Country': 'Colombia',
        'Population':400
    }
]

contry = input('Type Country: ')

result = utils.population_by_contry(data, contry)
print(result)