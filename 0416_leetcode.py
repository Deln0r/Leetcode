class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = total_sum // 2
        reachable_sums = set()
        reachable_sums.add(0)
        
        for num in nums:
            current_sums = list(reachable_sums)
            for s in current_sums:
                new_sum = s + num
                if new_sum == target_sum:
                    return True
                if new_sum < target_sum:
                    reachable_sums.add(new_sum)
        return target_sum in reachable_sums