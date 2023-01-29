set_countries = {"mex", "col", "arg"}
print(set_countries)

size = len(set_countries)
print(size)

print("mex" in set_countries)
print("bra" in set_countries)
print("bra" in set_countries)

set_countries.add("bra")
print("bra" in set_countries)
print(set_countries)

set_countries.update({"ecu", "per"})
print(set_countries)

set_countries.remove("bra")
set_countries.discard("bra")
print(set_countries)

set_countries.clear()
print(set_countries)
size = len(set_countries)
print(size)