a = 1
b = 4
print(a,b)
temp = a
a = b
b= temp
print(a,b)

a,b = b,a
print(a,b)

numbers=[1, 2, 3]
numbers[0], numbers[1]= numbers[1], numbers[0]
print(numbers)

#sortowanie bąbelkowe
# [4, 5, 2, 1]
# [4, 2, 1, 5]
# [2, 1, 4, 5]
# [1, 2, 4, 5]

numbers = [4, 5, 1, 2, 6, 3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers = ["C", "D", "A", " ", "F", "Z"]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

list_1 =[9]
list_2 = list_1 #kopiuje nazwę listy a  nie zawartość
list_2[0] =13
print(list_1)
#kopiowanie za pomocą wycinków
list_1 =[9]
list_2 = list_1[:] #kopiuje całą listę
list_2[0] =13
print(list_1)
#wycinki

#lista [start:end]
numbers =[10, 8, 6, 4, 2]
new_numbers = numbers[1:4]
print(new_numbers)

numbers =[10, 8, 6, 4, 2]
new_numbers = numbers[-4:-1]
print(new_numbers)

numbers =[10, 8, 6, 4, 2]
new_numbers = numbers[3:]
print(new_numbers)

#operatory in, not in
numbers =[1, 2, 3, 4, 5]
print(5 in numbers)
print(6 not in numbers)

#wyrażenia listowe

numbers =[i for i in range(1,101)]
print(numbers)

numbers =[99 for i in range(1,101)]
print(numbers)

numbers =[i*2 for i in range(1,101)]
print(numbers)

numbers =[i*2 for i in range(1,101) if i %2==0]
print(numbers)
