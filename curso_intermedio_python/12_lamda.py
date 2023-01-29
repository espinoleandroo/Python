def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

full_name = lambda name, last_name : f'Full name es {name.title()} {last_name.title()}'

text = full_name('leandro', 'espino')
print(text)