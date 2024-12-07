from day_1_challenge_1_input_data import input_data

## Turning the input data into the two required lists

data = input_data.input

no_new_lines = data.replace("\n", "   ")
input_list = no_new_lines.rsplit("   ")

list_a = []
list_b = []

i = 0
for item in input_list:
    i += 1

    if (i % 2) != 0:
        list_a.append(item)
    else:
        list_b.append(item)

#######################################################