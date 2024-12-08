#wylosuj trzy liczby ze zbioru od 1-10 , bez powtórzeń, posortuj wynik

import random

numbers =[i for i in range(1,11)]
random_number =random.sample(numbers,3) #losowanie liczb ze zbioru bez powtórzeń
random_number.sort()
print(random_number)

