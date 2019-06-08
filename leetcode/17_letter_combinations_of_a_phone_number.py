class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        keyboard = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        memo = {}

        def helper(idx = 0):
            if idx == len(digits):
                return ['']

            if idx in memo:
                return memo[idx]

            to_return = []
            next_call = helper(idx + 1)

            for next_str in next_call:
                for letter in keyboard[digits[idx]]:
                    to_return.append(letter + next_str)

            memo[idx] = to_return
            return to_return

        return helper()