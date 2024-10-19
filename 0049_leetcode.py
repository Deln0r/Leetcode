class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {} 
        for s in strs:
            so ="".join(sorted(s)) 
            if so not in dict:
                dict[so] = [s] 
            else:
                dict[so].append(s)
        return dict.values()

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        db = {}

        for s in strs:
            key = tuple(sorted(s))
            if key in db:
                db[key].append(s)
            else:
                db[key] = [s]
        return list(db.values())