from day_5_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/5

######################################################

data = input_data.input

data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

######################################################

## Parsing the input

# This separates the pages from the updates and separates the pages and updates into lists with one entry each
split_data = data.split("\n\n") 
unsanitised_pages = split_data[0]
unsanitised_updates = split_data[1]

string_pages = unsanitised_pages.split("\n")
string_updates = unsanitised_updates.split("\n")

# Turns the list of strings into actual lists
updates = []
for update in string_updates:
    temp_list = []
    temp_list_str = update.split(",")
    
    for i in temp_list_str:
        temp_list.append(int(i))
    updates.append(temp_list)

pages = []
for page in string_pages:
    temp_list = []
    temp_list_str = page.split("|")

    for i in temp_list_str:
        temp_list.append(int(i))

    pages.append(temp_list)
    
######################################################

## Ideas
# Build a function to create one big list of all pages in their required order
# Build a function that will take this big list and then check each update and ensure they are in the appropriate order

# Each number should only be entered once so you can always find the index right?
# function for big list
def list_sorter(input):
    final_list = []

    for i in input:
        pass

#for page in pages:
#    print(page)

