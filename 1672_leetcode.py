class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for a in accounts:
            a_sum = sum(a)
            if a_sum > ans:
                ans = a_sum
        return ans