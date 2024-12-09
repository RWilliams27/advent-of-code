from day_3_input_data import input_data
import re

## Challenge URL: https://adventofcode.com/2024/day/3

#######################################################

data = input_data.input

# Needed regex for finding the valid mul statements
x = re.findall(r"mul\(\d+,\s*\d+\)", data)

print(x)