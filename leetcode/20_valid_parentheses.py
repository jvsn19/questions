# Complexity
# Time: O(N)
# Space: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        reverse = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if not (stack and stack[~0] == reverse[c]):
                    return False
                stack.pop()

        return len(stack) == 0