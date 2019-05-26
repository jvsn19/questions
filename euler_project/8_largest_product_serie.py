# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem

from functools import reduce

def largest_product_serie(number, k):
    size_number = len(number)
    largest_product = 0

    for i in range(size_number - k + 1):
        curr_prod = reduce(lambda a,b: a*b, number[i:k + i])
        largest_product = max(largest_product, curr_prod)

    return largest_product



t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = list(map(int, list(input().strip())))
    print(largest_product_serie(num, k))

