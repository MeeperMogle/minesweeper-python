import random
import sys


def generate_board(board_width=10, board_height=20, mine_amount=25):
    total_squares = board_width * board_height

    mine_positions = []
    squares = [0] * total_squares
    
    for i in range(0, mine_amount):
        new_mine_burial_position = -1
        while new_mine_burial_position in [mine_positions, -1]:
            new_mine_burial_position = random.randint(0, total_squares-1)
        mine_positions.append(new_mine_burial_position)
    
    for i in range(0, len(squares)):
        squares[i] = get_adjacent_mine_count(i, mine_positions, total_squares, board_width)
        
    return squares


def is_adjacent(square, middle, total_squares, board_width):
    # Must be inside the board
    if square < 0 or square > total_squares:
        return False
        
    # Horizontal position at most 1 apart
    square_row_position = square % board_width
    middle_row_position = middle % board_width
    return abs(square_row_position - middle_row_position) < 2


def get_adjacent_mine_count(square_position, mine_positions, total_squares, board_width):
    # Only matter if they're not a mine themselves
    if square_position not in mine_positions:
        right_above, right_below = (square_position - board_width, square_position + board_width)
        
        around = [right_above - 1, right_above, right_above + 1, right_below - 1, right_below, right_below + 1,
                  square_position - 1, square_position + 1]
                    
        adjacent = list(map(lambda x: is_adjacent(x, square_position, total_squares, board_width), around))
        
        adjacent_mines = 0
        
        for i in range(0, len(around)):
            try:
                adjacent_mines = adjacent_mines + 1 if adjacent[i] and around[i] in mine_positions else adjacent_mines
            except IndexError as e:
                pass
        return adjacent_mines
    # If they are, indicate m(ine)
    else:
        return "m"

if __name__ == "__main__":
    width = 10 if len(sys.argv) < 2 or not sys.argv[1].isdigit() else int(sys.argv[1])
    height = 20 if len(sys.argv) < 3 or not sys.argv[2].isdigit() else int(sys.argv[2])
    m_amount = 25 if len(sys.argv) < 4 or not sys.argv[3].isdigit() else int(sys.argv[3])
    
    board = generate_board(width, height, m_amount)
    
    for i in range(0, len(board)):
        print(str(board[i]) + ' ', end='')
        if (i+1) % width == 0:
            print('')