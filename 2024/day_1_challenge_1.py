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
        print(f"Number: {item} was added to List A")
    else:
        list_b.append(item)
        print(f"Number: {item} was added to List B")

#######################################################

## Sorting lists by ascending value
list_a.sort()
list_b.sort()

## Calculating the distance between each pair and adding it to a list
distance_list = []

i = 0
while i < len(list_a):
    list_a_item = int(list_a[i])
    list_b_item = int(list_b[i])
    print(list_a_item, list_b_item)

    if list_a_item < list_b_item:
        distance_list.append(list_b_item - list_a_item)
    else:
        distance_list.append(list_a_item - list_b_item)
    print(f"Distance of pair {i} is {distance_list[i]}")


    i += 1

#######################################################