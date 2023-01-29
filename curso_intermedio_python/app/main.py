import utils
import read_csv
import charts

data = read_csv.read_csv("./data/working_with_files/world_population.csv")

def get_history_population_by_country():
    contry = input('Type Country: ')

    result = utils.population_by_country(data, contry)

    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)

def get_world_population_percentage():
    continent = input('Type Continent: ')
    result = utils.countries_continent(data, continent)

    dict = utils.world_population_percentage(result)
    keys = list(dict.keys())
    values = list(dict.values())
    charts.generate_pie_chart(keys, values)


def run():
    #get_history_population_by_country()
    get_world_population_percentage()


if __name__ == '__main__':
    run()