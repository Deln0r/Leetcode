class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val = len(s) + 1
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0 
        dictionary_set = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1

            for l in range(1, i + 1): 
                if s[i-l:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[i-l])
                    
        return dp[-1]


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # Build a trie with reversed words in dictionary
        trie = {}
        for w in dictionary:
            w = reversed(w)
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['match'] = True

        def getDictWord(i, trie, s):
            '''Retrieve the lookback indices with revserd trie and index.'''
            cur = trie
            res = []
            for j in range(i+1)[::-1]:
                if s[j] in cur:
                    cur = cur[s[j]]
                    if 'match' in cur:
                        res += [j]
                else:
                    break
            return res


        n = len(s)
        dp = []
        for i in range(n):
            # - Fetch lookback indices
            lookback = getDictWord(i, trie, s)
            # - Initial cost
            if dp:
                v = dp[-1] + 1
            else:
                v = 1
            # - Optimized the cost with lookback indices
            if lookback:
                for j in lookback:
                    if j == 0:
                        v = 0
                        break
                    v = min(v, dp[j-1])
            dp += [v]
        return dp[-1]