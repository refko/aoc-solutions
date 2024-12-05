grid = []
total = 0
word = "XMAS"
current_word = ""
grid_cols_length = 0
grid_rows_length = 0

def out_of_bounds(row, col):
    return not (0 <= row < grid_rows_length) or not (0 <= col < grid_cols_length)

def check_e(row, col):
    global total
    xmas = ""
    for i in range(4):
        if not out_of_bounds(row, col+i):
            xmas += grid[row][col+i]
        else: break
        if i == 3:
            if xmas == word:
                print("found to the right of %s, %s" % (row, col))
                total+=1
            break
        

def check_w(row, col):
    global total
    xmas = ""
    for i in range(4):
        if not out_of_bounds(row, col-i):
            xmas += grid[row][col-i]
        else: break
        if i == 3:
            if xmas == word:
                print("found to the left of %s, %s" % (row, col))
                total+=1
            break

def check_n(row, col):
    global total
    xmas = ""
    for i in range(4):
        if not out_of_bounds(row-i, col):
            xmas += grid[row-i][col]
        else: break
        if i == 3:
            if xmas == word:
                print("found to the north of %s, %s" % (row, col))
                total+=1
            break
            
def check_s(row, col):
    global total
    xmas = ""
    for i in range(4):
        if not out_of_bounds(row+i, col):
            xmas += grid[row+i][col]
        else: break
        if i == 3:
            if xmas == word:
                print("found to the south of %s, %s" % (row, col))
                total+=1
            break

def check_ne(row, col, word_index=0):
    global total
    global current_word
    if word_index == 4:
        if current_word == word:
            print("found ne of %s, %s" % (row-4, col-4))
            total+=1
        current_word = ""
        return
    if out_of_bounds(row, col):
        current_word = ""
        return
    current_word += grid[row][col]
    check_ne(row-1, col+1, word_index+1)

def check_nw(row, col, word_index=0):
    global total
    global current_word
    if word_index == 4:
        if current_word == word:
            print("found nw of %s, %s" % (row-4, col-4))
            total+=1
        current_word = ""
        return
    if out_of_bounds(row, col):
        current_word = ""
        return
    current_word += grid[row][col]
    check_nw(row-1, col-1, word_index+1)
        
def check_se(row, col, word_index=0):
    global total
    global current_word
    if word_index == 4:
        if current_word == word:
            print("found se of %s, %s" % (row-4, col-4))
            total+=1
        current_word = ""
        return
    if out_of_bounds(row, col):
        current_word = ""
        return
    current_word += grid[row][col]
    check_se(row+1, col+1, word_index+1)

def check_sw(row, col, word_index=0):
    global total
    global current_word
    if word_index == 4:
        if current_word == word:
            print("found sw of %s, %s" % (row-4, col-4))
            total+=1
        current_word = ""
        return
    if out_of_bounds(row, col):
        current_word = ""
        return
    current_word += grid[row][col]
    check_sw(row+1, col-1, word_index+1)

def check_all_directions(row, col):
    check_e(row, col)
    check_w(row, col)
    check_n(row, col)
    check_s(row, col)
    check_ne(row, col)
    check_se(row, col)
    check_nw(row, col)
    check_sw(row, col)
    
with open("input.txt", "r") as input_file:
    grid = input_file.read().split("\n")
    
grid_rows_length = len(grid[0:])
grid_cols_length = len(grid[0][0:])

for row_index, row in enumerate(grid):
    for col_index, _ in enumerate(row):
        check_all_directions(row_index, col_index)
print(total)
