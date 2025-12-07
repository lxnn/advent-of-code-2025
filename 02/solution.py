import sys, re

ranges = [
    tuple(map(int, part.strip().split('-')))
    for part in sys.stdin.read().split(',')
]

def is_invalid_p1(number):
    digits = str(number)
    n = len(digits)
    first_half, second_half = digits[:n//2], digits[n//2:]
    return first_half == second_half

p1 = sum(
    number
    for low, high in ranges
    for number in range(low, high+1)
    if is_invalid_p1(number)
)

print(p1)

pattern = re.compile(r'([0-9]+)\1+')

def is_invalid_p2(number):
    return pattern.fullmatch(str(number))

p2 = sum(
    number
    for low, high in ranges
    for number in range(low, high+1)
    if is_invalid_p2(number)
)

print(p2)
