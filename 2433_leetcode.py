class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) <= 1: return pref

        t = pref[0]
        for i in range(1 , len(pref)):
            x = pref[i]
            pref[i] = t^pref[i]
            t = x
        return pref
