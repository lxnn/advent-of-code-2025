import sys

with open(sys.argv[1]) as file:
    paper = {
        complex(r, c)
        for r, line in enumerate(file.read().splitlines())
        for c, char in enumerate(line)
        if char == '@'
    }

def neighbours(pos):
    return {
        pos + complex(dr, dc)
        for dr in (-1, 0, +1)
        for dc in (-1, 0, +1)
        if dr or dc
    }

def get_accessible(paper):
    return {
        pos
        for pos in paper
        if len(neighbours(pos) & paper) < 4
    }

p1 = len(get_accessible(paper))
print(p1)

remaining = set(paper)
while removed := get_accessible(remaining):
    remaining -= removed

p2 = len(paper) - len(remaining)
print(p2)

