#More Testing

from day_4_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/4

#######################################################

data = input_data.input

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


schema_dict = {
    "vertical": {
        "upwards":[0, 0, 0, 0],
        "downwards": [0, 0, 0, 0]
        },
    "diagonal": {
        "left": [0, -1, -2, -3],
        "right": [0, 1, 2, 3]
    },
    "letters": {
        "normal": ["X", "M", "A", "S"],
        "reverse": ["S", "A", "M", "X"]
    }
}

def wordsearch(direction, letter_order): # Will also need to add the dict I want appended to 
    wordCount = 0
    row_index = 0
    for row in grid:
        column_index = 0
        for i in row:
            if i == letter_order[0]:

                if row_index + 1 < len(grid) and column_index + direction[1] < len(row) and column_index + direction[1] >= 0:
                    if grid[row_index + 1][column_index + direction[1]] == letter_order[1]:

                        if row_index + 2 < len(grid) and column_index + direction[2] < len(row) and column_index + direction[2] >= 0:
                            if grid[row_index + 2][column_index + direction[2]] == letter_order[2]:

                                if row_index + 3 < len(grid) and column_index + direction[3] < len(row) and column_index + direction[3] >= 0:
                                    if grid[row_index + 3][column_index + direction[3]] == letter_order[3]:
                                        #print("----------------------")
                                        #print(f"ROW INDEX: {row_index}   |   {row}")
                                        #print(f"ROW INDEX: {row_index + 1}   |   {grid[row_index + 1]}")
                                        #print(f"ROW INDEX: {row_index + 2}   |   {grid[row_index + 2]}")
                                        #print(f"ROW INDEX: {row_index + 3}   |   {grid[row_index + 3]}")
                                        #print("----------------------")  
                                        wordCount += 1

            column_index += 1

        row_index += 1
    
    return wordCount

downwards_count = wordsearch(schema_dict["vertical"]["downwards"], schema_dict["letters"]["normal"])
upwards_count = wordsearch(schema_dict["vertical"]["upwards"], schema_dict["letters"]["reverse"])

diagonal_left = 0
diagonal_right = 0
diagonal_left += wordsearch(schema_dict["diagonal"]["left"], schema_dict["letters"]["normal"])
diagonal_left += wordsearch(schema_dict["diagonal"]["left"], schema_dict["letters"]["reverse"])

diagonal_right += wordsearch(schema_dict["diagonal"]["right"], schema_dict["letters"]["normal"])
diagonal_right += wordsearch(schema_dict["diagonal"]["right"], schema_dict["letters"]["reverse"])


print(f"horizontal_count: {horizontal_count}")
print(f"backwards_count: {backwards_count}") 
print(f"upwards_count: {upwards_count}")    
print(f"downwards_count: {downwards_count}") 
print(f"diagonal_left: {diagonal_left}") 
print(f"diagonal_right: {diagonal_right}") 

print(f"Final Count: {horizontal_count + backwards_count + upwards_count + downwards_count + diagonal_left + diagonal_right}")