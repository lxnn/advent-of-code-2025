#include <stdio.h>
#include <string.h>
#include <assert.h>
#define MAXLEN 1000

long long POW10[12] = {
	1,           10,           100,           1000, 
	10000,       100000,       1000000,       10000000, 
	100000000ll, 1000000000ll, 10000000000ll, 100000000000ll
};

long long joltage(char *bank, int n) {
	assert(strlen(bank) >= n);
	assert(n <= 12);
	if (n == 0) {
		return 0;
	}
	char first_digit = 0;
	int index_of = -1;
	for (int i = 0; bank[i+n-1]; i++) {
		if (bank[i] > first_digit) {
			first_digit = bank[i];
			index_of = i;
		}
	}
	assert(index_of >= 0);
	return POW10[n-1] * (first_digit - '0') + joltage(bank + index_of + 1, n-1);
}

void test() {
	char bank[] = "818181911112111";
	assert(joltage(bank, 2) == 92);
	assert(joltage(bank, 12) == 888911112111ll);
}

int main() {
	test();
	char buffer[MAXLEN];
	long long p1=0, p2=0;
	while (fgets(buffer, MAXLEN, stdin) != NULL) {
		buffer[strcspn(buffer, "\n")] = 0; // strip newline
		p1 += joltage(buffer, 2);
		p2 += joltage(buffer, 12);
	}
	printf("Part 1: %lld\n", p1);
	printf("Part 2: %lld\n", p2);
}

