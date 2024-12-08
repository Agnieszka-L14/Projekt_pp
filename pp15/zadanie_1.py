# Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
# Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
# i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
# powinna zwrócić None.

def safe_int():
    try:
        arg = input("podaj argument : ")
        print("przekonwertowany argument to ", int(arg))
    except:
        print("None")

safe_int()