import sys

with open(sys.argv[1]) as file:
    instructions = file.read().splitlines()

at = 50
p1 = 0
for instruction in instructions:
    before = at
    sign = +1 if instruction[0] == 'R' else -1
    dist = int(instruction[1:])
    at += sign * dist
    at %= 100
    p1 += at == 0
print(p1)

at = 50
p2 = 0
for instruction in instructions:
    before = at
    sign = +1 if instruction[0] == 'R' else -1
    dist = int(instruction[1:])
    div, at = divmod(at + sign*dist, 100)
    if sign > 0:
        p2 += div
    else:
        p2 += abs(div) + (at == 0) - (before == 0)
print(p2)

