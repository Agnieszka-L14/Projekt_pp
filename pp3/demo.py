#liczby całkowite

print(1_000_000)
print(1000000)
print(1_0_0_0_0_0)
print(-2)
print(2)
print(type(2))

#systemy liczbowe
#zapis 123 w systemie dziesiętnym =1*100+2*10+3*1, =1*10**2+2*10**1+3*1**0


print(0b101) #system dwójkowy
print(0o14) #system ósemkowy
print(0xFF) #system szesnastkowy

print(0o12+0xA)

print(type(0o127))

#liczby zmiennoprzecikowe

print(2.0)
print(.123)
print(3.)

#notacja wykładnicza
print(5e3) #5*10**3=5000
print(1e17)
print(2.45e-5)
print(2.45e-4)

print(123_000_000)
print ("{:.2e}".format(123_000_000))

print(2.3e-5)
print("{:.6f}".format(2.3e-5))

#ciągi znaków
print("Ala ma kota, a kot ma Alę")
print('Ala ma kota, a kot ma Alę')
print("tekst ze znakiem\n nowej linii")
print("I'm Monty Python")
print("I\'m Monty Python")
print("><", ">/\t<", ">\t\t\t<" , sep="\n")

#wartości logiczne
print(False)
print (2>3)
print(type(2>3))
print (2<9)

print(bool(1))
print(bool(0)) #zero jest false zawsze