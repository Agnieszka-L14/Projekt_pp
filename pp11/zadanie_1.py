import random

user_numbers = []
hit_total = 0
numbers = [i for i in range(1, 50)]
random_number = random.sample(numbers, 6) #bez powtórzeń
random_number.sort()

for i in range(6):
    user_numbers.append(int(input("Podaj  " + str(i + 1) + " liczbę od 1 do 49 : ")))
print(user_numbers)
user_numbers.sort()
print(random_number)
for number in user_numbers:
    if number in random_number:
        hit_total += 1
print("trafiono ", hit_total, " liczb.")