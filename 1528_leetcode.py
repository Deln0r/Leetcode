class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(indices)

        for i, num in enumerate(indices):
            ans[num] = s[i]

        ans = ''.join(ans)
        
        return ans