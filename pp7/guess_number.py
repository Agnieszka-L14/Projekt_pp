import random

number =random.randint(1,3)
guess = int(input("Zgadnij jaką liczbe mam na myśli (1,2 lub 3) :"))

if guess ==number:
    print("Brawo , dokładnie taką liczbe miałem na myśli ")
else:
    print("Niestety myślałem o liczbie " + str(number) + " . ")