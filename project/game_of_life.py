""" A python script that runs Conway's Game of Life

.. module:: game_of_life.py
    :platform: Windows, Unix
    :synopsis: This program takes the input...

        "Python game_of_life.py" (# of iterations) (cells to start "on")
        ie. python game_of_life.py 50 14:40 15:42 16:39 16:40 16:43 16:44 16:45

        ... all in a list seperated by spaces.  This program is a 0 player game
        which applies a set of rules to determine if cells live or die based on
        their neighbors status and prints the result as a grid.  This process is
        repeated based on the amount of iterations specified.

.. moduleauthor:: Tyler Chapman
        tyler.chapman@wsu.edu

"""
from sys import argv

# Make a function to create a grid
def create_grid(nrows, ncols):
    """ This function creates a grid of nrows and ncols

    The grid starts with the value 0 in every spot in the grid, which specified
    later is considered "off"

    :param nrows: the number of rows
    :type nrows: An integer value

    :param ncols: the number of columns
    :type ncols: An integer value

    :return: a variable containing the grid
    :type: A 2D array

    """

    # Create grid with 0's in all rows and columns
    grid = []
    for i in range (nrows):
        grid.append([0] * ncols)
    return(grid)

# Make a function to print the grid
def print_grid(grid, nrows, ncols):
    """ This function prints out the grid that was created

    This function accesses each value in the grid, and if the value is a 0, it
    converts it to a '-', and if it is not a 0, it converts it to an 'X'.  The
    grid with '-' and 'X' are then printed.

    :param grid: a variable containing the grid
    :type ncols: A 2D array

    :param nrows: the number of rows
    :type nrows: An integer value

    :param ncols: the number of columns
    :type ncols: An integer value

    :return: prints the grid
    :type: A 2D array

    """

    # Change the values in the current grid to '-' if 0 or 'X' if anything else.
    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 0:
                print('-', end = '')
            else:
                print('X', end = '')
        print("\n", end = '')

# Make a function to implement the rules and adjust the grid accordingly
def apply_rules(grid, nrows, ncols):
    """ This function applys the game's rules to the grid

    This function creates a new grid to apply rules to.  The number of live/dead
    cells are counted for each point in the grid, and their values are summed
    as neighbors.  The grid's current status is copied onto the new grid.  Based
    on how many neighbors are "living" vs "dead", the status of that cell in the
    new grid is changed to either 0 or 1.

    :param grid: a variable containing the grid
    :type ncols: A 2D array

    :param nrows: the number of rows
    :type nrows: An integer value

    :param ncols: the number of columns
    :type ncols: An integer value

    :return: A new grid with rules applied
    :type: A 2D array

    """

    #Create a new grid to store changes in
    new_grid = create_grid(nrows, ncols)

    # Count neighbor cells from grid
    for i in range(nrows):
        for j in range(ncols):
            nw = grid[i-1][j-1]
            n = grid[i-1][j]
            w = grid[i][j-1]

            # Else: statements to avoid errors from looking past nrows and ncols
            if j == ncols - 1:
                ne = grid[i-1][j]
            else:
                ne = grid[i-1][j+1]

            if j == ncols - 1:
                e = grid[i][j]
            else:
                e = grid[i][j+1]

            if i == nrows - 1:
                sw = grid[i][j-1]
            else:
                sw = grid[i+1][j-1]

            if i == nrows - 1:
                s = grid[i][j]
            else:
                s = grid[i+1][j]

            # se is based on whether it's at the end of nrows, ncols, or both
            if j == ncols - 1 and i == nrows - 1:
                se = grid[i][j]
            if j == ncols - 1 and i < nrows - 1:
                se = grid[i+1][j]
            if j < ncols - 1 and i == nrows - 1:
                se = grid[i][j+1]
            if j < ncols - 1 and i < nrows - 1:
                se = grid[i+1][j+1]

            # Define neighbors
            neighbors = nw + n + ne + w + sw + s + se + e

            # Set new_grid values = to current grid values
            new_grid[i][j] = grid[i][j]

            # Apply changes to new_grid
            if grid[i][j] == 1:
                if neighbors < 2:
                    new_grid[i][j] = 0
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = 1
                if neighbors > 3:
                    new_grid[i][j] = 0
            if grid[i][j] == 0:
                if neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0

    # Return the new_grid
    return(new_grid)

# Run the program
def main():
    """ This function runs the program

    This function defines n_ticks and the start_cells based on the users
    specification.  It then defines how many rows and columns the grids will
    have and creates the grid with the create_grid function.  It then set the
    starting cells which the user specified, and keeps track of the current
    tick.  Then, the grid is printed with the print_grid function, and the rules
    are applied with the apply_rules function.  The tick counter goes up by one,
    and this repeats until the current tick = the specified number of ticks from
    the user.

    :return: # of grids speficied by user with applied rules each iteration
    :type: A 2D array

    """

    # define n_ticks and start_cells based on the command-line prompts
    n_ticks = argv[1]
    start_cells = argv[2:]

    # Define nrows and ncols, initialize the grid
    nrows = 30
    ncols = 80
    grid = create_grid(nrows, ncols)

    # Set the starting cells specified by the user
    for start_cell in start_cells:
        i, j = start_cell.split(':')
        i = int(i) - 1 # -1 to convert users input to python's 0-based indexing
        j = int(j) - 1 # -1 to convert users input to python's 0-based indexing
        grid[i][j] = 1

    # Initialize current tick as 1
    current_tick = 1

    # Iterate through the steps (ticks)
    while current_tick <= (int(n_ticks) + 1): # +1 because prints initial state

        # Print the grid after rules
        print_grid(grid, nrows, ncols)

        # Apply the rules and save result as grid
        grid = apply_rules(grid, nrows, ncols)

        # Add 1 to current tick
        current_tick += 1

        # Space the grids out
        print("\n")

# Call the main function
if __name__ == "__main__":
    main()
