with open('./curso_intermedio_python/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write("Lorem0\n")
    file.write("Lorem1\n")
    file.write("Lorem2\n")

