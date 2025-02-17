from math import factorial


class Solution:
    # Also backtracking, but with more math (we don't need to calculate the num of sequences
    # of each length separately.
    def numTilePossibilities(self, tiles: str) -> int:
        remaining = list(Counter(tiles).values())
        ans = 0
        res = [0] * len(remaining)

        def backtrack(i):
            nonlocal ans
            permutations = 1
            for x in res:
                if x > 0:
                    permutations *= factorial(x)
            ans += factorial(sum(res)) // permutations

            for j in range(i, len(remaining)):
                if remaining[j] > 0:
                    res[j] += 1
                    remaining[j] -= 1
                    backtrack(j)
                    res[j] -= 1
                    remaining[j] += 1

        backtrack(0)
        return ans - 1