class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i


from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
    	return list(Counter(t) - Counter(s))[0]
