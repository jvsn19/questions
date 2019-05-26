# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

sieve = [False]*45
primes = []

for num in range(2, 45):
    if sieve[num]: continue
    primes.append(num)
    mult = num * 2

    while mult < 45:
        sieve[mult] = True
        mult += num

def smallest_multiple(n):
    expo = [0 for _ in range(45)]

    for prime in primes:
        for num in range(2, n+1):
            expo_count = 0
            while num >= prime and num % prime == 0:
                num //= prime
                expo_count += 1
            expo[prime] = max(expo[prime], expo_count)
    answer = 1
    for prime in primes:
        answer *= prime**expo[prime]
    return answer

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))

