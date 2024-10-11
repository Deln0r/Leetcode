class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0

        for c in s:
            if c == 'L':
                balance -= 1
            else:
                balance += 1
            if balance == 0:
                ans += 1
        return ans