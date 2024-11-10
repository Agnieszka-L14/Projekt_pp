#. Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

a=int(input("Podaj poczatkowa wartość zbioru cyfr : "))
b=int(input("Podaj końcową wartość zbioru cyfr : "))
is_first =True
print("liczby z zakresu od : ", a , " do ", b , " podzielne przez 3, 5 lub 7 to : " , end=" ")
for i in range(a,b+1):
    if (i %3 ==0 or i % 5==0 or i % 7 ==0):
        if not is_first:
            print(",", end=" ")
        print(i, end=" ")
        is_first=False
print(".")
