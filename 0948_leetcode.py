class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        ans = 0
        score = 0
        while l<=r:
            if score>=0 and power>=tokens[l]:
                power-=tokens[l]
                l+=1
                score += 1
                ans = max(ans,score)
            elif score>=1 and power<tokens[l]:
                power += tokens[r]
                score -=1
                r-=1
            else:
                return 0
        return ans