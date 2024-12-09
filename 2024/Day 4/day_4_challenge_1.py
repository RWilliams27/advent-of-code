from day_4_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/4

#######################################################

data = input_data.input
# Example data
data = """MMMSXXMASM 
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""



## Ideas
# Maybe it into a nested array with each line being an array to essentially create a grid?
# What if I check for each kind of xmas individually and then add up the final count? (IE: horizontal, then downwards, then upwards, then backwards, then diagonal)
## How do I achieve that?
# Backwards and forwards are easy, just do count() for them
# Downwards and upwards, I think the best method will be to do a detection for either "x" or "s" and then check the same index in each array and confirm if the word exists by checking for each letter
# Diagonal, I will need to check the previous and next index in each array and confirm if the word exists by checking for each letter

## Turning the data into a 2d array (grid) to visualise
no_new_lines = [row.strip() for row in data.split("\n")]

print(no_new_lines)

grid = [[0 for i in range(len(no_new_lines[0]))] for j in range(len(no_new_lines))]

for row in grid:
    print(row)

row_iterate = 0
while row_iterate < len(grid):
    column_iterate = 0

    while column_iterate < len(grid[0]):
        grid[row_iterate][column_iterate] = no_new_lines[row_iterate][column_iterate]

        column_iterate += 1
    row_iterate += 1
 
for i in grid:
    print(i)


horizontal_count = 0
backwards_count = 0

for row in grid:
    row_str = ""

    for i in row:
        row_str = row_str + i

    horizontal_count += row_str.count("XMAS")
    backwards_count += row_str.count("SAMX")

    print(f"Row String: {row_str}")


# Look for x's

#Downwards
downwards_count = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "X":
            
            if row_index + 1 < len(grid):
                if grid[row_index + 1][column_index] == "M":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index + 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid):
                        if grid[row_index + 2][column_index] == "A":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index + 1])
                            #print(grid[row_index + 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid):
                               if grid[row_index + 3][column_index] == "S":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   downwards_count += 1

        column_index += 1

    row_index += 1
        
#Upwards
upwards_count = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "S":           
            if row_index + 1 < len(grid):
                if grid[row_index + 1][column_index] == "A":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index + 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid):
                        if grid[row_index + 2][column_index] == "M":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index + 1])
                            #print(grid[row_index + 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid):
                               if grid[row_index + 3][column_index] == "X":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   upwards_count += 1
        column_index += 1

    row_index += 1

debug_1 = 0

# Diaganol Time right, downwards
diagonal_count = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "X":
            
            if row_index + 1 < len(grid) and column_index + 1 < len(row):
                if grid[row_index + 1][column_index + 1] == "M":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index + 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid) and column_index + 2 < len(row):
                        if grid[row_index + 2][column_index + 2] == "A":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index + 1])
                            #print(grid[row_index + 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid) and column_index + 3 < len(row):
                               if grid[row_index + 3][column_index + 3] == "S":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   diagonal_count += 1
                                   debug_1 += 1

        column_index += 1

    row_index += 1

# Diaganol Time right, upwards
debug_2 = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "S":
            
            if row_index + 1 < len(grid) and column_index + 1 < len(row):
                if grid[row_index + 1][column_index + 1] == "A":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index + 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid) and column_index + 2 < len(row):
                        if grid[row_index + 2][column_index + 2] == "M":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index + 1])
                            #print(grid[row_index + 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid) and column_index + 3 < len(row):
                               if grid[row_index + 3][column_index + 3] == "X":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   diagonal_count += 1
                                   debug_2 += 1

        column_index += 1

    row_index += 1

# Diaganol Time left, downwards
debug_3 = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "X":
            
            if row_index + 1 < len(grid) and column_index - 1 < len(row):
                if grid[row_index - 1][column_index - 1] == "M":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index - 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid) and column_index - 2 < len(row):
                        if grid[row_index - 2][column_index - 2] == "A":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index - 1])
                            #print(grid[row_index - 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid) and column_index - 3 < len(row):
                               if grid[row_index - 3][column_index - 3] == "S":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   diagonal_count += 1
                                   debug_3 += 1

        column_index += 1

    row_index += 1


# Diaganol Time left, upwards
debug_4 = 0
row_index = 0
for row in grid:
    column_index = 0
    for i in row:
        if i == "S":
            
            if row_index + 1 < len(grid) and column_index - 1 < len(row):
                if grid[row_index - 1][column_index - 1] == "A":
                    #print("----------------------")
                    #print(row)
                    #print(grid[row_index - 1])
                    #print("----------------------")

                    if row_index + 2 < len(grid) and column_index - 2 < len(row):
                        if grid[row_index - 2][column_index - 2] == "M":
                            #print("----------------------")
                            #print(row)
                            #print(grid[row_index - 1])
                            #print(grid[row_index - 2])
                            #print("----------------------")

                            if row_index + 3 < len(grid) and column_index - 3 < len(row):
                               if grid[row_index - 3][column_index - 3] == "X":
                                   print("----------------------")
                                   print(row)
                                   print(grid[row_index + 1])
                                   print(grid[row_index + 2])
                                   print(grid[row_index + 3])
                                   print("----------------------")
                                   diagonal_count += 1
                                   debug_4 += 1

        column_index += 1

    row_index += 1



print(f"horizontal_count: {horizontal_count}") # Correct for example
print(f"backwards_count: {backwards_count}") # Correct for example
print(f"upwards_count: {upwards_count}")    # Correct for example
print(f"downwards_count: {downwards_count}") # Correct for example
print(f"diagonal_count: {diagonal_count}  |   Expected number: 10")

print(f"Final Count: {horizontal_count + backwards_count + upwards_count + downwards_count + diagonal_count}")


print(f"DEBUG_1: {debug_1}")
print(f"DEBUG_2: {debug_2}")
print(f"DEBUG_3: {debug_3}")
print(f"DEBUG_4: {debug_4}") ## ISSUE IS WITH THE FINAL FUNCTION | LEFT-UPWARDS