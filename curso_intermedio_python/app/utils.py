def get_population():
    keys = ['Mex', "Col"]
    values = [400, 300]
    return keys, values

def population_by_contry(data, contry):
    result = list(filter(lambda item: item["Country"] == contry, data))
    return result
