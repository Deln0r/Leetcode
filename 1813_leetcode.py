class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        while s1 and s2 and s1[0] == s2[0]:
            s1.pop(0)
            s2.pop(0)
         
        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()

        if not s1 or not s2:
            return True
        return False