class Solution:
    def minimumSteps(self, s: str) -> int:
        ans, black = 0, 0
        for i in s:
            if i == '1':
                black += 1
            else:
                ans += black
        return ans