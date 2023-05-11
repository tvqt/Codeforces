import math
n, m, a = [int(x) for x in input().split()]

print(math.ceil(m/a) * math.ceil(n/a))  