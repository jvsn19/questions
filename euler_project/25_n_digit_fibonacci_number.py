# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler025/problem

from math import log, ceil

memo = {}

first, second = 0, 1
num_digits = 1
idx = 1

while num_digits <= 5000:
    num_digits = ceil(log(second, 10))
    memo[num_digits] = min(memo.get(num_digits, float('inf')), idx)
    first, second = second, first + second
    idx += 1

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(memo[n])