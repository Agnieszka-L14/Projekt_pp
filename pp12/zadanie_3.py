print("Obliczenie wskaźnikia BMI")


def BMI():
    a = int(input("podaj swój wzrost w cm : "))
    b = float(input("podaj swoja wagę w kg : "))
    c = b / ((a / 100) ** 2)

    print("Twoje BMI to :", c)


BMI()

weight_in_kg = float(input("podaj swoja wagę w kg : "))
height_in_cm = float(input("podaj swój wzrost w cm : "))


def calculate(weight_in_kg, height_in_m):
    return weight_in_kg / height_in_m ** 2



def determine_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi >= 18.5 and bmi < 25:
        return "Waga prawidłowa"
    elif bmi >= 25 and bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


bmi = calculate(weight_in_kg, height_in_cm * 0.01)
category = determine_category(bmi)

print("Wskażnik BMI: ", round(bmi,2))
print("Kategoria :", category)
