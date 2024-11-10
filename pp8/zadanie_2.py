# wyświetlenie macierzy

large = int(input("Wprowadź wielkość macierzy : "))
char = input("Wprowadź znak z którego bedzie zbudowana macierz : ")

for _ in range(large):
    for _ in range(large):
        print(char, end=" ")
    print()



