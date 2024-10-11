class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for c in s:
            if c != 'i':
                ans.append(c)
            else:
                ans.reverse()
        return ''.join(ans)