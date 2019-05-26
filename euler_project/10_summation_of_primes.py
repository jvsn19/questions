# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

LIMIT = 2*10**6 + 1
sieve = [False] * LIMIT
primes = []

for num in range(2, LIMIT):
    if sieve[num]: continue
    primes.append(num)
    mult = num * 2
    
    while mult < LIMIT:
        sieve[mult] = True
        mult += num

prev_sum = [0] * LIMIT
sum_ = 0

for num in range(2, LIMIT):
    if not sieve[num]:
        sum_ += num
    prev_sum[num] = sum_

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prev_sum[n])
