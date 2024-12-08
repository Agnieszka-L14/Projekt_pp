phones = {"Tomek": 66657463, "Ada": 87846352, "Karol": 76574364, "Tomek": 84676736627}
print(phones)

animals_dict = {
    "kot": "cat",
    "pies":"dog",
    "chomik": "hamster"
}
print(animals_dict["kot"]) # jak nie ma takiego klucza to error
print(animals_dict.get("kot", "Brak takiego klucza w słowniku"))#jak nie ma tekiego klucza , wartość none
print(animals_dict.get("wiewiórka", "Brak takiego klucza w słowniku"))

words=["kot","lew","chomik"]

for word in words:
    if word in animals_dict.keys():
        print(word,"->",animals_dict[word])
    else:
        print("Nie znaleziono jakiego słowa {} w słowniku".format(word))

for key in animals_dict.keys():
    print(key,"->",animals_dict[key])

print()

for value in animals_dict.values():
    print(value)

print()

for item in animals_dict.items():
    print(item)

for pl, en in animals_dict.items():
    print(pl, "->" ,en)

animals_dict["świnka"]= "pig" #dodanie elementu
print(animals_dict)

animals_dict.popitem() #usunięcie
print(animals_dict)
animals_dict.clear() #wyczyszczenie całego słownika
print(animals_dict)