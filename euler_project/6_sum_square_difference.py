# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

LIMIT = 10**4 + 1
sum_ = 0
sum_square = 0

answer = []

for num in range(1, LIMIT):
    sum_square += (num**2)
    sum_ += num
    answer.append(sum_**2 - sum_square)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(answer[n-1])