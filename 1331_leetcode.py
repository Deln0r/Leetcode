class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = arr.copy()
        sorted_arr.sort()

        d = {}
        rank = 1
        for n in sorted_arr:
            if n not in d:
                d[n] = rank
                rank += 1

        ans = []

        for n in arr:
            ans.append(d[n])
        
        return ans