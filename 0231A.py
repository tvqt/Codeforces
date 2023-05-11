# get the first line of the input
n = int(input())
# initialize the counter
counter = 0
# get the next n lines of the input
for i in range(n):
    # get the next line of the input
    line = input()
    # if the line contains at least two 1's
    if line.count('1') >= 2:
        # increment the counter
        counter += 1
# print the counter
print(counter)