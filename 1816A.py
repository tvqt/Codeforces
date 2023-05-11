import fractions
t = int(input())

def passes_through_another_coordinate(x1, y1, x2, y2):
    if x1 != x2:
        slope = (y2 - y1) / (x2 - x1)
        # get the remainder of the slope
        if slope % 1 == 0:
            x = x1 + 1
            y = x1 + slope
        else:
            f = fractions.Fraction(slope).limit_denominator()
            x = x1 + f.denominator
            y = y1 + f.numerator
    else:
        x = x1
        y = y1 + 1
    return (x, y) != (x2, y2)

def generate_coordinates(x, y, d):
        return ([(x - d, j) for j in range(y - d + 1, y + d)] + 
                [(x + d, j) for j in range(y - d + 1, y + d)] +  
                [(i, y - d) for i in range(x - d, x + d + 1)] + 
                [(i, y + d) for i in range(x - d, x + d + 1)])

def solve(a, b):
    if not passes_through_another_coordinate(0, 0, a, b):
        print(1)
        print(a, b)
        return
    d = 1
    while True:
        neighbours = generate_coordinates(a, b, d)
        for neighbour in neighbours:
            if not passes_through_another_coordinate(0, 0, neighbour[0], neighbour[1]):
                if not passes_through_another_coordinate(neighbour[0], neighbour[1], a, b):
                    print(2)
                    print(neighbour[0], neighbour[1])
                    print(a, b)
                    return
        d += 1

for i in range(t):
    a, b = [int(x) for x in input().split()]
    solve(a, b)