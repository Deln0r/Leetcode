class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        
        prev = sentence[-1]
        for i in sentence.split():
            if i[0] != prev:
                return False
            prev = i[-1]
        return True