class Solution:
    def numWays(self, words: List[str], target: str) -> int:
  
        m, n = len(words[0]),len(target)
        ans = [0] * (n + 1)
        ans[0] = 1

        ctr = list(map(Counter,zip(*map(list,words)))) # <-- transpose

        for word in ctr:
            for i in reversed(range(n)):
                ans[i+1] += ans[i] * word[target[i]] %1_000_000_007

        return ans[n] %1_000_000_007