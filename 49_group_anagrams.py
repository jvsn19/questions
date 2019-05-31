# Complexity
# Time: O(N*K*logK), where N is the number of words and K is the maximum lenght
# Space: O(N*K)

from collections import defaultdict

class SolutionA:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())

#################################################################

# Complexity
# Time: O(N*K), where N is the number of words and K is the maximum lenght
# Space: O(N*K)

from collections import defaultdict, Counter

class SolutionB:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = {chr(char_code): 0 for char_code in range(ord('a'), ord('z')+1)}
            for c in s: key[c] += 1
            key = tuple(key.values())
            groups[key].append(s)

        return list(groups.values())