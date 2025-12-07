import sys, operator, functools

OPS = {'+': operator.add, '*': operator.mul}

*lines, last_line = sys.stdin.read().splitlines()

ops = [OPS[opname] for opname in last_line.split()]

number_groups_p1 = [
    [int(word) for word in group]
    for group in zip(*map(str.split, lines))
]
p1 = sum(
    functools.reduce(op, group)
    for op, group in zip(ops, number_groups_p1)
)
print(p1)

reformatted = '\n'.join(''.join(col).strip() for col in zip(*lines))
paras = reformatted.split('\n\n')
number_groups_p2 = [
    [int(word) for word in para.split()]
    for para in paras
]
p2 = sum(
    functools.reduce(op, group)
    for op, group in zip(ops, number_groups_p2)
)
print(p2)
