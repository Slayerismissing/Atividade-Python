capitals = {
    "USA": "Washington D.C",
    "India":"New Delhi",
    "China":"Beijing",
    "Russia":"Moscow",
    "Brazil":"Brazilia"
    }

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does NOT exists")

# capitals.update({"Germany":"Berlim"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# values = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"\nCountry: {key} - capital: {value}")

