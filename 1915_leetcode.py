class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * 1024
        cnt[0] = 1
        
        ans = 0
        mask = 0
        
        chars = list(word)
        for c in chars:
            idx = ord(c) - ord('a')
            mask ^= 1 << idx
            ans += cnt[mask]
            
            for i in range(10):
                lookFor = mask ^ (1 << i)
                ans += cnt[lookFor]
                
            cnt[mask] += 1
            
        return ans