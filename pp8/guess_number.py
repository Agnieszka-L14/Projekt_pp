# gra toczy się dopóki nie zostanie odgadnięta liczba

import random
counter =1
number =random.randint(1,10)

guess= int(input("Zgadnij jaka liczbe mam na myśli (0-10)"))

while guess !=number:
    guess = int(input("Nie to nie ta. Spróbuj jeszcze raz "))
    counter +=1
print("Brawo , udało Ci sie za " + str(counter)+ " razem ")