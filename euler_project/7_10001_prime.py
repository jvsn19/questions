# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

not_prime = set()
prime = []

for num in range(2, 10**6):
    if len(prime) >= 10**4+5: break
    if num in not_prime: continue
    prime.append(num)
    mul = num*2
    while mul < 10**6:
        not_prime.add(mul)
        mul += num
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime[n-1])
