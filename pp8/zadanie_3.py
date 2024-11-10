#ziarnka na szachownicy, plansza z 64 polami
s = 0
for i in range (64):
    s += 2 ** i

print("suma wszystkich ziarenek na szachownicy to " + str(s))

#założenia : waga jednego ziarna to 0,4mg -> 0.0004g

#1kg-1000g
#1000kg -1t

tons =int(s * 0.0004 / 1000 / 1000)
print("to bedzie : " + str(tons))

#roczna produkcja zbożna na świecie 782 mln ton
years =int(tons/782000000)
print("Ilośc lat " + str(years))

#pociąg może przewieźć 2200 ton
trains = int(tons/2200)
print ("ilość pociągów ", trains)