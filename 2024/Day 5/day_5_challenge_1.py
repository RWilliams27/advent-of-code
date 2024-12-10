from day_5_input_data import input_data
from collections import defaultdict

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
        #temp_list.append(int(i))
        temp_list.append(i)

    pages.append(temp_list)

######################################################

## Ideas
# Build a function to create one big list of all pages in their required order
# Build a function that will take this big list and then check each update and ensure they are in the appropriate order

## ORRR topological nested dictionary 

# Each number should only be entered once so you can always find the index right?
# function for big list

parsed_dict = {}

print(pages)

def dict_maker(input):
    
    for i in input:
        if i[0] not in parsed_dict:
            parsed_dict[i[0]] = []

        parsed_dict[i[0]].append(i[1])



dict_maker(pages)
print(parsed_dict)


temp_dict = {}

for key, value in parsed_dict.items():
    print(f"Key: {key}, Value: {value}")
    for number in value:
        if number not in parsed_dict.keys():
            temp_dict[number] = []

parsed_dict.update(temp_dict)

print(parsed_dict)

def kahn(nodes: dict):
    # Heavily relied on source from https://dev.to/leopfeiffer/topological-sort-with-kahns-algorithm-3dl1
    queue = []
    indegrees = {k: 0 for k in nodes.keys()}

    # Calculate the indegree for each node
    for name, edges in nodes.items():
        for edge in edges:
            indegrees[edge] += 1

    for node in nodes.keys():
        if indegrees[node] == 0:
            queue.append(node)

    print(f"queue: {queue}")

    topological_order = []

    while len(queue) > 0:
        current_node = queue.pop(0)

        topological_order.append(current_node)

        for edge in nodes[current_node]:
            indegrees[edge] -= 1

            if indegrees[edge] == 0:
                queue.append(edge)

    if len(topological_order) != len(nodes):
        print("Circular Path Found")

    return topological_order

print(kahn(parsed_dict))