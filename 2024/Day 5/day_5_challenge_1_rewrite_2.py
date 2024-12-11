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

raw_rules, updates = data.strip().split("\n\n")
rules = []

for line in raw_rules.split("\n"):
    a, b = line.split("|")
    rules.append((int(a), int(b)))

updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

def rule_check(update):
    id = {}

    for index, value in enumerate(update):
        id[value] = index

    for a, b in rules:
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

print(f"FINAL COUNT: {final_count}")
