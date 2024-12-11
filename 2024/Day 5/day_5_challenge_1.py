from day_5_input_data import input_data
import logging
from collections import deque, defaultdict

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

for page in pages:
    print(page)

######################################################

parsed_dict = {}

logging.debug(pages)

def dict_maker(input):
    
    for i in input:
        if i[0] not in parsed_dict.keys():
            parsed_dict[i[0]] = []
        parsed_dict[i[0]].append(i[1])

        #if i[1] not in parsed_dict.keys(): # Do I want this?
        #    parsed_dict[i[1]] = []

        logging.debug(f"Input: {i}")
        logging.debug(f"Parsed Dict per step: {parsed_dict}")

dict_maker(pages)
logging.debug(f"Parsed Dict: {parsed_dict}")

#logging.debug(f"Thirteen and Sixty Six: {parsed_dict["13"]}   |   {parsed_dict["66"]}")

temp_dict = {}

for key, value in parsed_dict.items():
    logging.debug(f"Key: {key}, Value: {value}")
    for number in value:
        if number not in parsed_dict.keys():
            temp_dict[number] = []

parsed_dict.update(temp_dict)
logging.debug(f"TEMP DICT: {temp_dict}")

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


order = []

def dfs_topological_sort(graph):
    # Helper function to perform DFS
    def dfs(node, graph, visited, stack):
        # Mark the node as visited
        visited[node] = True
        
        # Visit all the neighbors of the node
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        
        # Push the node to the stack after visiting all neighbors
        stack.append(node)

    visited = {node: False for node in graph}  # Keep track of visited nodes
    stack = []  # This will store the topologically sorted nodes

    # Perform DFS for each unvisited node
    for node in graph:
        if not visited[node]:
            dfs(node, graph, visited, stack)

    # The stack will contain the nodes in reverse topological order
    return stack[::-1]

str_template = dfs_topological_sort(parsed_dict)
logging.debug(f"STRING TEMPLATE: {str_template}")
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
                check = template.index(i, check)
                logging.debug(f"Value: {i}")
                logging.debug(f"Index: {check}")

        except ValueError as e:
            logging.debug(f"Error A: {e}")
            
            try:
                logging.debug("WE HERE")
                testing = template.index(i)
                logging.debug(f"Index 2 |   {testing}")
                hit = True 
                break
            except ValueError as e:
                logging.debug("WE NEVER GET HERE")
                logging.debug(f"Error B: {e}") 
                #pass        
            
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






def chat_kahn(graph):
    # Step 1: Compute in-degree for each node
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
        if node not in in_degree:
            in_degree[node] = 0

    # Step 2: Initialize the queue with nodes having in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])

    topological_order = []

    # Step 3: Process nodes in the queue
    while queue:
        node = queue.popleft()
        topological_order.append(node)

        # For each neighbor, reduce the in-degree
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the topological order contains all nodes, it's a valid sort
    if len(topological_order) == len(in_degree):
        logging.debug("Topological Order:", topological_order)
    else:
        logging.debug("The graph has a cycle and cannot be topologically sorted.")


chat_kahn(parsed_dict)
logging.debug(order)

