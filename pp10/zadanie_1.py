#Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
#• skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
#• pobrać kolejne elementy i zapisać je do listy,
#• wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika
names=[]

number = int(input("Podaj liczbe imion , które chcesz wprowadzić : " ))
for i in range (number):
    name = input("Podaj imię użytkownika : ")
    names.append(name)
print("Podano nastepujace imiona : ",names)

#for i in range (number):
    #names.append(input("Podaj" +str(i+1) + " imię : "))
    #print("Podano nastepujace imiona : ",names)