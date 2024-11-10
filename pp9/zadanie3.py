#Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
#całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.

number =int(input(" podaj dowolna lioczbe całkowitą : "))
n = int(input("podaj numer bitu : "))
mask = 1 << n
result = number & mask
bit = int(bool(result))
print("Bit na pozycji ", n , " dla liczby " , number , " wynosi ",  str(bit)) , " ."
# sprawdzenie jak wygląda liczba
print("{:08b}".format(number))
print("{:08b}".format(mask))
print("-" * 8)
print("{:08b}".format(result))