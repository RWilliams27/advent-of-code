from day_2_input_data import input_data
import logging

## Challenge URL: https://adventofcode.com/2024/day/2

#######################################################

logging.basicConfig(
    filename="Day_2_Challenge_2.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M",
    level=logging.DEBUG,
)

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
    print(report)
    level_list = []
    for str_level in report:
        print(str_level)       
        level_list.append(int(str_level))
        print(level_list)
    levels.append(level_list)
        

    print("----------------------")

#######################################################

## Performing the actual logic for the puzzle
list_appended = 0
debug_broken = 0
valid_levels = []

for report in levels:
    print("---------------------------------------")
    print(report)
    previous_level = None
    checked = 0
    rule_broken = False
    level_was_the_same = None
    valid_level_list = []
    for level in report:
        print("---------------------------------------")
        logging.debug("---------------------------------------")
        print(f"Previous Level: {previous_level}")
        # Ensures that the level is skipped if the rule was broken 
        if rule_broken:
            break
        # Skips the first number in each report as we dont need to check it
        if previous_level == None and checked == 0:
            checked += 1
            previous_level = level
            print(f"SKIPPED {level}")
            continue
        else:
            print(f"LEVEL: {level}")

        # This figures out whether the report should be checking for ascending or descending numbers
        if checked == 1:
            if previous_level == level:
                print(f"Previous Level: {previous_level} and Level: {level} are the same")
                continue
            else:
                checked += 1
                if previous_level < level:
                    up_or_down = True 
                elif previous_level > level:
                    up_or_down = False
                print(f"Up or down? {up_or_down}")

        # It can stop checking here for this level if the level and previous level are the same
        if previous_level == level:
            print(f"Previous Level: {previous_level} and Level: {level} are the same")
            level_was_the_same = True
            continue

        if up_or_down:
            if level - previous_level > 3:
                logging.debug("Rule Broken")
                print("Rule Broken")
                debug_broken += 1
                rule_broken = True
                break
            else:
                valid_level_list.append(level)
        else:
            if previous_level - level > 3:
                logging.debug("Rule Broken")
                print("Rule Broken")
                debug_broken += 1
                rule_broken = True
                break
            else:
                valid_level_list.append(level)

        previous_level = level  
#        print(f"Valid List: {valid_level_list}")      
#
#    if valid_level_list != []:
#        valid_levels.append(valid_level_list)
#        print("LIST APPENDED")
#        list_appended += 1
#print("---------------------------------------")
#logging.debug("---------------------------------------")
#print(valid_levels)
#print(list_appended)
#print(debug_broken)
#######################################################

## Final Count 

valid_level_count = len(levels) - debug_broken

print(valid_level_count)