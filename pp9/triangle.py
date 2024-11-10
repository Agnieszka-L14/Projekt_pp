#pobieramy od użytkownika długości trzech odcinków
#sprawdzamy czy można z nich zbudowac trójkąt
#sprawdzamy jaki to będzie trójkąt , ze wzgledu na boki(różnoboczny, równoboczny,równoramienny)
#sprawdź jaki to bedzie trójkat ze wzgledu na kąty (prostokątny, ostrokątny, rozwartokątny)

print("podaj długości trzech odcinków (liczby całkowite)")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a+b >c and a+c> b and b+c> a:
    print("Z tych odcinków można zbudować trójkąt ", end=" ")
    if a ==b ==c:
        print("To trójkat równoboczny. ", end=" ")
    elif a==b or a==c or b==c:
        print(" To trójkat równoramienny. ")
    else:
        print("To  trójkąt różnoboczny. ")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
        print("To trójkąt prostokątny. ")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2 :
        print("To trójkąt rozwartokatny. ")
    else:
        print("To trójkąt ostrokatny .")
else:
    print("Z tych odcników nie powstanie trójkąt")

