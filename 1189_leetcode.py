class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        ans = min(c['b'], c['a'], (c['l'] // 2), (c['o'] // 2), c['n'])
        return ans