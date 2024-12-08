while True:
    try:
        number = int(input("podaj liczbę całkowitą: "))
        print("Odwrotna liczba to ", 1 / number)
    except ValueError:
        print("To nie jest liczba całkowita ")
    except ZeroDivisionError:
        print("Bład dzielenia przez zero")
    except:
        print("Cos poszło nie tak ")
