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

