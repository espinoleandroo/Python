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

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print('new list')
print(new_items)
print('old list')
print(items)
