from day_5_input_data import input_data
import logging

## Challenge URL: https://adventofcode.com/2024/day/5

logging.basicConfig(
    filename="Day_5_Challenge_1.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M",
    level=logging.DEBUG,
)

######################################################

data = input_data.input

## Parsing the input

# This separates the pages from the updates and separates the pages and updates into lists with one entry each
split_data = data.strip().split("\n\n") 
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
        temp_list.append(i)

    pages.append(temp_list)

for page in pages:
    print(page)

#########

def rule_check(update):
    id = {}

    for index, value in enumerate(update):
        id[value] = index

    for page in pages:
        for a, b in page:
            if a in id and b in id and not id[a] < id[b]:
                return False
            
            
    return True


valid_update = []
invalid_update = []
final_count = 0

for update in updates:
    if rule_check(update):
        mid = len(update) // 2

        final_count += mid

print(final_count)
