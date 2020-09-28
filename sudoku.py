def create_dict(filepath):
    sudoku_unsolved = {}
    with open (filepath,'r') as f:
        lines = f.readlines()
        for line_number,line in enumerate(lines):
            for i in range(0,9):
                sudoku_unsolved[(i+1) + line_number*9] = int(line[i])
    return sudoku_unsolved


all_values = [1,2,3,4,5,6,7,8,9]
sudoku_potential_values = {}
choose_sudoku = input("Provide the file name of a sudoku in text format to solve: ")
sudoku_unsolved = create_dict(choose_sudoku)
sudoku_in_progress = sudoku_unsolved
count_scans = 0
for cell in range(1,82):
    if sudoku_in_progress[cell] > 0:
        sudoku_potential_values[cell] = sudoku_in_progress[cell]
    else:
        sudoku_potential_values[cell] = all_values

lines = {}
columns = {}
squares  = {}
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

def find_line(dict,cell):
  for key, value in dict.items():
      if cell in value:
          return key
def find_column(dict,cell):
  for key, value in dict.items():
      if cell in value:
          return key
def find_square(dict,cell):
  for key, value in dict.items():
      if cell in value:
          return key

def scanning():
    global sudoku_in_progress, sudoku_potential_values, count_scans
    count_cumulative_unproductive_iterations = 0
    count_scans += 1
    print("Starting scanning number {}".format(count_scans))
    while (0 in sudoku_in_progress.values()) and (count_cumulative_unproductive_iterations < 81):
        for cell in range(1,82):
            if sudoku_in_progress[cell] == 0:
                incompatible_values = []
                potential_values_line = []
                potential_values_column = []
                potential_values_square = []
                for key, value in sudoku_in_progress.items():
                    if ((value > 0) and (value in sudoku_potential_values[cell]) and (key in lines[find_line(lines,cell)] or key in columns[find_column(columns,cell)] or key in squares[find_square(squares,cell)])):
                        incompatible_values.append(value)
                sudoku_potential_values[cell] = [value for value in sudoku_potential_values[cell] if value not in incompatible_values]
                print("Removing {} from cell {}. {} are still potential values" .format(incompatible_values, cell, sudoku_potential_values[cell]))
                if len(incompatible_values) == 0:
                    count_cumulative_unproductive_iterations += 1
                else:
                    count_cumulative_unproductive_iterations = 0
                if len(sudoku_potential_values[cell]) == 1:
                    sudoku_in_progress[cell] = sudoku_potential_values[cell][0]
                    print("The value of cell {} is {} because is it the only value that can be there".format(cell,sudoku_in_progress[cell]))
                else:
                    for key, value in sudoku_potential_values.items():
                        if (sudoku_in_progress[key] == 0) and (key in lines[find_line(lines,cell)]) and (key != cell):
                            potential_values_line.append(value)
                        if (sudoku_in_progress[key] == 0) and (key in columns[find_column(columns,cell)]) and (key != cell):
                            potential_values_column.append(value)
                        if (sudoku_in_progress[key] == 0) and (key in squares[find_square(squares,cell)]) and (key != cell):
                            potential_values_square.append(value)
                    potential_values_line_int = [y for x in potential_values_line for y in x]
                    potential_values_column_int = [y for x in potential_values_column for y in x]
                    potential_values_square_int = [y for x in potential_values_square for y in x]
                    for value in sudoku_potential_values[cell]:
                        if (potential_values_line_int.count(value) == 0) or (potential_values_column_int.count(value) == 0) or (potential_values_square_int.count(value) == 0):
                            sudoku_in_progress[cell] = value
                            print("The value of cell {} is {} because the value can only be in that cell".format(cell, value))
            else:
                 pass
    print("Scanning number {} completed".format(count_scans))

scanning()

import copy
saved_sudoku_in_progress = copy.deepcopy(sudoku_in_progress)
saved_sudoku_potential_values = copy.deepcopy(sudoku_potential_values)

def reset_values():
    global sudoku_in_progress, sudoku_potential_values, saved_sudoku_in_progress, saved_sudoku_potential_values
    sudoku_in_progress = copy.deepcopy(saved_sudoku_in_progress)
    sudoku_potential_values = copy.deepcopy(saved_sudoku_potential_values)

while 0 in sudoku_in_progress.values():
    if [] not in sudoku_potential_values.values():
        length_potential_values = [len(value) for value in sudoku_potential_values.values() if type(value) == list and len(value) > 1]
        least_potential_values = min(length_potential_values)
        cells_with_least_potential_values = [key for key, value in sudoku_potential_values.items() if (type(value) == list) and (len(value) == least_potential_values)]
        import random
        cell_to_guess = random.choice(cells_with_least_potential_values)
        print("Trying with {} as value for cell {}.".format(sudoku_potential_values[cell_to_guess][0],cell_to_guess))
        sudoku_in_progress[cell_to_guess] = sudoku_potential_values[cell_to_guess][0]
        scanning()
    else:
        reset_values()
        print("Going back to last save as {} as value for cell {} is not a good guess".format(sudoku_potential_values[cell_to_guess][0],cell_to_guess))
        sudoku_potential_values[cell_to_guess].remove(sudoku_potential_values[cell_to_guess][0])

sudoku_solved = sudoku_in_progress
cell_values = [str(value) for key, value in sudoku_solved.items()]
readable_solved_sudoku = [''.join(cell_values[i:i+9]) for i in range(0,81,9)]
print("The solved sudoku looks like this:")
for line in readable_solved_sudoku:
    print(line)
import time
start_time = time.time()
print("It took", round(time.time() - start_time,8), "secondes to run")
