from sys import argv

# I could improve my sudoku resolver by
# using a list of possibilities for the
# current number and use different checks
# to find the answer

LIST_OF_9_FIRST_NUMBERS = [1, 2 , 3, 4, 5, 6, 7, 8, 9]

def sudoku(grid):
    """
        Take a simple sudoku and
        Return the sudoku done
    """
    grid = format_input(grid)

    while True:
        still_to_find = False
        for ordonate ,line in enumerate(grid):
            for abscisse ,element in enumerate(line):
                if element != '_':
                    continue
                coord = (abscisse, ordonate)
                if check(grid, coord):
                    still_to_find = True

        if not still_to_find:
            break

    return grid

def format_input(grid):
    """
        Take the txt file and return
        a table of the number in the sudoku
    """
    f = open(grid, 'r')
    res = []

    for line_num, line in enumerate(f):
        if line_num == 3 or line_num == 7:
            continue
        # removing the '|' character in the string
        line = line[:3] + line[4:7] + line[8:11]
        list_line = []
        for char in line:
            if char != "_":
                list_line.append(int(char))
            else:
                list_line.append(char)
        res.append(list_line)
    f.close()

    return res

def check(grid, coord):
    """
        Take a sudoku grid and the element to test
        Return the solution
    """
    line_values = grid[coord[1]]
    isResolve, solution = check_values(line_values)

    if isResolve:
        grid[coord[1]][coord[0]] = solution
        return False

    column_values = []

    for line in grid:
        column_values.append(line[coord[0]])
    isResolve, solution = check_values(column_values)

    if isResolve:
        grid[coord[1]][coord[0]] = solution
        return False

    square_values = []

    # This rule is true for the row and the column
    square_abscissa_values = []
    square_ordonees_values = []

    # Define the abs in the square
    if coord[1] % 3 == 0:
        square_abscissa_values = [coord[1], coord[1] + 1, coord[1] + 2]
    elif coord[1] % 3 == 1:
        square_abscissa_values = [coord[1] - 1, coord[1], coord[1] + 1]
    else:
        square_abscissa_values = [coord[1] - 2, coord[1] - 1, coord[1]]

    # Define the ord in the square
    if coord[0] % 3 == 0:
        square_abscissa_values = [coord[0], coord[0] + 1, coord[0] + 2]
    elif coord[0] % 3 == 1:
        square_abscissa_values = [coord[0] - 1, coord[0], coord[0] + 1]
    else:
        square_abscissa_values = [coord[0] - 2, coord[0] - 1, coord[0]]

    for abss in square_abscissa_values:
        for ords in square_ordonees_values:
            square_values.append(grid[ords][abss])

    isResolve, solution = check_values(square_values)
    if isResolve:
        grid[coord[1]][coord[0]] = solution
        return False

    return True

def check_values(line):
    """
        Take a line of the sudoku and
        Return the completed line
    """
    test_values = [i for i in range(1, 10)]

    for element in line:
        if element != '_':
            test_values.remove(element)
    if len(test_values) == 1:
        return True, test_values[0]
    return False, None

print(sudoku(argv[1]))
