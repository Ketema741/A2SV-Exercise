def zigzag_traverse(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        if i % 2 == 0:  # even rows
            for j in range(n):
                print(grid[i][j], end=' ')
        else:  # odd rows
            for j in range(n-1, -1, -1):
                print(grid[i][j], end=' ')


"""
    Here the function takes grid as input.
    
    The outer for loop is used to iterate through the rows of the grid, and 
    the inner for loop is used to iterate through the columns of each row. 
    
    The if-else statement checks whether the current row index is even or odd, and 
    based on this, it determines the direction of the zigzag traverse.
"""
