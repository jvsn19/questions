# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

def a_n(n, q, a0):
    return (n-1)*q + a0

def pa_sum(n, q, a0):
    return ((a0 + a_n(n, q, a0)) * n) // 2

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip()) - 1
    
    print(pa_sum(n//3, 3, 3) + pa_sum(n//5, 5, 5) - pa_sum(n//15, 15, 15))
