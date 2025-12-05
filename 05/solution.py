import sys

with open(sys.argv[1]) as file:
    first_para, second_para = file.read().split('\n\n')
    ranges = []
    for line in first_para.splitlines():
        start, end = map(int, line.split('-'))
        ranges.append((start, end+1))
    ingredients = list(map(int, second_para.split()))

def is_fresh(ingredient):
    return any(start <= ingredient < stop for (start, stop) in ranges)

p1 = sum(is_fresh(ingredient) for ingredient in ingredients)
print(p1)

total_ids = 0
range_iter = iter(sorted(ranges))
curr_start, curr_stop = next(range_iter)

for start, stop in range_iter:
    if start <= curr_stop:
        curr_stop = max(stop, curr_stop)
    else:
        total_ids += curr_stop - curr_start
        curr_start, curr_stop = start, stop
total_ids += curr_stop - curr_start

p2 = total_ids
print(p2)

