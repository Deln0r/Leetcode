class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        has = {}
        for i in arr:
            if i in has:
                has[i]+=1
            else:
                has[i]=1

        freq = set()
        
        for val in has:
            if has[val] in freq:
                return False
            freq.add(has[val])
        
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)

        occur = [v for v in c.values()]
        s_occur = set(occur)

        return len(occur) == len(s_occur)