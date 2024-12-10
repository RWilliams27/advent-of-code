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

#data = """47|53
#97|13
#97|61
#97|47
#75|29
#61|13
#75|53
#29|13
#97|29
#53|29
#61|53
#97|53
#61|29
#47|13
#75|47
#97|75
#47|61
#75|61
#47|29
#75|13
#53|13
#
#75,47,61,53,29
#97,61,53,29,13
#75,29,13
#75,97,47,61,53
#61,13,29
#97,13,75,29,47"""

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

parsed_dict = {}

logging.debug(pages)

def dict_maker(input):
    
    for i in input:
        if i[0] not in parsed_dict:
            parsed_dict[i[0]] = []

        parsed_dict[i[0]].append(i[1])



dict_maker(pages)
logging.debug(f"Parsed Dict: {parsed_dict}")


temp_dict = {}

for key, value in parsed_dict.items():
    logging.debug(f"Key: {key}, Value: {value}")
    for number in value:
        if number not in parsed_dict.keys():
            temp_dict[number] = []

parsed_dict.update(temp_dict)

logging.debug(parsed_dict)

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

    topological_order = []

    logging.debug(f"InDegrees: {indegrees}")

    while len(queue) > 0:
        current_node = queue.pop(0)

        topological_order.append(current_node)

        for edge in nodes[current_node]:
            indegrees[edge] -= 1

            if indegrees[edge] == 0:
                queue.append(edge)
                logging.debug(f"queue: {queue}")

    if len(topological_order) != len(nodes):
        logging.debug("Circular Path Found")

    return topological_order

str_template = kahn(parsed_dict)
logging.debug(f"String Template: {str_template}")

template = []
for str in str_template:
    template.append(int(str))

def compare(template: list, input_array:list):
    check = None
    for i in input_array:
        hit = False

        try:
            if check == None:
                check = template.index(i)
                logging.debug(f"Value: {i}")
                logging.debug(f"Index: {check}")
            else:
                check = template.index(i, check +1)

        except ValueError as e:
            logging.debug(f"Error: {e}")
            
            try:
                template.index(i)
                hit = True 
                break
            except ValueError as e:
                logging.debug(f"Error: {e}") 
                pass        
            
    return hit

valid_updates = []
invalid_updates = []
for update in updates:
    logging.debug(f"Template: {template}")
    logging.debug(f"Update: {update}")
    if compare(template, update):
        invalid_updates.append(update)
        logging.debug("Compare: INVALID")
    else:
        valid_updates.append(update)
        logging.debug("Compare: VALID")

#for update in valid_updates:
#    logging.debug(f"Valid: {update}")
#    
for update in invalid_updates:
    logging.debug(f"Invalid: {update}")

middle_array = []

for update in valid_updates:
    middle = int(len(update) / 2)
    middle_array.append(update[middle])

final_count = 0
for number in middle_array:
    final_count += number

logging.debug(f"Final Count: {final_count}")