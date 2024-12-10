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


## Parsing the input

# This separates the pages from the updates and separates the pages and updates into lists with one entry each
split_data = data.split("\n\n") 
unsanitised_pages = split_data[0]
unsanitised_updates = split_data[1]

pages = unsanitised_pages.split("\n")
updates = unsanitised_updates.split("\n")

