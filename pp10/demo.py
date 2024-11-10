a = 3
b = 2
c = 11
d = 2
e = 20

print(a, b, c, d, e)
numbers =[3, 2, 11, 2, 20]
print(numbers)

fruits=['apple', 'banana', 'cherry']
print(fruits)
#własności list
# uporządkowanie
numbers_1=[1, 2, 3]
print(numbers_1)
#pozwala przechowywać duplikaty
numbers =[1, 1, 1, 1]
print(numbers)
# pozwala przechowywac elementy o różnych typach
numbers = [1, "jeden", True, 2.0, 9]
print(numbers)

#każdy element z listy posiada indeks , elementy zawsze numerowane od 0
print(numbers[0], numbers[1])

#indeksy ujemne ostani element -1
print(fruits[-1])

#wyznaczanie długości listy i usuwanie
print(len(fruits),fruits)
del fruits[0]
print(len(fruits),fruits)

#usuwanie listy
#del fruits
#print(len(fruits))

fruits = ['apple', 'banana', 'cherry']
print(len(fruits)) #len to funkacja
fruits.append('plum') #metoda
print(fruits)
fruits.insert(0, "plum")
print(fruits)

for i in range(len(fruits)):
    print(fruits[i])
for fruit in fruits:
    print(fruit)


