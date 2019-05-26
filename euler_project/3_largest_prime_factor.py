# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

def largest_prime_factor(n):
    prime = 2
    
    while prime <= n**0.5:
        while n > prime and n % prime == 0:
            n //= prime
        prime += 1
    
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))

