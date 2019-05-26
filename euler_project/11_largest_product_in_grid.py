# Based on ProjectEuler+ from Hackerrank.
# Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem

def max_product(grid):
    max_prod = 1

    for row in range(20):
        for col in range(20):
            row_prod = col_prod = diag_a_prod = diag_b_prod = 1
            for i in range(4):
                row_prod *= grid[row][col + i] if col + i < 20 else 0
                col_prod *= grid[row + i][col] if row + i < 20 else 0
                diag_a_prod *= grid[row + i][col + i] if col + i < 20 and row + i < 20 else 0
                diag_b_prod *= grid[row + i][col - i] if col - i >= 0 and row + i < 20 else 0
            max_prod = max([max_prod, row_prod, col_prod, diag_a_prod, diag_b_prod])
    
    return max_prod


grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

print(max_product(grid))

