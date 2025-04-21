class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_s = 0
        max_s = 0
        cur = 0
        for d in differences:
            cur += d
            if cur < min_s:
                min_s = cur
            if cur > max_s:
                max_s = cur
        
        low_bound = lower - min_s
        high_bound = upper - max_s
        
        if high_bound < low_bound:
            return 0
        return high_bound - low_bound + 1         