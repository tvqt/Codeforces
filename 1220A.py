n = int(input())
zero = ['z', 'e', 'r', 'o']
one = ['o', 'n', 'e']
input = [char for char in input()]
out = ''
# count the number of each character in the input
ones = min([input.count(char) for char in one])
zeros = [input.count(char) for char in zero]
zeros[1] -= ones
zeros[3] -= ones
zeros = min(zeros)
# create a string which is '1' repeated ones times

print(' '.join([str(1)] * ones + [str(0)] * zeros))
