class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        s1=""
        for i in word1:
            s+=i
        for j in word2 : 
            s1+=j
        return s1==s
