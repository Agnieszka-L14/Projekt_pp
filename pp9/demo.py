temp = 12
is_sunshining =False
# jeśli będzie dodatnia temperatutra i bedzie słonecznie to pójdziemy na spacer , w innym przypadku zostajemy w domu
if temp>0 and is_sunshining :
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-"*20)

#jeśli będzie ujemna temperatura lub bedzie pochmurnie to zostajemy w domu , a jeśli nie , idziemy na spacer

if not(temp < 0 or not is_sunshining) :
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-"*20)

#operatory logiczne
# and - koniungcja czytamy jako i
# or - alternatywa , czytamy jako lub
# not - negacja , czytamy jak nie

#iterujemy od 0-9 (10 iteracji)
#wyświetlamy cyfrę chyba , że
#będzie to liczba parzysta lub liczba większa od 6 to wyświetl *

for i in range (10):
    if i %2 ==0 or i>6:
        print("*")
    else:
        print(i)

a,b,c =2,3,4
if a<b and b<c:
    print("!!!")
if a<b<c:
    print("!!!")


a=5
b=3
#koniungcja bitowa
print(a, "&" , b , " = ", a & b)
print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a&b))
print()
#alternatywa bitowa
print(a, "|" , b , " = ", a | b)
print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a|b))
print()

#alternatywa rozłączna bitowa
print(a, "^" , b , " = ", a ^ b)
print(bin(a))
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a^b))

print()
#Przesunięcie w prawo
print(a, ">>" , b , " = ", a >> b)
print(bin(a))
print("{:08b}".format(a))

print("-" * 8)
print("{:08b}".format(a>>b))

#Przesunięcie w lewo
print(a, "<<" , b , " = ", a <<b)
print(bin(a))
print("{:08b}".format(a))

print("-" * 8)
print("{:08b}".format(a<<b))
print()
#negacja bitowa
print("~" + str(a), " = ", ~a)

print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))