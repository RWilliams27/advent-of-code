from day_3_input_data import input_data
import re

## Challenge URL: https://adventofcode.com/2024/day/3#part2

#######################################################

data = input_data.input

#data = "carrot don't() dasfa do() juniper don't() eggs final"
#
### Find a way to parse only the valid bits before the rest of the logic
#
## Couldnt get regex to find the right parts without using re.escape
#entry = "do()"
#exit_word = "don't()"
#pattern = re.escape(entry) + r"(.*?)" + re.escape(exit_word)
#x = re.findall(pattern, data)
#
#print(x)
#
#y = data.find("don't()")
#
#print(y)
#
#z = data.split("don't()", 1)
#
#print(z)


#######################################################

split_data = data.split("don't()")



entry = "do()"
exit_word = "don't()"
pattern = re.escape(entry) + r"(.*?)" + re.escape(exit_word)
further_data = re.findall(pattern, data)

add_list = []
def mult(mul):
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

# Needed regex for finding the valid mul statements
first_valid_mul = re.findall(r"mul\(\d+,\s*\d+\)", split_data[0])

print(first_valid_mul)

stringified_further_data = str(further_data)

valid_mul = re.findall(r"mul\(\d+,\s*\d+\)", stringified_further_data)

for mul in first_valid_mul:
    mult(mul)

for mul in valid_mul:
    mult(mul)

# Add all the multiplied figures together
final_count = 0

for count in add_list:
    final_count += count

print(final_count)