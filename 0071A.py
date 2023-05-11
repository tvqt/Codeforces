# get the first line of the input
n = int(input())
# get the next n lines of the input
for i in range(n):
    # get the next line of the input
    word = input()
    # if the length of the word is greater than 10
    if len(word) > 10:
        # print the first and last letter of the word
        print(word[0] + str(len(word) - 2) + word[-1])
    # otherwise
    else:
        # print the word
        print(word)