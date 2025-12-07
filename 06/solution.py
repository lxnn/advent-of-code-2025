import sys, operator, functools, itertools

lines = sys.stdin.read().splitlines()

OPS = {'+': operator.add, '*': operator.mul}

results_p1 = [
    functools.reduce(OPS[opname], map(int, numbers))
    for *numbers, opname in zip(*(line.split() for line in lines))
]

p1 = sum(results_p1)
print(p1)

problems = [
    (
        OPS[first[-1]],
        [int(first[:-1]), *map(int, rest)]
    )
    for is_separator, (first, *rest) in itertools.groupby(
        (''.join(column) for column in zip(*lines)),
        lambda column: column.strip() == '',
    )
    if not is_separator
]
results_p2 = [
    functools.reduce(op, numbers)
    for op, numbers in problems
]
p2 = sum(results_p2)
print(p2)
