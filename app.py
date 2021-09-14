from flask import Flask, render_template, request
from sudoku_solver.sudoku import sudoku_solver

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontend():
    if request.method == 'GET':
        print('Hello World!')        
    return render_template('content.html')

@app.route('/background_process_test', methods=['GET', 'POST'])
def background_process_test():
        solver('sudoku_solver/data/sudoku4.txt')
        return ("nothing")
    
@app.route('/test', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        grid = []
        for i in range(1,82):
            if request.form[str(i)] == '':
                grid.append(0)
            else:
                grid.append(int(request.form[str(i)]))
        grid = [grid[i:i+9] for i in range(0,81,9)]
        print(sudoku_solver(grid))
        return render_template('content.html')

if __name__ == "__main__":
    app.run(debug=True)
