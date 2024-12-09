from day_3_input_data import input_data
import re

## Challenge URL: https://adventofcode.com/2024/day/3#part2

#######################################################

data = input_data.input

data = """}mul(620,236)where()*@}!&[mul(589,126)]&^]mul(260,42)when() when()$ ?{/^*mul(335,250)>,@!<{when()+-$don't()*'^?+>>/%:mul(422,738),mul(694,717);~;%<[why()>@-mul(417,219)?&who(474,989){select()-{#mul(366,638)mul(773,126)/*{mul(757,799)]when()mul(778,467)^mul(487,365)]*'{where(952,954){?who()who()when()mul(172,666)#<do()why()~&why())'< {mul(33,475)}mul(916,60)what()?when()>?$,-mul(250,228)(]when()}<mul(817,274)'{})mul(836,930):@how()]!@'select()~?mul(514,457)from()&what()what()when()mul(872,884)select()<select()from()'!who()mul(11,966)/from()(~}#,(*from()mul(941,908)#>mul(760,139)mul(892,161)!'@[%when()<(mul(775,872)+~#)//$select()mul(946,63)how()??select()?from(277,915)~'mul(637,565)~mul(881,294)who()what()}mul(995,866)?mul(952,57)who()mul(387,599)mul(46,724)who()[how()select()mul(992,19)'~mul(909,687)where()mul(953,804)from()/;where(474,270)from()}mul(907,410)&(&what()%{mul(192,898)who()-,mul(196,400)#--{%]how()mul(144,141)~@[when()!%:[mul(377,942)^*mul(89,46)who()<}when()?!'%mul(172,448){]@mul(351,18)~]&!$mul(490,127)/]] }}mul(851,465)when()*-why()what()))@+<mul(465,978):*>^<-select()do()%#+;%:mul(549,307)<where(154,242)(;< /who()mul(426,943)mul(477,782)*?do() mul(745,445)@  (how()$where()mul(118,902)when()when()}!how()don't();mul(523,781)"""
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
    print(output)

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

print(stringified_further_data)

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