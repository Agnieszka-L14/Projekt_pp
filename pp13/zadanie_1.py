# Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy


def escal(n, e):
    n = n[:]  # zabezpieczenie przed modyfikacją listy
    for i in range(len(n)):
        n[i] = n[i] ** e

    return n

#def escal2(n, e): do sprawdzenia i poprawy
   # result =[]
    #for a in n:
      #  result.append(a**e)
    # return result

def escal3(n, e):
    return [x**e for x in n]


n = [1, 2, 3, 4]
print(escal(n,2))

print(escal3(n,2))


