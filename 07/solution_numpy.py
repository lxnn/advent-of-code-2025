import sys
import numpy as np

first, *rest = [
    np.array(list(line))
    for line in sys.stdin.read().splitlines()
]
beam_count = first == 'S'
split_count = 0

for arr in rest:
    splitters = arr == '^'
    split_beams = np.where(splitters, beam_count, 0)
    unsplit_beams = np.where(~splitters, beam_count, 0)
    split_count += np.count_nonzero(split_beams)
    beam_count = (
            unsplit_beams
        +   np.roll(split_beams, -1)
        +   np.roll(split_beams, +1)
    )

print(split_count)
print(beam_count.sum())
