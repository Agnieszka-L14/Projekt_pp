def perimeter(a, b):
    print("obwód prostokata to ", (2 * a + 2 * b))
def square(a,b):
    print("pole prostokąta  ", ( a * b))

def diagonal(a,b):
    d=((a**2 + b**2)**0.5)
    print(" Przekątna prostokąta to", d)

perimeter(4, 5)
perimeter(2678, 5678)
perimeter(344555, 788998)

square(4, 5)
square(2678, 5678)
square(344555, 788998)

diagonal(4, 5)
diagonal(2678, 5678)
diagonal(344555, 788998)

def perimeter(a, b):
    return 2 * a + 2 * b
def square(a,b):
    return  a * b
def diagonal(a,b):
    return ((a**2 + b**2)**0.5)

def show_resoult(a,b):
    print("Prostokąt o bokach {}  i {}: ".format(a,b))
    print("Obwód: ", perimeter(a,b))
    print("pole powierzchni : ", square(a,b))
    print("długość przekątnej : ", diagonal(a,b))
    print()
show_resoult(4, 5)
show_resoult(2678, 5678)
show_resoult(344555, 788998)