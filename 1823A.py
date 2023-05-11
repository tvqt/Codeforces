import math
t = int(input())

def solve(n, k):
    if n == 2 and k == 0:
        print("YES")
        print("1 -1")
    elif math.ceil(n/2)-1 <= k <= math.floor(n/2): 
        print("YES")
        print(' '.join(["1"] * (k*2) + ["-1"] * (math.ceil(n/2)-k)))
    else:
        print("NO")

for i in range(t):
    n, k = [int(x) for x in input().split()]
    solve(n, k)