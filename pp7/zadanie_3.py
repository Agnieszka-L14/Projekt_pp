import random

number =random.randint(1,10)

msg ="Zgadnij jaką liczbe mam na myśli (od 1 do 10) :"
guess = int(input(msg))

if guess ==number:
    print("Brawo , dokładnie taką liczbe miałem na myśli! ")
else:
    msg ="Masz kolejna szansę, moja liczba jest "
    if number % 2 ==0:
        msg += "parzysta : "
    else:
        msg += "nieparzysta : "
    guess = int(input(msg))
    if guess ==number:
        print(" Brawo, udało sie odgadnąc juz za drugim razem")
    else:
        msg = "Masz ostatnia szansę , moja liczba jest : "
        if number > 5 :
            msg += "wieksza niż "
        else:
            msg += "mniejsza lub równa : "
        msg += "pięć : "
        guess = int(input(msg))
        if guess == number:
            print(" Brawo, udało sie odgadnąc juz za trzecim razem")
        else:
            print("Niestety , myślałem o liczbie " + str(number) +" .")




