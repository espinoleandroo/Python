items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalon',
        'price': 300
    },
    {
        'product': 'pantalon 2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)