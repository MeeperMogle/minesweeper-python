import functools, random, sys

def generateBoard(boardWidth = 10, boardHeight = 20, mineAmount = 25):
    boardSize = (boardWidth, boardHeight)
    totalSquares = boardWidth * boardHeight

    minePositions = []
    squares = [0] * totalSquares
    
    for i in range(0, mineAmount):
        newMineBurialPosition = -1
        while newMineBurialPosition in [minePositions, -1]:
            newMineBurialPosition = random.randint(0, totalSquares-1)
        minePositions.append(newMineBurialPosition)
    
    for i in range(0, len(squares)):
        squares[i] = getAdjacentMineCount(i, minePositions, totalSquares, boardWidth)
        
    return squares

def isAdjacent(square, middle, totalSquares, boardWidth):
    # Must be inside the board
    if square < 0 or square > totalSquares:
        return False
        
    # Horizontal position at most 1 apart
    squareRowPosition = square % boardWidth
    middleRowPosition = middle % boardWidth
    return abs(squareRowPosition - middleRowPosition) < 2

def getAdjacentMineCount(squarePosition, minePositions, totalSquares, boardWidth):
    # Only matter if they're not a mine themselves
    if squarePosition not in minePositions:
        rightAbove, rightBelow = (squarePosition - boardWidth, squarePosition + boardWidth)
        
        around = [rightAbove - 1, rightAbove, rightAbove + 1, rightBelow -1, rightBelow, rightBelow + 1,
                    squarePosition - 1, squarePosition + 1]
                    
        adjacent = list(map(lambda x: isAdjacent(x, squarePosition, totalSquares, boardWidth), around))
        
        adjtMines = 0
        
        for i in range(0, len(around)):
            try:
                adjtMines = adjtMines + 1 if adjacent[i] and around[i] in minePositions else adjtMines
            except IndexError as e:
                pass
        return adjtMines
    # If they are, indicate m(ine)
    else:
        return "m"

if __name__ == "__main__":
    boardWidth = 10 if len(sys.argv) < 2 or not sys.argv[1].isdigit() else int(sys.argv[1])
    boardHeight = 20 if len(sys.argv) < 3 or not sys.argv[2].isdigit() else int(sys.argv[2])
    mineAmount = 25 if len(sys.argv) < 4 or not sys.argv[3].isdigit() else int(sys.argv[3])
    
    board = generateBoard(boardWidth, boardHeight, mineAmount)
    
    for i in range(0, len(board)):
        print(str(board[i]) + ' ', end='')
        if (i+1) % boardWidth == 0:
            print('')