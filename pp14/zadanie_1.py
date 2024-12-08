# Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informację o jego braku.

phones = {"Tomek": 66657463,
          "Ada": 87846352,
          "Karol": 76574364,
          "Marek": 846767366,
          "Agata": 457452415
          }


def show_number():
    name = input("podaj imię : ")
    for i in phones:
        if name in phones.keys():
            print(name, "->", phones[name])
            break
        else:
            print("Nie znaleziono jakiego imienia {} w słowniku".format(name))
            break


print(show_number())

while True:
    name =input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("telefon:", phones[name])
    else:
        print("Nie znaleziono")
