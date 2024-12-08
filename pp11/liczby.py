#liczby z zakresu 1-300 podzielne przez 3 i 7

print(len([i for i in range (1,301) if i%3 ==0 and i%7==0]))

print([[1,2],[3,4]])

row = [1, 2]
matrix = [row[:], row[:]]
print(matrix)
matrix[0][0]=99
print(matrix)

#tworzymy plnsze do gry w szachy
chess_row =["--" for i in range(8)]
print(chess_row)
chessboard =[chess_row[:] for _ in range(8)]
print(chessboard)

chessboard =[["--" for i in range(8)]for i in range(8)]
WHITE_POWN =("BP")
BLACK_POWN =("CP")
chessboard[3][4]=WHITE_POWN
chessboard[2][7]=BLACK_POWN

for chess in chessboard:
    for chess_squere in chess_row:
        print(chess_squere , end=" ")
    print()