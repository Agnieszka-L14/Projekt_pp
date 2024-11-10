#czy pierwiastek kwadratowy z liczby całkowitej jest liczbą całkowią
number = int(input ("Podaj liczbę całkowitą: "))
a = number ** (0.5)

if a % 1 == 0:
    str1= "Tak"
    str2 = ""

else:
    str1 = "Nie"
    str2 = "nie"
print(str1 + ",  pierwiastek kwadratowy z liczby " + str(number) +" "+ str2 + " liczbą całkowitą . ")