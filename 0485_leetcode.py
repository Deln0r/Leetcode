class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
                if counter > max_: 
                    max_ += 1
            else:
                counter = 0
        return max_