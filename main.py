import minesweeperBoard

# Printing a default-size, random board
print(minesweeperBoard.generate_board())

# Example: Visualising the board
customWidth = 15
customHeight = 20
mines = 30
customBoard = minesweeperBoard.generate_board(customWidth, customHeight, mines)

for i in range(0, len(customBoard)):
    print(customBoard[i], end=' ')
    if (i+1) % customWidth == 0:
        print('')