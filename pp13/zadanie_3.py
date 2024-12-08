# . Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.

import random

first_symbol = "A"
Last_symbol = "H"
number_of_letters = 6


# zbior ["a", "b","c"..]
# kod znaku A =65
# funkcja ord
def draw_letter():
    return chr(random.randint(ord(first_symbol), ord(Last_symbol)))


def draw_row():
    return [draw_letter() for _ in range(number_of_letters)]


def check(row):
    first_letter = row[0]
    for element in row:
        if first_letter != element:
            return False
    return True


counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

print(draw_letter())
print(draw_row())
print(check(draw_row()))

print(ord("A"))
print(ord("B"))
print(chr(66))
