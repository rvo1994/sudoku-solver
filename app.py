from flask import Flask, render_template, request, flash
from sudoku_solver.sudoku import sudoku_solver

app = Flask(__name__)

empty_grid = [['' for i in range(9)] for i in range(9)]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        message1 = "Enter known numbers:"
        return render_template('form.html', grid=empty_grid, message=message1)
    elif request.method == 'POST':
        grid = []
        for i in range(1,82):
            if request.form[str(i)] == '':
                grid.append(0)
            else:
                grid.append(int(request.form[str(i)]))
        grid = [grid[i:i+9] for i in range(0,81,9)]
        if sudoku_solver(grid) == False:
            message2 = "Please enter a valid grid!"
            color1 = "pred"
            return render_template('form.html', grid=empty_grid, message=message2, color=color1)
        solved_grid = sudoku_solver(grid)
        message3 = "Sudoku solved!"
        color2 = "pgreen"
        return render_template('form.html', grid=solved_grid, message=message3, color=color2)

if __name__ == "__main__":
    app.run(debug=True)
