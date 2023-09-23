class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x:len(x))
        dp = {word:1 for word in words}
        answer = 1
        
        for word in words:
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(1+dp[prev], dp[word])
                    answer = max(answer, dp[word])
        
        return answer
