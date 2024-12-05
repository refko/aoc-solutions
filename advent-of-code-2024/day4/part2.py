grid = []
total = 0
grid_cols_length = 0
grid_rows_length = 0

def out_of_bounds(row, col):
    return not (0 <= row < grid_rows_length) or not (0 <= col < grid_cols_length)

def check_top_left_to_bottom_right(row, col):
    string = grid[row-1][col-1] + "A" + grid[row+1][col+1]
    return string == "MAS" or string == "SAM"
    
def check_top_right_to_bottom_left(row, col):
    string = grid[row-1][col+1] + "A" + grid[row+1][col-1]
    return string == "MAS" or string == "SAM"

def check_if_x_mas(row, col):
    global total
    
    if not out_of_bounds(row-1, col-1) and not out_of_bounds(row+1, col+1) and not out_of_bounds(row-1, col+1) and not out_of_bounds(row+1, col-1):
        if check_top_left_to_bottom_right(row, col) and check_top_right_to_bottom_left(row, col):
            total+=1
    
with open("input.txt", "r") as input_file:
    grid = input_file.read().split("\n")
    
grid_rows_length = len(grid[0:])
grid_cols_length = len(grid[0][0:])

for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):
        if col == "A":
            check_if_x_mas(row_index, col_index)
            
print(total)