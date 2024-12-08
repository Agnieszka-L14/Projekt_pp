#Napisz funkcję zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
#Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def marge_lists(sources, target):
    for element in sources:
        if element not in target:
            target.append(element)


def transform_data(list_1,list_2,list_3):
    result =[]
    marge_lists(list_1,result)
    marge_lists(list_2,result)
    marge_lists(list_3,result)
    return tuple(result)


print(transform_data([1,2],[1,1],[4,4,4]))
print(transform_data([1,2,3],[1,2,3],[4,5,6]))
print(transform_data(["ala", "ma"],["ala", "ma", "kota"],["mysz"]))
