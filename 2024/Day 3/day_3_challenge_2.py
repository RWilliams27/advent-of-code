#Test 3
import re
from day_3_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/3#part2

#######################################################

def reader(input):
    for i in input:
        print("------------------------------------------------")
        print(i)
        print("------------------------------------------------")

data = input_data.input

first_split = data.split("don't()", 1)
first_valid_mult = first_split[0]
new_data = first_split[1]

dont_split = new_data.split("don't()")

new_list =[]

for i in dont_split:
    y = i.split("do()")


    timer = 0
    if len(y) > 1:
        for j in y:
            if timer == 0:
                timer += 1
                continue

            new_list.append(y[timer])

            timer += 1

add_list = []
def mult(mul):
    # Turns the fetched "valid-muls" into pairs of numbers
    output = mul.lstrip("mul(")
    output = output.rstrip(")")
    output = output.split(",")
    print(output)

    # Turn all the numbers into integers
    output[0] = int(output[0])
    output[1] = int(output[1])

    # Multiplies all the pairs
    output = output[0] * output [1]

    add_list.append(output)

mult_list = []
for item in new_list:
    mult_list.append(re.findall(r"mul\(\d+,\s*\d+\)", item))

data_mult_list = []

first_mult_list = re.findall(r"mul\(\d+,\s*\d+\)", first_split[0])

for item in mult_list:
    for i in item:
        data_mult_list.append(i)


for i in first_mult_list:
    data_mult_list.append(i)

for mul in data_mult_list:
    mult(mul)

# Add all the multiplied figures together
final_count = 0

for count in add_list:
    final_count += count

print(final_count)