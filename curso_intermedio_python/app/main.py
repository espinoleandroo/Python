import utils

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

def run():
    keys, values = utils.get_population()
    print(keys, values)

    contry = input('Type Country: ')

    result = utils.population_by_contry(data, contry)
    print(result)


if __name__ == '__main__':
    run()