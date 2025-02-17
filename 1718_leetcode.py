class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        seen = set()
        def backtrack(i):
            if i == len(res):
                return True
            if res[i]:
                return backtrack(i+1)
            for j in range(n,0,-1):
                if j in seen:
                    continue
                seen.add(j)
                res[i] = j
                if j == 1:
                    if backtrack(i+1):
                        return True
                elif j + i < len(res) and res[i+j] == 0:
                    res[i+j] = j
                    if backtrack(i+1):
                        return True
                    res[i+j] = 0
                res[i] = 0
                seen.remove(j)
            return False
        backtrack(0)
        return res