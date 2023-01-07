'''
while True:
    print(":)")
'''

counter = 0
while counter < 10:
    counter += 1
    print(counter)

print("--- " * 10)

counter = 0
while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)

print("--- " * 10)

counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)