import sys, re

def ints(s):
    return list(map(int, re.findall(r"[0-9]+", s)))

*shapes, problems = sys.stdin.read().split("\n\n")

shape_dimensions = [
    (len(shape[0]), len(shape))
    for _, *shape in map(str.splitlines, shapes)
]
shape_widths, shape_heights = zip(*shape_dimensions)
max_shape_width = max(shape_widths)
max_shape_height = max(shape_heights)

total_solvable = 0
for problem in problems.splitlines():
    width, height, *quantities = ints(problem)
    total_filled = sum(
        shape.count("#") * quantity
        for shape, quantity in zip(shapes, quantities)
    )
    definitely_unsolvable = width * height < total_filled

    rows = width // max_shape_width
    cols = height // max_shape_height
    definitely_solvable = rows * cols >= sum(quantities)

    assert definitely_solvable ^ definitely_unsolvable
    if definitely_solvable:
        total_solvable += 1

print(total_solvable)
