import random

blank_square = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"]
chess_board = [[blank_square for i in range(8)] for i in range(8)]
counter = 0
while counter < 5:
    row = random.randint(0, 7)
    col = random.randint(0, 7)
    if chess_board[row][col] == blank_square:
        chess_board[row][col] = pieces[counter]
        counter +=1
for row in range(len(chess_board)):
    if row ==0:
        print(" ", "A","B","C","D","E","F","G","H", sep= " ")
    print(row +1 , end =" ")

    for col in range(len(chess_board[row])):
        print(chess_board[row][col], end=" ")
    print()