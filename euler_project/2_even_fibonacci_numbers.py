# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

def fibonacci_sum(n):
    first, second = 0, 1
    sum_ = 0

    while second < n:
        if second&1 == 0: sum_ += second
        first, second = second, first + second
        
    return sum_

n = int(input().strip())
print(fibonacci_sum(n))