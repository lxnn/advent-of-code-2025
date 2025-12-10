import sys, itertools

tiles = [
    (int(x), int(y))
    for x, y in (line.strip().split(",") for line in sys.stdin.readlines())
]

head, *tail = tiles
edges = list(zip(tiles, [*tail, head]))

def intersect(rect1, rect2):
    """
    Determine whether the two rectangles intersect.

    A rectangle is represented by a pair of opposite corners (inclusive). A
    line is just a thin rectangle. Two rectangles are considered to intersect
    if any tile of one rectangle is co-located with any *interior* tile of the
    other rectangle: if only the edge tiles of the rectangles overlap, this is
    not considered intersection, for the sake of this function.
    """
    (x0, y0), (x1, y1) = rect1
    (x2, y2), (x3, y3) = rect2
    x0, x1 = min(x0, x1), max(x0, x1)
    x2, x3 = min(x2, x3), max(x2, x3)
    y0, y1 = min(y0, y1), max(y0, y1)
    y2, y3 = min(y2, y3), max(y2, y3)
    return not (x1 <= x2 or x3 <= x0 or y1 <= y2 or y3 <= y0)

def area(rect):
    (x0, y0), (x1, y1) = rect
    width = abs(x0 - x1) + 1
    height = abs(y0 - y1) + 1
    return width * height

valid_rects_p1 = itertools.combinations(tiles, 2)
p1 = max(area(rect) for rect in valid_rects_p1)
print(p1)

valid_rects_p2 = (
    rect
    for rect in itertools.combinations(tiles, 2)
    if not any(intersect(rect, edge) for edge in edges)
)
p2 = max(area(rect) for rect in valid_rects_p2)
print(p2)
