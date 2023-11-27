class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        for _ in range(n-1):
            dp_next = [0] * 10
            for digit in range(10):
                for move_digit in moves[digit]:
                    dp_next[digit] += dp[move_digit]
                    
            dp = dp_next
        
        return sum(dp) % (10**9 + 7)
