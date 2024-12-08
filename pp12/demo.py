name = input("jak masz na imię :") #funkcja input
print(" Witaj {} ".format(name) )


print("raz", "dwa","trzy")

def introduce (first_name , last_name):
    print("cześć jestem " , first_name , last_name + " ")
introduce(first_name="Agnieszka", last_name ="Lichota")
def introduce (first_name ="Jan" , last_name = "Kowalski"):
    print("cześć jestem " , first_name , last_name + " ")
introduce(first_name="Agnieszka")
print("raz", "dwa","trzy" , sep="-")

def show_name (name="Jan"):
    print("Cześć mam na imię {}" .format(name))
    return None
print(show_name("Agnieszka"))
show_name("Agnieszka")
show_name()

def empty_function():
    pass
print(empty_function())

if empty_function() is None:
    print("funkcja nic nie zwróciła!!!")
