import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv("./data/working_with_files/world_population.csv")
    contry = input('Type Country: ')

    result = utils.population_by_country(data, contry)

    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)

if __name__ == '__main__':
    run()