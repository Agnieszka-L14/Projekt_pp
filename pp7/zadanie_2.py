point =int(input ("Podaj liczbe punktów otrzymaną przez studenta (0-100): "))

if point >= 95:
    print("Ocena studenta to 5,0 .")
elif 95 > point >= 84:
    print("Ocena studenta to 4.5 ."),
elif 84 > point >= 70 :
    print("Ocena studenta to 4.0 ."),
elif 70 > point >= 60:
    print("Ocena studenta to 3.5 ."),
elif 60 > point >= 50:
    print("Ocena studenta to 3.0 ."),
else:
    print("Nie zdałeś , otrzymałeś 2.0")

print("Twoją ocena jest :", end=" ")
if point >= 95:
    print("bardzo dobra (5.0)")
elif point > 84:
    print("ocena (4.5)")
elif point >=70:
    print("ocena 4.0")
elif point >60:
    print(" ocena 3.5")
elif point >50:
    print("ocena 3.0")
else:
    print("ocena 2.0")
