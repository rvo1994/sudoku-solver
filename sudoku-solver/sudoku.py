import copy
import random

def main():
    all_values, sudoku_potential_values = [1,2,3,4,5,6,7,8,9], {}
    filepath = input("Provide the file name of a sudoku in text format to solve: ")
    sudoku_in_progress = {}
    with open (filepath,'r') as f:
        lines = f.readlines()
        for line_number,line in enumerate(lines):
            for i in range(9):
                sudoku_in_progress[(i+1) + line_number*9] = int(line[i])
    count_scans = 0
    for cell in range(1,82):
        if sudoku_in_progress[cell] > 0:
            sudoku_potential_values[cell] = sudoku_in_progress[cell]
        else:
            sudoku_potential_values[cell] = all_values

    lines, columns, squares = {}, {}, {}
    for value in all_values:
        lines[value] = [(line_cells + ((value-1) * 9)) for line_cells in range(1,10)]
        columns[value] = [(value + column_cells) for column_cells in range(0,81,9)]
    for i in range(1,3):
        squares[i] = lines[1][((3*i - 3) % 9): ((i*3) % 9)] + lines[2][((3*i - 3) % 9): ((i*3) % 9)] + lines[3][((3*i - 3) % 9): ((i*3) % 9)]
    for i in range (4,6):
        squares[i] = lines[4][((3*i - 3) % 9): ((i*3) % 9)] + lines[5][((3*i - 3) % 9): ((i*3) % 9)] + lines[6][((3*i - 3) % 9): ((i*3) % 9)]
    for i in range (7,9):
        squares[i] = lines[7][((3*i - 3) % 9): ((i*3) % 9)] + lines[8][((3*i - 3) % 9): ((i*3) % 9)] + lines[9][((3*i - 3) % 9): ((i*3) % 9)]
    for i in range(3,10,3):
        squares[i] = columns[7][(i-3):i] + columns[8][(i-3):i]  + columns[9][(i-3):i]
    
    sudoku_in_progress, sudoku_potential_values, count_scans = scanning(sudoku_in_progress, sudoku_potential_values, count_scans, lines, columns, squares)
    
    saved_sudoku_in_progress, saved_sudoku_potential_values = copy.deepcopy(sudoku_in_progress), copy.deepcopy(sudoku_potential_values)
    
    while 0 in sudoku_in_progress.values():
        if [] not in sudoku_potential_values.values():
            length_potential_values = [len(value) for value in sudoku_potential_values.values() if type(value) == list and len(value) > 1]
            least_potential_values = min(length_potential_values)
            cells_with_least_potential_values = [key for key, value in sudoku_potential_values.items() if (type(value) == list) and (len(value) == least_potential_values)]
            cell_to_guess = random.choice(cells_with_least_potential_values)
            sudoku_in_progress[cell_to_guess] = sudoku_potential_values[cell_to_guess][0]
            sudoku_in_progress, sudoku_potential_values, count_scans = scanning(sudoku_in_progress, sudoku_potential_values, count_scans, lines, columns, squares)
        else:
            sudoku_in_progress, sudoku_potential_values = copy.deepcopy(saved_sudoku_in_progress), copy.deepcopy(saved_sudoku_potential_values)
            sudoku_potential_values[cell_to_guess].remove(sudoku_potential_values[cell_to_guess][0])

    sudoku_solved = sudoku_in_progress
    cell_values = [str(value) for key, value in sudoku_solved.items()]
    readable_solved_sudoku = [''.join(cell_values[i:i+9]) for i in range(0,81,9)]
    for line in readable_solved_sudoku:
        print(line)

def find_group(dict,cell):
  for key, value in dict.items():
      if cell in value:
          return key

def scanning(sudoku_in_progress, sudoku_potential_values, count_scans, lines, columns, squares):
    count_cumulative_unproductive_iterations = 0
    count_scans += 1
    while (0 in sudoku_in_progress.values()) and (count_cumulative_unproductive_iterations < 81):
        for cell in range(1,82):
            if sudoku_in_progress[cell] == 0:
                incompatible_values, potential_values_line, potential_values_column, potential_values_square = [], [], [], []
                for key, value in sudoku_in_progress.items():
                    if ((value > 0) and (value in sudoku_potential_values[cell]) and (key in lines[find_group(lines,cell)] or key in columns[find_group(columns,cell)] or key in squares[find_group(squares,cell)])):
                        incompatible_values.append(value)
                sudoku_potential_values[cell] = [value for value in sudoku_potential_values[cell] if value not in incompatible_values]
                if len(incompatible_values) == 0:
                    count_cumulative_unproductive_iterations += 1
                else:
                    count_cumulative_unproductive_iterations = 0
                if len(sudoku_potential_values[cell]) == 1:
                    sudoku_in_progress[cell] = sudoku_potential_values[cell][0]
                else:
                    for key, value in sudoku_potential_values.items():
                        if (sudoku_in_progress[key] == 0) and (key in lines[find_group(lines,cell)]) and (key != cell):
                            potential_values_line.append(value)
                        if (sudoku_in_progress[key] == 0) and (key in columns[find_group(columns,cell)]) and (key != cell):
                            potential_values_column.append(value)
                        if (sudoku_in_progress[key] == 0) and (key in squares[find_group(squares,cell)]) and (key != cell):
                            potential_values_square.append(value)
                    potential_values_line_int, potential_values_column_int, potential_values_square_int = [y for x in potential_values_line for y in x], [y for x in potential_values_column for y in x], [y for x in potential_values_square for y in x]
                    for value in sudoku_potential_values[cell]:
                        if (potential_values_line_int.count(value) == 0) or (potential_values_column_int.count(value) == 0) or (potential_values_square_int.count(value) == 0):
                            sudoku_in_progress[cell] = value
            else:
                 pass
    return sudoku_in_progress, sudoku_potential_values, count_scans

if __name__ == "__main__":
    main()