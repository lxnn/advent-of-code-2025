import sys

def bitset(string, ones_char):
    return int(
        ''.join(
            '1' if char == ones_char else '0'
            for char in string
        ),
        base=2,
    )

first, *rest = sys.stdin.read().splitlines()
beams = bitset(first, 'S')
split_count = 0

for line in rest:
    splitters = bitset(line, '^')
    split_beams = beams & splitters
    unsplit_beams = beams & ~splitters
    split_count += split_beams.bit_count()
    beams = unsplit_beams | split_beams << 1 | split_beams >> 1

print(split_count)
