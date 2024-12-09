from day_2_input_data import input_data

import logging
## Challenge URL: https://adventofcode.com/2024/day/2#part2

#######################################################

logging.basicConfig(
    filename="Day_2_Challenge_2.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s.%(msecs)06d - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.DEBUG,
)


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
valid_levels = []
not_valid_levels = []

def level_check(report):    
    previous_level = None
    checked = 0
    rule_broken = False
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

        # This performs the logic to make sure that the numbers are within the acceptable parameters
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
    elif rule_broken: 
        not_valid_levels.append(report)

new_valid_levels = []
def invalid_level_check(report):    
    previous_level = None
    checked = 0
    rule_broken = False
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

        # This performs the logic to make sure that the numbers are within the acceptable parameters
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
        new_valid_levels.append(valid_level_list)

def level_check_new_attempt(report):    
    previous_level = None
    checked = 0
    rule_broken = 0
    valid_level_list = []

    for level in report:
        # Ensures that the level is skipped if the rule was broken 
        if rule_broken >= 2:
            break

        # Skips the first number in each report as we dont need to check it
        if previous_level == None and checked == 0:
            checked += 1
            previous_level = level
            continue

        # It can stop checking here for this level if the level and previous level are the same
        if previous_level == level:
            rule_broken += 1 
            logging.debug(f"Rule was broken due to matching figures: {rule_broken}")
            continue

        # This figures out whether the report should be checking for ascending or descending numbers
        if checked == 1:
            if previous_level == level:
                rule_broken += 1
                logging.debug(f"Rule was broken due to matching figures: {rule_broken}")
                continue
            else:
                checked += 1
                if previous_level < level:
                    up_or_down = True 
                elif previous_level > level:
                    up_or_down = False

        # This performs the logic to make sure that the numbers are within the acceptable parameters
        if up_or_down:
            if level < previous_level:
                rule_broken += 1
                logging.debug(f"Rule was broken due to it going the wrong direction: {rule_broken}")
                continue
            elif level - previous_level > 3:
                rule_broken += 1
                logging.debug(f"Rule was broken due to it going the the gap being too big: {rule_broken}")
                continue
            else:
                valid_level_list.append(level)
        else:
            if level > previous_level:
                rule_broken += 1
                logging.debug(f"Rule was broken due to it going the wrong direction: {rule_broken}")
                continue
            elif previous_level - level > 3:
                rule_broken += 1
                logging.debug(f"Rule was broken due to it going the gap being too big: {rule_broken}")
                continue
            else:
                valid_level_list.append(level)

        previous_level = level       

    # Adds the list to the list for valid reports
    if valid_level_list != [] and rule_broken <= 2:
        valid_levels.append(valid_level_list)
    elif rule_broken: 
        not_valid_levels.append(report)


for report in levels:
    level_check(report)


#   Take a report
#   Create the same amount of lists as the length of the report
#   Within each of these new lists, add the report minus one number in the list, which iterates
#   This should create a nested list that contains all lists to test 

new_list = []

for report in not_valid_levels:
    i = 0 
    logging.debug("------------------------------------------------------")
    while i <= len(report):
        logging.debug(f"Report: {report}")
        maths = len(report) - i
        logging.debug(maths)

        temp_list = []

        k = 0
        while k < len(report):
            if k == i:
                k += 1
                continue

            temp_list.append(report[k])
            k += 1

        new_list.append(temp_list)
        logging.debug(f"TEMP_Report: {temp_list}")
        logging.debug("------------------------------------------------------")
        i += 1

    logging.debug("------------------------------------------------------")
    
for report in new_list:
    invalid_level_check(report)

for report in new_valid_levels:
    logging.debug(report)

#######################################################

## Final Count 

valid_level_count = len(valid_levels)

logging.debug(f"Final valid_levels count: {valid_level_count}")
logging.debug(f"Final not_valid_levels count: {len(not_valid_levels)}")
logging.debug(f"Final new_valid_levels count: {len(new_valid_levels)}")
logging.debug(f"Please be right: {valid_level_count + len(new_valid_levels)}")