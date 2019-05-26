# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

palindromes = []

for a in range(100, 1000):
    for b in range(100, 1000):
        product = a*b
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    biggest = -1

    for palindrome in palindromes:
        if palindrome < n:
            biggest = max(biggest, palindrome)
    
    print(biggest)