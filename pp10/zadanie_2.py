#Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
#wyświetli poniższe informacje:
#• zestaw wylosowanych wyników,
#• wyrzucaną wartość za 8 razem,
#• liczbę wyrzuconych szóstek,
#• maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import  random
numbers =[]
counter = 0
DICE_ROLLS_TOTAL = 16

for i in range (DICE_ROLLS_TOTAL):
    numbers.append(random.randint(1,6))


print("podane liczby to : ", numbers)
print("Liczba z indeksem 8 to: ", numbers[7])


for roll in numbers:
    if roll == 6:
        counter = counter + 1

print("Wyrzucono ", counter, "razy szóstkę ")

in_row_value_tem =numbers[0]
in_row_total_tem =0
in_row_value =0
in_row_total = 0
for roll in numbers:
    if roll == in_row_value_tem:
        in_row_total_tem +=1
    else:
        in_row_value_tem = roll
        in_row_total_tem = 1
    if in_row_total_tem > in_row_total:
        in_row_value = in_row_value_tem
        in_row_total = in_row_total_tem
print("Pod rząd wyrzucono ", in_row_total , " razy wartość ", str(in_row_value) , ".")


