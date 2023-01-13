def spiral_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])  # number of rows and columns
    visited = [[False for _ in range(cols)]
               for _ in range(rows)]  # visited cells

    # directions for traversal (right, down, left, up)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    current_row, current_col, direction = 0, 0, 0  # starting point and direction

    for _ in range(rows * cols):  # traverse all cells
        print(matrix[current_row][current_col],
              end=' ')  # visit the current cell

        visited[current_row][current_col] = True
        next_row = current_row + dx[direction]
        next_col = current_col + dy[direction]  # check the next cell

        if (0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col]):
            current_row, current_col = next_row, next_col  # move to the next cell
        else:
            # change direction if next cell is invalid
            direction = (direction + 1) % 4
            current_row = current_row + dx[direction]
            current_col = current_col + dy[direction]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def spiralTraversal(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []
    row, col = 0, 0
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_index = 0
    for _ in range(rows * cols):
        result.append(matrix[row][col])
        visited[row][col] = True
        next_row, next_col = row + dirs[dir_index][0], col + dirs[dir_index][1]
        if (next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or visited[next_row][next_col]):
            dir_index = (dir_index + 1) % 4
            next_row = row + dirs[dir_index][0]
            next_col = col + dirs[dir_index][1]
        row, col = next_row, next_col
    return result

print(spiralTraversal(matrix))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
