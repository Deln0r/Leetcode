class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1)!=len(word2):
            return False

        counter1=Counter(word1)
        counter2=Counter(word2)
        num= set(word1)^set(word2)
        if sorted(counter1.values())==sorted(counter2.values()) and len(num)==0:
            return True
        return False
    
    
    
    
    
    
    
    



class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        return (f:=lambda w:(set(w),sorted(Counter(w).values())))(w1)==f(w2)