#Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
#parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
#przynajmniej dzielą się przez 9.

for i in range(1,101):
    if(i > 90 and i%2==0 ) or (i%2 != 0  and i%9==0):
         print(i)

counter = 0
for i in range(1,101):
    if (i > 90 and i%2==0 ) or (i%2 != 0  and i%9==0) :
        counter += 1
print("Ilość liczb spełniajacych warunek to : " + str(counter) + ".")