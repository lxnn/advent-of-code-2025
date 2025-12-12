import sys, re

def ints(s):
    return list(map(int, re.findall(r'[0-9]+', s)))

*raw_shapes, raw_problems = sys.stdin.read().split('\n\n')

shape_sizes = [shape.count('#') for shape in raw_shapes]
spare_cells = [
    width * height - sum(count * size for count, size in zip(counts, shape_sizes))
    for width, height, *counts in map(ints, raw_problems.splitlines())
]

for spare in spare_cells:
    assert spare < 0 or spare > 100

print(sum(spare >= 0 for spare in spare_cells))
