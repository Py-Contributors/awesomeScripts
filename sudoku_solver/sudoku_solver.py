# The size of our sudoku
MAX_SIZE = 9

# Defining our sudoku where 0 represents empty cell
# else it is not empty

sudoku = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 0, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 0, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 0, 4, 7, 2, 0, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 0, 8, 6, 3, 1, 0],
]

# another example
# sudoku = [
#     [6,5,0,8,7,3,0,9,0],
#     [0,0,3,2,5,0,0,0,8],
#     [9,8,0,1,0,4,3,5,7],
#     [1,0,5,0,0,0,0,0,0],
#     [4,0,0,0,0,0,0,0,2],
#     [0,0,0,0,0,0,5,0,3],
#     [5,7,8,3,0,1,0,2,6],
#     [2,0,0,0,4,8,9,0,0],
#     [0,9,0,6,2,5,0,8,1]
# ]


# Basically this function is used to check if the
# given cell is unassigned or not.
# Else if it is not then we do not have to change it.
# For the same reason we have passed -1.
def if_unassigned(row, col):
    num_unassign = 0
    for i in range(0, MAX_SIZE):
        for j in range(0, MAX_SIZE):
            if sudoku[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a


# This function is used to check if the value which we have passes
# Satisfies all the conditions or not
# If the conditions are not satisfied we return False else True
# Here we check the conditions in all cases i.e in each row, in each column,
# in each sub 3x3 matrix


def check_safe(n, r, c):
    # row check
    for i in range(0, MAX_SIZE):
        if sudoku[r][i] == n:
            return False

    # column check
    for i in range(0, MAX_SIZE):
        if sudoku[i][c] == n:
            return False
    start_row = (r // 3) * 3
    start_column = (c // 3) * 3

    # sub-matrix check
    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            if sudoku[i][j] == n:
                return False

    return True


# Basically this function is used to check for every value from 1-9
# which is the possible value for an un-assigned cell
def main_func():
    row = 0
    col = 0
    # To check if it is un-assigned or not
    a = if_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1, 10):
        if check_safe(i, row, col):
            sudoku[row][col] = i
            # backtracking step
            if main_func():
                return True
            sudoku[row][col] = 0
    return False


# function to print sudoku
def print_sudoku():
    for i in sudoku:
        print(*i)


if main_func():
    print("The answer for the sudoku is ")
    print_sudoku()
else:
    print("No solution")
