file = open('./curso_intermedio_python/text.txt')
print(file.read())
file.close()
print("--------")

file = open('./curso_intermedio_python/text.txt')
print(file.readline())
print(file.readline())
file.close()
print("--------")


file = open('./curso_intermedio_python/text.txt')
for line in file:
    print(line)
file.close()
print("--------")


with open('./curso_intermedio_python/text.txt') as file:
    for line in file:
        print(line)

