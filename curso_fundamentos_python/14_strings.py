text = "Ella sabe programar en Python"
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print("Elejiste bien")
else:
    print("Tambien elejiste bien")

size = len(text)
print(size)

print(text)
print(text, text.upper())
print(text, text.lower())

print(text.count('a'))
print(text.swapcase())

print(text.startswith("Ella"))
print(text.endswith("Python"))

print(text.replace("Python", "Go"))


text2 = "este es un titulo"
print(text2.capitalize())
print(text2.title())

print(text2.isdigit())
print("11".isdigit())
