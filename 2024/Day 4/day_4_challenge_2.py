from day_4_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/4#part2

#######################################################

data = input_data.input

#data = """MMMSXXMASM
#MSAMXMSMSA
#AMXSXMAAMM
#MSAMASMSMX
#XMASAMXAMM
#XXAMMXXAMA
#SMSMSASXSS
#SAXAMASAAA
#MAMMMXMMMM
#MXMXAXMASX"""

## Turning the data into a 2d array (grid) to visualise
no_new_lines = [row.strip() for row in data.split("\n")]

grid = [[0 for i in range(len(no_new_lines[0]))] for j in range(len(no_new_lines))]

row_iterate = 0
while row_iterate < len(grid):
    column_iterate = 0

    while column_iterate < len(grid[0]):
        grid[row_iterate][column_iterate] = no_new_lines[row_iterate][column_iterate]

        column_iterate += 1
    row_iterate += 1

## Ideas
# Look for "A"'s and then check the diagonal figures for the "S"'s and "M"'s
# Nest the ifs 

## Angles
# Top-Left
# Bottom-Left
# Top-Right
# Bottom-Right

def gridCheck(direction, letter, row_index, column_index, row):

    if direction == "Top-Left":
        if row_index - 1 < len(grid) and row_index - 1 >= 0 and column_index - 1 < len(row) and column_index - 1 >= 0:
                if grid[row_index - 1][column_index - 1] == letter:
                    return True
                    
    elif direction == "Top-Right":
        if row_index - 1 < len(grid) and row_index - 1 >= 0 and column_index + 1 < len(row) and column_index + 1 >= 0:
                if grid[row_index - 1][column_index + 1] == letter:
                    return True
                
    elif direction == "Bottom-Left":
        if row_index + 1 < len(grid) and row_index + 1 >= 0 and column_index - 1 < len(row) and column_index - 1 >= 0:
            if grid[row_index + 1][column_index - 1] == letter:
                return True
            
    elif direction == "Bottom-Right":
        if row_index + 1 < len(grid) and row_index + 1 >= 0 and column_index + 1 < len(row) and column_index + 1 >= 0:
            if grid[row_index + 1][column_index + 1] == letter:
                return True
    
    else:
        return False

def mas_wordsearch():
    word_count = 0
    row_index = 0

    for row in grid:
        column_index = 0
        for i in row:
            if i == "A":

                # Top left S
                if gridCheck("Top-Left", "S", row_index, column_index, row):

                    if gridCheck("Bottom-Right", "M", row_index, column_index, row):

                        if gridCheck("Top-Right", "S", row_index, column_index, row):

                            if gridCheck("Bottom-Left", "M", row_index, column_index, row):
                                word_count += 1

                        elif gridCheck("Top-Right", "M", row_index, column_index, row):

                            if gridCheck("Bottom-Left", "S", row_index, column_index, row):
                                word_count += 1

                # Top left M

                elif gridCheck("Top-Left", "M", row_index, column_index, row):

                    if gridCheck("Bottom-Right", "S", row_index, column_index, row):

                        if gridCheck("Top-Right", "M", row_index, column_index, row):

                            if gridCheck("Bottom-Left", "S", row_index, column_index, row):
                                word_count += 1

                        elif gridCheck("Top-Right", "S", row_index, column_index, row):

                            if gridCheck("Bottom-Left", "M", row_index, column_index, row):
                                word_count += 1

            column_index += 1

        row_index += 1

    return word_count

words = mas_wordsearch()

print(f"Word Count: {words}")
