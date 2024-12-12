from day_6_input_data import input_data
import logging, time
from typing import Union

## Challenge URL: https://adventofcode.com/2024/day/6

logging.basicConfig(
    filename="Day_6_Challenge_1.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M",
    level=logging.DEBUG,
)


######################################################

data = input_data.input

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

logging.debug("")
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
            logging.debug(directions[current_direction])

logging.debug("----------------------------")
for row in grid:
    logging.debug(row)
logging.debug("----------------------------")

def move(move_direction, direction):
    if move_direction + direction >= len(directions):
        move_direction = 0
        return move_direction
    
    elif direction == 0:
        logging.debug(f"Move Direction: {move_direction}")
        return move_direction
    
    elif direction >= 1:
        logging.debug(f"Move Direction: {move_direction}")
        return move_direction + 1

def main(curr_dir: int, grid = grid):
    running = True
    previous_grid = grid
    player_row, player_column = directions[curr_dir]
    logging.debug(f"Current Dir: {directions[curr_dir]}")
            
    logging.debug("-----------------------------")
    for row in grid:
        logging.debug(row)
    logging.debug("-----------------------------")  
    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            if item == 2:
                if row_index + player_row < len(grid) and row_index + player_row >= 0 and column_index + player_column < len(row) and column_index + player_column >= 0: 
                    if grid[row_index + player_row][column_index + player_column] == 1:
                        logging.debug(f"Player Row: {player_row}    |   Player Column: {player_column}")
                        curr_dir = move(curr_dir, 1)           
                        logging.debug("HIT 2")   
                        return curr_dir, grid, running        
                    else: 
                        logging.debug(f"Player Row: {player_row}    |   Player Column: {player_column}")
                        previous_grid[row_index][column_index] = 3
                        previous_grid[row_index + player_row][column_index + player_column] = 2

                        logging.debug("HIT 3")
                        return curr_dir, grid, running

                else:
                    logging.debug("HIT 4")
                    running = False
                    return curr_dir, grid, running

    grid = previous_grid 

    logging.debug(f"Row Index + Player Row: {row_index + player_row}   |   Column Index + Player Column: {column_index + player_column}")  
    return curr_dir, grid, running


def final_path_count(grid: list, final_count: int):
    for row_index, row in enumerate(grid):
        for column_index, column in enumerate(row):
            if grid[row_index][column_index] == 3:
                final_count += 1
    
    return final_count






    
move_count = 0
running = True
i = 0
while running:
    current_direction, grid, running = main(current_direction)
    i += 1

final_count = 1
final_count = final_path_count(grid, final_count)

logging.debug("----------------------------")
for row in grid:
    logging.debug(row)
logging.debug("----------------------------")

logging.debug(f"Move Count: {move_count}")

logging.debug(f"Final Count: {final_count}")