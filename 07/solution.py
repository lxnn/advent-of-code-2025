import sys
from collections import Counter

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

grid = {
    (r, c): char
    for r, line in enumerate(lines)
    for c, char in enumerate(line)
}

def getall(target):
    return {cell for cell, char in grid.items() if char == target}

all_cells = grid.keys()
splitters = getall('^')

split_count = 0
beams = getall('S')
while beams:
    updated_beams = set()
    for (r, c) in beams:
        if (r+1, c) in splitters:
            updated_beams.add((r+1, c-1))
            updated_beams.add((r+1, c+1))
            split_count += 1
        else:
            updated_beams.add((r+1, c))
    beams = updated_beams & all_cells

p1 = split_count
print(p1)

timelines = Counter(getall('S'))
ultimate_count = 0
while timelines:
    updated_timelines = Counter()
    for (r, c), count in timelines.items():
        successor = (r+1, c)
        if successor in splitters:
            updated_timelines[r+1, c-1] += count
            updated_timelines[r+1, c+1] += count
        elif successor in all_cells:
            updated_timelines[r+1, c] += count
        else:
            ultimate_count += count
    timelines = updated_timelines

p2 = ultimate_count
print(p2)

