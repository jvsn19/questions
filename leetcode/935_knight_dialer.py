from collections import defaultdict

class Solution:
    def knightDialer(self, N: int) -> int:
        next_value = {
            0: [4, 6],
            1: [8, 6],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            6: [1, 7, 0],
            5: [],
            7: [6, 2],
            8: [1, 3],
            9: [2,4],
        }
        MOD = (10**9 + 7)
        memo = [[-1 for _ in range(10)] for _ in range (N + 1)]
        
        def helper(curr, size_num = 1):
            if size_num == N:
                return 1
            
            if memo[size_num][curr] != -1:
                return memo[size_num][curr]
            
            curr_count = 0
            for num in next_value[curr]:
                curr_count += helper(num, size_num + 1) % MOD
                
            memo[size_num][curr] = curr_count % MOD
            return memo[size_num][curr]
        
        return sum([helper(num) for num in range(0, 10)]) % MOD