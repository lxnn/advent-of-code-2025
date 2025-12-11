import sys
from collections import Counter

graph = {
    lhs.strip(): set(rhs.split())
    for lhs, rhs in (line.split(":") for line in sys.stdin.readlines())
}

def neighbours(node):
    return graph.get(node, set())

def count_paths(start, goal, successors):
    frontier = Counter([start])
    total = 0
    while frontier:
        total += frontier[goal]
        new_frontier = Counter()
        for state, count in frontier.items():
            for successor in successors(state):
                new_frontier[successor] += count
        frontier = new_frontier
    return total

p1 = count_paths("you", "out", neighbours)
print(p1)

def successors_p2(state):
    node, dac, fft = state
    for neighbour in neighbours(node):
        yield (neighbour, dac or neighbour == "dac", fft or neighbour == "fft")

p2 = count_paths(("svr", False, False), ("out", True, True), successors_p2)
print(p2)
