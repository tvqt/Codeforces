t = int(input())


for i in range(t):
    n, k = [int(x) for x in input().split()]    
    p = [int(x) for x in input().split()]
    if k == 1: # if k == 1, then we know we can sort it
        print(0)
        continue
    able = [(p-i-1)%k for i, p in enumerate(p)]
    zeros = [a == 0 for a in able]
    if all(zeros): # if all elements are zero, then we can sort it
        print(0)
        continue
    elif sum(zeros) == len(zeros) -2 and sum(able) == k: # if there are only two non-zero elements and their sum is k, then we can sort it. Don't ask me why this works, because I don't know lol
        print(1)
        continue
    else: # otherwise, we can't sort it
        print(-1)
        continue


        