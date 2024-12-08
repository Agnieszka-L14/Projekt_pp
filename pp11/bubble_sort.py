numbers= [4, 5, 2, 1, 3, 123, 9, 29, 39, 38, 100, 0, 0, 18]
swapped = True
while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            swapped = True
print(numbers)