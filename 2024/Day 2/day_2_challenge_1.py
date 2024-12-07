from day_2_input_data import input_data
import logging

## Challenge URL: https://adventofcode.com/2024/day/2

#######################################################

logging.basicConfig(
    filename="Day_2_Challenge_2.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s.%(msecs)05d - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%dT%H:%M:%S",
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
    logging.debug(report)
    level_list = []
    for str_level in report:
        logging.debug(str_level)       
        level_list.append(int(str_level))
        logging.debug(level_list)
    levels.append(level_list)
        

    logging.debug("----------------------")

#######################################################

## Performing the actual logic for the puzzle
list_appended = 0
debug_broken = 0
valid_levels = []

for report in levels:
    logging.debug("---------------------------------------")
    logging.debug(report)
    previous_level = None
    checked = 0
    rule_broken = False
    level_was_the_same = None
    valid_level_list = []
    for level in report:
        logging.debug("---------------------------------------")
        logging.debug(f"Previous Level: {previous_level}")
        # Ensures that the level is skipped if the rule was broken 
        if rule_broken:
            break
        # Skips the first number in each report as we dont need to check it
        if previous_level == None and checked == 0:
            checked += 1
            previous_level = level
            logging.debug(f"SKIPPED {level}")
            continue
        else:
            logging.debug(f"LEVEL: {level}")

        # It can stop checking here for this level if the level and previous level are the same
        if previous_level == level:
            logging.debug(f"Previous Level: {previous_level} and Level: {level} are the same")
            rule_broken = True
            break

        # This figures out whether the report should be checking for ascending or descending numbers
        if checked == 1:
            if previous_level == level:
                logging.debug(f"Previous Level: {previous_level} and Level: {level} are the same")
                continue
            else:
                checked += 1
                if previous_level < level:
                    up_or_down = True 
                elif previous_level > level:
                    up_or_down = False
                logging.debug(f"Up or down? {up_or_down}")

        

        if up_or_down:
            if level < previous_level:
                rule_broken = True
                break
            elif level - previous_level > 3:
                logging.debug("Rule Broken")
                debug_broken += 1
                rule_broken = True
                break
            else:
                valid_level_list.append(level)
        else:
            if level > previous_level:
                rule_broken = True
                break
            elif previous_level - level > 3:
                logging.debug("Rule Broken")
                debug_broken += 1
                rule_broken = True
                break
            else:
                valid_level_list.append(level)

        previous_level = level  
        logging.debug(f"Valid List: {valid_level_list}")      

    if valid_level_list != [] and rule_broken == False:
        valid_levels.append(valid_level_list)
        logging.debug("LIST APPENDED")
        list_appended += 1
logging.debug("---------------------------------------")
logging.debug(valid_levels)
logging.debug(list_appended)
logging.debug(debug_broken)
#######################################################

## Final Count 

valid_level_count = len(valid_levels)

logging.debug(valid_level_count)