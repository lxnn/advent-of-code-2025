import sys

banks = sys.stdin.read().splitlines()

def max_joltage_p1(bank):
    first_digit = max(bank[:-1])
    index = bank.index(first_digit)
    second_digit = max(bank[index+1:])
    return int(first_digit + second_digit)

p1 = sum(max_joltage_p1(bank) for bank in banks)
print(p1)

def max_joltage_p2(bank, n=12):
    assert len(bank) >= n
    if n == 0:
        return 0
    first_digit = max(bank[:len(bank)-(n-1)])
    remaining = bank[bank.index(first_digit)+1:]
    return 10**(n-1) * int(first_digit) + max_joltage_p2(remaining, n=n-1)

p2 = sum(max_joltage_p2(bank) for bank in banks)
print(p2)

