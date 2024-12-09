from day_3_input_data import input_data
import re

## Challenge URL: https://adventofcode.com/2024/day/3

#######################################################

data = input_data.input

# Needed regex for finding the valid mul statements
valid_mul = re.findall(r"mul\(\d+,\s*\d+\)", data)

add_list = []

for mul in valid_mul:
    # Turns the fetched "valid-muls" into pairs of numbers
    output = mul.lstrip("mul(")
    output = output.rstrip(")")
    output = output.split(",")

    # Turn all the numbers into integers
    output[0] = int(output[0])
    output[1] = int(output[1])

    # Multiplies all the pairs
    output = output[0] * output [1]

    add_list.append(output)

# Add all the multiplied figures together
final_count = 0

for count in add_list:
    final_count += count

print(final_count)