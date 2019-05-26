# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

from collections import defaultdict

LIMIT = 3*10**3 + 1
memo = defaultdict(int)

for a in range(1, LIMIT):
    for b in range(a + 1, LIMIT):
        c = (a**2 + b**2)**0.5
        if c - int(c) == 0: # c is an integer
            c = int(c)
            memo[a+b+c] = max(memo[a+b+c], a*b*c)
            

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(memo[n] if memo[n] else -1)
