numbers = (1, 2, 3, 4, 5)  # krotka
krotka = 1, 2, 3  # też są krotka bez nawiasu

number=() # pusta krotka

number_s = (1,) #- krotka jednoargumentowa

print(numbers[:]) #wycinek, kopia całości

numbers_list = [x for x in range(10) if x%2 == 0] # dla listy
numbers_tuple = tuple(x for x in range(10) if x%2 == 0) # dla krotki
numbers_1=(1,2,3,4,5)
numbers_1[0]=999 # nie zadziała , bo nie można modyfikować
del numbers_1[0] # też nie zadziała

del numbers_1 # to zadziała bez problemu

print(len(numbers)) # jest ok
print(numbers * 2)

#przekonwertowanie listy na krotkę
ooo=[1,2,3,4,5]
 ooo = tuple.ooo

letters = tuple("Ala ma kota")
print(letters)




