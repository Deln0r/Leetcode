class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        min_group, max_group, max_prev_group, prev_bit_cnt = 0, 0, 0, 0
        for num in nums:
            bit_cnt = num.bit_count()
            if bit_cnt != prev_bit_cnt:
                if max_prev_group > min_group:
                    return False
                max_prev_group = max_group
                max_group = min_group = num
            prev_bit_cnt = bit_cnt
            min_group, max_group = min(num, min_group), max(num, max_group)
        return max_prev_group < min_group