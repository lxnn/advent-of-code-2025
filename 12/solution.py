import sys, re

def ints(s):
    return list(map(int, re.findall(r'[0-9]+', s)))

*shapes, problems = sys.stdin.read().split('\n\n')

total_solvable = 0
for problem in problems.splitlines():
    width, height, *quantities = ints(problem)
    total_filled = sum(
        shape.count('#') * quantity
        for shape, quantity in zip(shapes, quantities)
    )
    definitely_unsolvable = width * height < total_filled
    definitely_solvable = (width - width%3) * (height - height%3) >= sum(quantities) * 9
    assert definitely_solvable or definitely_unsolvable
    if definitely_solvable:
        total_solvable += 1

print(total_solvable)
