correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]


def check_sudoku_list(sudoku_list):
    size = len(sudoku_list)
    is_valid = True
    for i in range(1,size + 1):  # since valid sudoku digits start with 1, not 0, make
                                 # adjustment in range statement for better clarity, at 
                                 # least for me when stepping through this in the debugger. 
        if (i) not in sudoku_list:
            is_valid = False
    return is_valid

def check_sudoku(grid):
    # A shortcut: we only have to verify that each of the required 1..N integers
    # is in a particular row or column.  No need to explicitly check for dupes, if there's a 
    # dupe then one of the required integers isn't going to be in the row or column.
    
    # check rows
    for row in grid:
        if not check_sudoku_list(row):
            return False           
    # check columns. Generate 1 column at a time as list and pass to check_list()
    num_columns = len(grid[0])
    for i in range(0,num_columns):
        column = []
        for row in grid:
           column.append(row[i])
    return check_sudoku_list(column)

print check_sudoku(correct)
print check_sudoku(incorrect) 
print check_sudoku(incorrect3) 
print check_sudoku(incorrect4) 


