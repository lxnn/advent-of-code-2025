import sys, math, heapq, itertools

p1_connections = int(sys.argv[1]) if len(sys.argv) >= 2 else 1000
points = [
    tuple(map(int, line.split(',')))
    for line in sys.stdin.read().splitlines()
]

closest_pairs = sorted(
    itertools.combinations(points, 2),
    key=lambda pair: math.dist(*pair),
)

parent = {box: box for box in points}
size = {box: 1 for box in points}
roots = size.keys()

def root(box):
    "Find the (arbitrary) root node/box of a circuit."
    if parent[box] == box:
        return box
    parent[box] = root(parent[box])
    return parent[box]

def connect(box1, box2):
    "Combine two circuits into one, if not already connected."
    root1, root2 = root(box1), root(box2)
    if root1 == root2:
        return
    parent[root2] = root1
    size[root1] += size[root2]
    del size[root2]

for pair in closest_pairs[:p1_connections]:
    connect(*pair)

three_largest = heapq.nlargest(3, roots, key=size.get)
p1 = math.prod(size[circuit] for circuit in three_largest)
print(p1)

remaining_pairs = itertools.islice(closest_pairs, p1_connections, None)
last_connected = None
while len(roots) > 1:
    last_connected = next(remaining_pairs)
    connect(*last_connected)

assert last_connected is not None

(x1, _, _), (x2, _, _) = last_connected
p2 = x1 * x2
print(p2)

