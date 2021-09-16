def find_empty(grid):
    """Find next empty position"""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(grid, num, pos):
    """Check if row, col and box are valid"""
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(grid):
    """Recursive call to solve until done"""
    find = find_empty(grid)
    if not find:
        return True

    row, col = find
    for i in range(1, 10):
        if valid(grid, i, (row, col)):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False    

def sudoku_solver(grid):
    """Sudoku solver"""
    print(grid)
    for row in range(9):
        for col, num in enumerate(grid[row]):  
            if not valid(grid, num, (row, col)) and num != 0:
                return False 
    solve(grid)
    return grid

