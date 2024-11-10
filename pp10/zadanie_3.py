#Napisz skrypt, który znajdzie najczęściej występującą cyfrę w zbiorze.
#Np. w zbiorze [4, 1, 2, 9, 4, 4] najczęściej występującą cyfrą jest 4,
#występuje 3 razy.

digits =[1, 2, 3, 3, 4, 1, 2, 3]
frequency =[0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ]
for i in digits:
    frequency[i] = frequency[i] + 1
most_common =0
for a in range(len(frequency)):
    if frequency[a] >frequency[most_common]:
        most_common = a

print("Najczęściej wystepujaca cyfrą jest " , str(most_common), " wystąpiła " , str(frequency[most_common]),  "razy")
print(digits)
print(frequency)
