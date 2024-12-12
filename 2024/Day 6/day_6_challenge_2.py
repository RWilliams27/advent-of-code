from day_6_input_data import input_data
import logging, time, copy

## Challenge URL: https://adventofcode.com/2024/day/6#part2

logging.basicConfig(
    filename="Day_6_Challenge_2.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M",
    level=logging.DEBUG,
)

start = time.time()
######################################################

#data = input_data.input

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

#logging.debug("")
rows = data.split("\n")

# Declares 2d array
grid = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]

#"up": (-1, 0)
#"down": (+1, 0)
#"right": (0, +1)
#"left": (0, -1)

directions = [(-1, 0), (0, +1), (+1, 0),  (0, -1)]

current_direction = 0
# Translates input map into a 2d array
for row_index, row in enumerate(rows):
    obstacles = []
    player = 0
    for index, item in enumerate(row):
        if item == "#":
            grid[row_index][index] = 1
        if item == "^": #Hardcoded to start as up
            grid[row_index][index] = 2
            #logging.debug(directions[current_direction])

#logging.debug("----------------------------")
for row in grid:
    #logging.debug(row)
    pass
#logging.debug("----------------------------")

def move(move_direction, direction):
    if move_direction + direction >= len(directions):
        move_direction = 0
        return move_direction
    
    elif direction == 0:
        #logging.debug(f"Move Direction: {move_direction}")
        return move_direction
    
    elif direction >= 1:
        #logging.debug(f"Move Direction: {move_direction}")
        return move_direction + 1

def main(curr_dir: int, grid, checked = None):

    max_check = 200 #len(grid) * len(grid[0])
    running = True
    previous_grid = grid
    player_row, player_column = directions[curr_dir]
    exit_found = False

    while checked <= max_check:
        for row_index, row in enumerate(grid):
            for column_index, item in enumerate(row):
                checked += 1
                print(f"Checked: {checked}")
                if item == 2:
                    if row_index + player_row < len(grid) and row_index + player_row >= 0 and column_index + player_column < len(row) and column_index + player_column >= 0: 
                        if grid[row_index + player_row][column_index + player_column] == 1 or grid[row_index + player_row][column_index + player_column] == 4:
                            curr_dir = move(curr_dir, 1)         
                            return curr_dir, grid, running, exit_found, checked        
                        else: 
                            previous_grid[row_index][column_index] = 3
                            previous_grid[row_index + player_row][column_index + player_column] = 2
                            return curr_dir, grid, running, exit_found, checked  

                    else:
                        running = False
                        exit_found = True
                        return curr_dir, grid, running, exit_found, checked  

        grid = previous_grid 

        return curr_dir, grid, running, exit_found, checked   
    else:
        running = False
        return curr_dir, grid, running, exit_found, checked   


def grid_maker(og_grid): # Makes copies of the grid, each copy having the obstacle in a different place
    new_grid = []
    template_grid = copy.deepcopy(og_grid)
    
    for row_index, row in enumerate(og_grid):
        for column_index, column in enumerate(row):  
            if og_grid[row_index][column_index] == 1 or og_grid[row_index][column_index] == 2:
                continue        
            temp_grid = copy.deepcopy(template_grid)
            temp_grid[row_index][column_index] = 4
            new_grid.append(temp_grid)
            
    return new_grid

def final_path_count(grid: list, final_count: int):
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if grid[row_index][column_index] == 3:
                final_count += 1
    
    return final_count    

new_grid = grid_maker(grid)

for grid in new_grid:
    logging.debug("-------------------------FINAL GRID----------------------")
    for row in grid:
        logging.debug(row)
    logging.debug("-------------------------FINAL GRID----------------------")


print(f"New Grid Length: {len(new_grid)}")

i = 0
loops = 0

while i < len(new_grid):
    

    i += 1

print(f"Loops is: {loops}")


for grid in new_grid:
    logging.debug("-------------------------FINAL OTHER GRID----------------------")
    for row in grid:
        logging.debug(row)
    logging.debug("-------------------------FINAL OTHER GRID----------------------")