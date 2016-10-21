# Minesweeper

Basic Minesweeper board generator. Randomly creates a 1D list/array representing a 2D board of Minesweeper.

List contains numbers of 0-8 (adjacent mines) with 'm' representing a mine.
> [0, 0, 1, 'm', 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 0, 2, 'm', 3, 'm', 1, 0, 'm', 2, 2, 1, 3, 'm', 4, 2, 2, 0, ...

All arguments are optional. Default values are
- width: 10
- height: 20
- mines: 25

#### Usage examples: Imported (returns 1D list/array)

```python
import minesweeperBoard

# Printing a default-size, random board-list.
print(minesweeperBoard.generateBoard())

# Visualising the board with print()
customWidth = 15
customHeight = 20
mines = 30
customBoard = minesweeperBoard.generateBoard(customWidth, customHeight, mines)

for i in range(0, len(customBoard)):
    print(customBoard[i], end=' ')
    if (i+1) % customWidth == 0:
        print('')
```

#### Usage examples: Command line (prints random board)

```python
python minesweeperBoard.py
python minesweeperBoard.py 10
python minesweeperBoard.py 10 20
python minesweeperBoard.py 10 20 25
```
