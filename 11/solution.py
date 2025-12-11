import sys
from collections import Counter

graph = {
    lhs.strip(): set(rhs.split())
    for lhs, rhs in (
        line.split(':')
        for line in sys.stdin.readlines()
    )
}

path_count = Counter()
path_count['you'] = 1
p1 = 0
while path_count:
    p1 += path_count['out']
    new_path_count = Counter()
    for node, count in path_count.items():
        for successor in graph.get(node, set()):
            new_path_count[successor] += count
    path_count = new_path_count
print(p1)

state_count = Counter()
state_count['svr', False, False] = 1
p2 = 0
while state_count:
    p2 += state_count['out', True, True]
    new_state_count = Counter()
    for (node, dac, fft), count in state_count.items():
        for successor in graph.get(node, set()):
            new_state = (
                successor,
                dac or successor == 'dac',
                fft or successor == 'fft',
            )
            new_state_count[new_state] += count
    state_count = new_state_count
print(p2)
