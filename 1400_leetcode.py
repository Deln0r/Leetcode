class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        hashmap = Counter(s)
        count = 0
        for key, value in hashmap.items():
            if value % 2 == 1:
                count+=1
        return count<=k 