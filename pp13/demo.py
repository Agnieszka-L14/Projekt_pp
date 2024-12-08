# zsumuj wszytskie elementy listy

def sum_numbers(numbesr):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum


numbers = [1, 2, 3, 4, 5]
print(sum_numbers(numbers))


def scope_test():
    x = 123
    print(x)
scope_test()
#print(x)

x=132
def scope_test_1():
    x=999 #zmienna lokalna nadpisała zmienna globalną
    print("W środku funkcji " ,x )
scope_test_1()
print("Poza funkcją  " ,x )

def scope_test_1():
    global x
    x=999 #zmienna lokalna nadpisała zmienna globalną
    print("W środku funkcji " ,x )
scope_test_1()
print("Poza funkcją  " ,x )

def change_value(n):
    print("Przed zmianą :" , n)
    n+=1
    print("Po zmianie :" ,n )
value =7
change_value(value)
print(value)

def change_value(my_list_1):
    my_list_1 = [0,0]

my_list_2 =[1,2]
change_value(my_list_2)
print(my_list_2)

def change_value(my_list_1):
    my_list_1[0] = 999

my_list_2 =[1,2]
change_value(my_list_2)
print(my_list_2)