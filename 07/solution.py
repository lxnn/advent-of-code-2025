import sys
from collections import Counter

lines = sys.stdin.read().splitlines()

grid = {
    (r, c): char
    for r, line in enumerate(lines)
    for c, char in enumerate(line)
}

def getall(target):
    return {cell for cell, char in grid.items() if char == target}

all_cells = grid.keys()
splitters = getall('^')
timelines = Counter(getall('S'))
p1 = 0
p2 = 0

while timelines:
    updated_timelines = Counter()
    for (r, c), count in timelines.items():
        successor = (r+1, c)
        if successor in splitters:
            updated_timelines[r+1, c-1] += count
            updated_timelines[r+1, c+1] += count
            p1 += 1
        elif successor in all_cells:
            updated_timelines[r+1, c] += count
        else:
            p2 += count
    timelines = updated_timelines

print(p1)
print(p2)

