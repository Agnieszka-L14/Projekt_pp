numbers=[]
numbers_total =int(input(" Podaj liczbe elementów zbioru: "))
for i in range(numbers_total):
    numbers.append(int(input("Podaj " +str(i+1)+ " liczbę : ")))
numbers.sort(reverse=True)
numbers_whitout_duplicates =[]
for number in numbers:
    if number not in numbers_whitout_duplicates:
        numbers_whitout_duplicates.append(number)
print(numbers_whitout_duplicates)
