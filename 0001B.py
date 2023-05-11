import re

def to_base_26(number):
    base_26_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        digit = (number - 1) % 26
        result = base_26_digits[digit] + result
        number = (number - 1) // 26

    return result

def to_base_10(number):
    base_26_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0

    for i in range(len(number)):
        digit = base_26_digits.index(number[i])
        result = result * 26 + digit + 1

    return result


# get the number of lines of the input
n = int(input())
for i in range(n):
    # get the next line of the input
    line = input()
    # if line matches the format "RXXCXX"
    if re.match('R\d+C\d+', line):
        # get the row number
        row = int(line[1:line.index('C')])
        # get the column number
        col = int(line[line.index('C') + 1:])
        # convert the column number to a base 26 number, and print the result
        print(to_base_26(col) + str(row))        
    else:
        # split the line on the boundary between letters and numbers
        col, row = re.findall(r'[A-Za-z]+|\d+', line)
        # convert the column number to a base 10 number, and print the result
        print("R" + row + "C" + str(to_base_10(col)))
