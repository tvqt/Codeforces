q = int(input())

def solve(t, a, b):
    # get the index of the largest element in b
    a = [x+i for i, x in enumerate(a)]
    b = [0 if a[i] > t else x for i, x in enumerate(b)]
    # check if any of the elements in b are not 0. If so, print the index of the largest element in b. Otherwise, print -1
    print(b.index(max(b))+1) if any(x != 0 for x in b) else print(-1)
  

for i in range(q):
    n, t = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    solve(t, a, b)