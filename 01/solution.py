import sys

lines = sys.stdin.read().splitlines()

rotations = [
    (+1 if first == 'R' else -1) * int(''.join(rest))
    for first, *rest in lines
]

at = 50
p1 = 0
p2 = 0

for rotation in rotations:
    before = at
    div, mod = divmod(at + rotation, 100)
    at = mod
    if rotation > 0:
        p1 += (at == 0)
        p2 += div
    else:
        p1 += (at == 0)
        p2 += abs(div) + (at == 0) - (before == 0)

print(p1)
print(p2)
