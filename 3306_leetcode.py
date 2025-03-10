class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def fn(op): 
            ans = []
            vowel = Counter()
            consonant = j = 0 
            for i, ch in enumerate(word): 
                if ch in "aeiou": vowel[ch] += 1
                else: consonant += 1
                while len(vowel) == 5 and op(consonant, k): 
                    if word[j] in "aeiou": 
                        vowel[word[j]] -= 1
                        if vowel[word[j]] == 0: vowel.pop(word[j])
                    else: consonant -= 1
                    j += 1
                ans.append(j)
            return ans
        
        return sum(hi-lo for hi, lo in zip(fn(ge), fn(gt)))
                