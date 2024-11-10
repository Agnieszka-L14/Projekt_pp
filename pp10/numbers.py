#wylosuj 10 dowolnych liczb od 1-100
#umieść w liście
#wyświetlaj listę

import  random
numbers =[]
for i in range (10):
    number =random.randint(1,100)
    numbers.append(number)
print(numbers)