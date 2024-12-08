numbers=[]
counter =1
while True:
    if counter>5:
        break
    try:
        number = int(input("podaj liczbę całkowitą : "))
        numbers.append(number)
        counter+=1
    except:
        print("To nie jest liczba całkowita , spróbuj ponownie ")

print(numbers)
