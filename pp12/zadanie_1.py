#Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
#ilość razy, w poziomie lub w pionie.

def char_print(sign="*", number =10, vertical=False):
    for i in range(number):
        if vertical:
            print(sign)
        else:
            print(sign + "" ,end=" ")

    if not vertical:
        print()
char_print()
char_print("%", 20, vertical=True)
char_print("%", 20, vertical=False)






