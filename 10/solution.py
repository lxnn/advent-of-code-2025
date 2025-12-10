import sys, re
import numpy as np
import scipy as sp

def ints(string):
    return map(int, re.findall(r"[0-9]+", string))

def make_button(length, schematic):
    button = np.zeros(length, dtype=int)
    button[list(ints(schematic))] = 1
    return button

def powerset(iterable):
    pool = list(iterable)
    for i in range(1 << len(pool)):
        yield tuple(pool[j] for j in range(len(pool)) if (1 << j) & i)

def toggle_all(lights, buttons):
    for button in buttons:
        lights ^= button
    return lights

machines = []
for line in sys.stdin.readlines():
    light_diagram, *button_schematics, joltage_requirements = line.split()
    target = np.array(list(light_diagram.strip("[]"))) == "#"
    buttons = [make_button(len(target), schematic) for schematic in button_schematics]
    joltage_targets = np.array(list(ints(joltage_requirements)), dtype=int)
    machines.append((target, buttons, joltage_targets))

def min_button_pushes_p1(target, buttons):
    return min(
        len(subset)
        for subset in powerset(buttons)
        if (toggle_all(np.zeros(len(target), dtype=int), subset) == target).all()
    )

p1 = sum(min_button_pushes_p1(target, buttons) for target, buttons, _ in machines)
print(p1)

def solve_p2(target, buttons):
    c = np.ones(len(buttons), dtype=int)
    A = np.array(buttons).T
    b = target
    result = sp.optimize.milp(
        c,
        integrality=1,
        constraints=(A, b, b),
    )
    assert result.success
    return round(result.x.sum())

p2 = sum(solve_p2(joltage_targets, buttons) for _, buttons, joltage_targets in machines)
print(p2)
