from day_2_input_data import input_data


## Challenge URL: https://adventofcode.com/2024/day/2

#######################################################

## Turning the input data reports and levels

data = input_data.input

report_list = []
reports = []
levels = []

## Creates list of reports
report_list = data.split("\n")

## Creates nested list of reports
for report in report_list:
    temp_report_list = report.split(" ")     
    reports.append(temp_report_list)

## Creates nested list of levels
for report in reports:
    level_list = []
    for str_level in report:    
        level_list.append(int(str_level))
    levels.append(level_list)

#######################################################

## Performing the actual logic for the puzzle
list_appended = 0
valid_levels = []

for report in levels:
    previous_level = None
    checked = 0
    rule_broken = False
    level_was_the_same = None
    valid_level_list = []
    for level in report:
        # Ensures that the level is skipped if the rule was broken 
        if rule_broken:
            break
        # Skips the first number in each report as we dont need to check it
        if previous_level == None and checked == 0:
            checked += 1
            previous_level = level
            continue

        # It can stop checking here for this level if the level and previous level are the same
        if previous_level == level:
            rule_broken = True
            break

        # This figures out whether the report should be checking for ascending or descending numbers
        if checked == 1:
            if previous_level == level:
                continue
            else:
                checked += 1
                if previous_level < level:
                    up_or_down = True 
                elif previous_level > level:
                    up_or_down = False

        # This performs the log to make sure that the numbers are within the acceptable parameters
        if up_or_down:
            if level < previous_level:
                rule_broken = True
                break
            elif level - previous_level > 3:
                rule_broken = True
                break
            else:
                valid_level_list.append(level)
        else:
            if level > previous_level:
                rule_broken = True
                break
            elif previous_level - level > 3:
                rule_broken = True
                break
            else:
                valid_level_list.append(level)

        previous_level = level       

    # Adds the list to the list for valid reports
    if valid_level_list != [] and rule_broken == False:
        valid_levels.append(valid_level_list)
        list_appended += 1
#######################################################

## Final Count 

valid_level_count = len(valid_levels)

print(valid_level_count)