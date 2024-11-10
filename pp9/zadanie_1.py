#przechwycona wiadomość, którą należy rozszyfrować Xq|`gf(bm{|(nibfq)
#dla każdego znaku zmieniono 4 bit ma przeciwny, bity loczymy od najmniej znaczącego


print(ord("c"), chr(99))
print("{:08b}".format(ord("c")))

#01100011 - chcemy zmienić 4 bit
#maskowanie 00001000 - maska pozwalająca wyizolować wskazany bit/bity 1<<3
#chcemy zmienić na 00101011 -> uzywamy XORa (alternatywa rozłączna, do zmiany bitów

print("{:08b}".format(1<<3))
print("{:08b}".format(ord("c")^(1<<3)))

print()
str = "Xq|`gf(bm{|(nibfq)"
for c in str:
    print(char(ord(c)^(1<<3)))