from day_1_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/1#part2

#######################################################

## Turning the input data into the two required lists

data = input_data.input

no_new_lines = data.replace("\n", "   ")
input_list = no_new_lines.rsplit("   ")

list_a = []
list_b = []

i = 0
for item in input_list:
    i += 1

    if (i % 2) != 0:
        list_a.append(item)
        print(f"Number: {item} was added to List A")
    else:
        list_b.append(item)
        print(f"Number: {item} was added to List B")

#######################################################

## Doing the count maths to get the score for each item in list_a
score = []

for item in list_a:
    item_score = list_b.count(item)
    if item_score != 0:
        score.append(item * item_score)


#######################################################