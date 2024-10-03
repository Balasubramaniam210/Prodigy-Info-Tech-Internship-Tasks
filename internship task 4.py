# Sudoku Solver Program

def print_board(board):
    """ Function to print the Sudoku board """
    for row in board:
        print(" ".join(str(num) for num in row))


def find_empty_location(board):
    """ Find an empty location in the board (represented by 0) """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)  # Return the position of the empty cell
    return None


def is_valid(board, num, pos):
    """ Check if it's valid to place 'num' at 'pos' """
    
    # Check row
    for col in range(9):
        if board[pos[0]][col] == num and pos[1] != col:
            return False
    
    # Check column
    for row in range(9):
        if board[row][pos[1]] == num and pos[0] != row:
            return False
    
    # Check 3x3 grid
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True


def solve_sudoku(board):
    """ Solve the Sudoku using backtracking """
    empty = find_empty_location(board)
    
    if not empty:
        return True  # Puzzle solved
    
    row, col = empty
    
    for num in range(1, 10):  # Try numbers from 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Temporarily place the number
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack if the number doesn't lead to a solution
    
    return False


# Example Sudoku puzzle (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku puzzle before solving:")
print_board(board)

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("\nSudoku puzzle solved:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku puzzle.")
