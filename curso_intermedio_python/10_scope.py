price = 100

def increment():
    price = 200
    price = price + 10
    print(price)
    return price

print(price)
price = increment()
print(price)