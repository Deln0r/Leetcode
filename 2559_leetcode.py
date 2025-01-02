class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        self.vowels = set({'a','e','i','o','u'})

        def is_vowel(s):
            return s[0] in self.vowels and s[-1] in self.vowels

        prefix = [0] * len(words)
        res = [0] * len(queries)
        vowel = 0

        for i in range(len(words)):
            if is_vowel(words[i]):
                vowel += 1
            prefix[i] = vowel

        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1]
            if not l:
                res[i] = prefix[r]
            else:
                res[i] = prefix[r] - prefix[l-1]
        return res        
        