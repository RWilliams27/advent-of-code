from day_6_input_data import input_data
import logging, time

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

print("")
rows = data.split("\n")

# Declares 2d array
grid = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]

directions = {
    "up": (-1, 0),
    "down": (+1, 0),
    "right": (0, +1),
    "left": (0, -1)
}
curr_dir = None
# Translates input map into a 2d array
for row_index, row in enumerate(rows):
    obstacles = []
    player = 0
    for index, item in enumerate(row):
        if item == "#":
            grid[row_index][index] = 1
        if item == "^": #This wont check direction yet
            grid[row_index][index] = 2
            curr_dir = directions["up"]
            print(curr_dir)

print("----------------------------")
for row in grid:
    print(row)
print("----------------------------")

def move(start_pos: tuple = None):
    print(f"Current Dir: {curr_dir}")
    player_row, player_column = curr_dir
    for row_index, row in enumerate(grid):

        for column_index, item in enumerate(row):
            if item == 2:
                print(f"row: {row_index + player_row}   |   column: {column_index + player_column}")

                if grid[row_index + player_row][column_index + player_column] == 1:
                    curr_dir = directions["right"]

                if row_index + player_row < len(grid) and row_index + player_row >= 0 and column_index + player_column < len(row) and column_index + player_column >= 0: #Doesnt care if there is a 1 in the way but does go all the way up now
                    print("HIT")
                    grid[row_index][column_index] = 0
                    grid[row_index + player_row][column_index + player_column] = 2

                    

                else:
                    return False
                
    print("----------------------------")
    for row in grid:
        print(row)
    print("----------------------------")

    time.sleep(2)
    return True


    


edge_hit = True

while edge_hit:
    edge_hit = move()

print("----------------------------")
for row in grid:
    print(row)
print("----------------------------")
