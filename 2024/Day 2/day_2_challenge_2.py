from day_2_input_data import input_data

## Challenge URL: https://adventofcode.com/2024/day/2#part2

#######################################################

report_list = []
reports = []
levels = []

data = input_data.input

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


for report in levels:
    print(report)


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
            if level > previous_level:
                rule_broken = True
                break
            elif previous_level - level > 3:
                rule_broken = True
                break
            

        previous_level = level       

    if rule_broken:
        return True
    else:
        return False



def mini_check(report):
    broken = False
    for level in report:
        if broken:
            break
        if level == 7:
            broken = True

    if broken:
        return True
    else:
        return False



array = []
new_list = []
nested_list = []

for report in levels:
    new_list = []
    i = 0 
    print("------------------------------------------------------")
    while i <= len(report):
        print(f"Report: {report}")
        maths = len(report) - i
        print(maths)

        temp_list = []

        k = 0
        while k < len(report):
            if k == i:
                k += 1
                continue

            temp_list.append(report[k])
            k += 1

        new_list.append(temp_list)
        print(f"TEMP_Report: {temp_list}")
        print("------------------------------------------------------")
        i += 1

    print("------------------------------------------------------")

    nested_list.append(new_list)

final_nested_list = []

for nested_report in nested_list:
    valid = False
    print("------------------------------------------------------")
    print(nested_report)
    for report in nested_report:
        print(report)

        if level_check(report) == False:
           print(f"Report Valid: {report}")
           valid = True
           final_nested_list.append(report)
           break
            

    if valid:
        print(f"HIT")
    print("------------------------------------------------------")


print(len(final_nested_list))