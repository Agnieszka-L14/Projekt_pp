# zadanie 1

imie = "Maria"
wiek = 25
miasto = "Kraków"

print("Użytkownik ma na imię " + imie + " , ma " + str(wiek) + " lat , mieszka w mieście " + miasto + ".")

# zadanie 2
kwadrat_1 = 2
kwadrat_2 = 7
kwadrat_3 = 11
kwadrat_4 = 19

pole_kwadratu1 = kwadrat_1 ** 2
pole_kwadratu2 = kwadrat_2 ** 2
pole_kwadratu3 = kwadrat_3 ** 2
pole_kwadratu4 = kwadrat_4 ** 2

print("pola kwadratów to :", pole_kwadratu1, pole_kwadratu2, pole_kwadratu3, pole_kwadratu4)

# obwód
obwod1 = kwadrat_1 * 4
obwod2 = kwadrat_2 * 4
obwod3 = kwadrat_3 * 4
obwod4 = kwadrat_4 * 4

print("Obwody kwadratow to :", obwod1, obwod2, obwod3, obwod4)

# przekątna
przekatna1 = (2 ** 0.5) * kwadrat_1
przekatna2 = (2 ** 0.5) * kwadrat_2
przekatna3 = (2 ** 0.5) * kwadrat_3
przekatna4 = (2 ** 0.5) * kwadrat_4

print("przekatne kwadratów to", round(przekatna1, 2), round(przekatna2, 2), round(przekatna3, 2), round(przekatna4, 2))

# zadanie 3
srodki_początkowe = 46567.
srodki_rok1 = 46567. * 1.075
srodki_rok2 = srodki_rok1 * 1.075
srodki_rok3 = srodki_rok2 * 1.075

print("Srodki po roku", round(srodki_rok1, 2))
print("Srodki po drugim roku", round(srodki_rok2, 2))
print("Srodki po trzecim roku", round(srodki_rok3, 2))
print("Zysk wynosi ", round((srodki_rok3 - srodki_początkowe), 2), "zł")
srodki_początkowe *= 1.075
print("środki po 1 roku", round(srodki_początkowe, 2), "zł")
srodki_początkowe *= 1.075
print("środki po drugim roku", round(srodki_początkowe, 2), "zł")
srodki_początkowe *= 1.075
print("Środki po trzecim roku", round(srodki_początkowe, 2), "zł")
