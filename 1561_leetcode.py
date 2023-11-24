class Solution:
    def maxCoins(self, piles):
        piles.sort()
        total_coins = 0
        pair = len(piles) // 3
        for i in range(pair, len(piles), 2):
            total_coins += piles[i]
        return total_coins